import sys
import random
from bitarray import bitarray # type: ignore
from .pont_adn import PontADN
from .nucleotide import complements

# =============================================================================
# Classe MoleculeADN
# =============================================================================
class MoleculeADN:
    """
    Représente une molécule d'ADN constituée d'une liste de ponts (PontADN).
    Fournit plusieurs méthodes pour extraire un fragment, rechercher un motif,
    afficher un fragment de manière graphique et mesurer le taux de fusion.
    
    De plus, des méthodes d'optimisation mémoire sont intégrées:
      - compactRepresentation() : Représente la molécule sous forme compacte en utilisant bitarray.
        # Cette méthode réduit la taille en mémoire en codant chaque base sur 2 bits au lieu d'utiliser des objets Python complets.
        
      - rawSize() : Calcule la taille approximative du stockage naïf de l'objet.
        # Cette méthode évalue la taille brute en octets de la liste d'objets PontADN et de leurs attributs.
        
      - optimizedSize() : Calcule la taille de la représentation compacte.
        # Cette méthode évalue la taille de la représentation compacte en mémoire en tenant compte des attributs des objets.
        
      - optimizationFactor() : Calcule le facteur d'optimisation (rapport rawSize/optimizedSize  qui doit === 1/8).
        # Cette méthode évalue le rapport entre la taille brute et la taille optimisée.
    """

    def __init__(self, nb=50):
        # Initialisation : Le nombre de ponts doit être strictement supérieur à 0.
        while True:
            try:
                if nb <= 0:
                    raise ValueError("Le nombre de ponts ADN doit être supérieur à 0.")
                self.nb = nb
                # Création d'une liste de ponts.
                choix = int(input("vous désirez un choix aléatoire(1) de la base ou pas(2) ? [1/2]\n==>"))
                self.brin = [PontADN(choix=choix) for _ in range(nb)]
                break
            except ValueError as e:
                print(e)
                nb = int(input("Entrer un nombre valide: "))
    
    def getFragment(self, pos=1, leng=10):
        """
        Extrait et retourne un fragment de la molécule.
        
        Paramètres:
            pos (int) : Position de départ (indice 1-based)
            leng (int) : Longueur du fragment à extraire
            
        La position est convertie en indice 0-based.
        """

        try:
            if pos < 1 or leng <= 0:
                raise ValueError(
                    "La position doit être supérieure à 0 et la longueur positive."
                )
            
            fragment = []
            pos -= 1  # Conversion en indice 0-based
            for i in range(pos, min(pos + leng, len(self.brin))):
                fragment.append(self.brin[i].toString())
            return "\n".join(fragment)
        except ValueError as e:
            print(e)
            pos = int(input("Veuillez entrer la position du premier élément du fragment (>0): "))
            leng = int(input("Veuillez entrer la longueur du fragment (>=0): "))
            return self.getFragment(pos, leng)

    def firstOccurence(self, cara):
        """
        Recherche et retourne la première occurrence d'un pont dont la base gauche
        correspond au caractère 'cara'. Le paramètre est converti en majuscule pour la cohérence.
        """
        while True:
            try:
                # Vérification du type d'entrée.
                if not isinstance(cara, str):
                    raise ValueError("ERREUR! Le paramètre doit être une chaîne de caractères.")
                
                # Conversion en majuscules pour traitement uniforme.
                cara = cara.upper()
                if cara not in ["A", "T", "C", "G"]:
                    raise ValueError("ERREUR! Le caractère doit être soit A, T, C, ou G.")
                
                # Affichage préliminaire de la liaison recherchée.
                chn = PontADN(cara, 2).toString()
                print(f"Recherche de la première occurrence de la liaison {chn}...")
                pos = 0
                for elm in self.brin:
                    if elm._baseGauche.symbol() == cara:
                        print (f"***Liaison {chn} trouvée à la position {pos+1}")
                        return
                    pos += 1
                print (f"***Liaison {chn} non trouvée !")
                return
            
            except ValueError as e:
                print(e)
                cara = input("Veuillez entrer un caractère valide (A, T, C, G): ")

    
    def displayFragment(self, pos=-1, leng=-1):
            """
            Affiche graphiquement un fragment de la molécule.
            L'affichage utilise des symboles pour représenter visuellement les ponts.
            """
            
            while True:
                try:
                    if pos < 1 or leng <= 0:
                        raise ValueError(
                            "\n\nLa position doit être supérieure à 0 et la longueur positive."
                        )
                    
                    # Dictionnaire pour choisir le type de liaison visuelle (p.ex. '=' ou '≡')
                    egal = {"A": "=", "T": "=", "C": "≡", "G": "≡"}
                    pos -= 1  # Conversion en index 0-based
                    for i in range(pos, min(pos + leng, len(self.brin))):
                        # Récupération de la base gauche pour l'affichage.
                        base = self.brin[i]._baseGauche.symbol()
                        print("P       P")
                        print(" \\     /")
                        # Affiche le pont avec le symbole et le mot de liaison correspondant.
                        print(f"  D{base}{egal[base]}{complements.get(base, '?')}D")
                        print(" /     \\")
                    print("P       P")
                    break
                except ValueError as e:
                    print(e)
                    pos = int(input("Veuillez entrer la position (>0): "))
                    leng = int(input("Veuillez entrer la longueur (>=0): "))


    def fusionRate(self, pos=1, leng=10):
        """
        Calcule et retourne le taux de fusion pour un fragment de la molécule.
        
        Le taux de fusion est ici défini comme le rapport (nombre de bases A ou T) / 
        (nombre de bases C ou G) pour le fragment considéré.
        """
        while True:
            try:
                if pos < 1 or leng <= 0:
                    raise ValueError(
                        "La position doit être supérieure à 0 et la longueur positive."
                    )
                at = 0
                cg = 0
                pos -= 1  # Conversion en indice 0-based
                for i in range(pos, min(pos + leng, len(self.brin))):
                    if self.brin[i]._baseGauche.symbol() in ["A", "T"]:
                        at += 1
                    else:
                        cg += 1
                return at / cg if cg != 0 else float('infini !')
            
            except ValueError as e:
                print(e)
                pos = int(input("Veuillez entrer la position (>0): "))
                leng = int(input("Veuillez entrer la longueur (>0): "))

    def searchPattern(self, chn="AAA"):
        """
        Cherche un motif (chaîne de bases) au sein du brin principal de la molécule.
        
        Le motif est recherché dans la séquence formée par les bases gauches des ponts
        ainsi que dans leur complémentaire.
        Le paramètre 'chn' est attendu sous forme de chaîne et converti en majuscules.
        """
        while True:
            try:
                if not isinstance(chn, str):
                    raise ValueError("La chaîne doit être une chaîne de caractères.")
                
                # Conversion en majuscules pour normaliser
                chn = chn.upper()
                if not all(cara in ["A", "T", "C", "G"] for cara in chn):
                    raise ValueError("Problème : la chaîne doit être composée uniquement de A, T, C, G.")
                if len(chn) > self.nb:
                    raise ValueError("Longueur de la chaîne trop longue !")
                
                # Construction d'une chaîne complète à partir du brin principal (la séquence des bases gauches)
                brinChn = ''.join(elm._baseGauche.symbol() for elm in self.brin)
                complement_brinChn = ''.join(complements[cara] for cara in brinChn)
                
                # Si la chaîne a exactement la longueur du brin, on compare l'ensemble de la molécule.
                if len(chn) == self.nb:
                    if brinChn == chn or complement_brinChn == chn:
                        print("***Il s'agit de la molécule entière !")
                        break
                    else:
                        print( "***La chaîne ne correspond pas à la molécule entière.")      
                        break          
                # Recherche du motif dans le brin principal ou dans son complément.
                for i in range(self.nb - len(chn) + 1):
                    if brinChn[i:i+len(chn)] == chn or complement_brinChn[i:i+len(chn)] == chn:
                        print(f"***Motif trouvé à la position {i + 1}")
                        break
                    else :
                        print("***Motif non trouvé.")
                        break
            
            except ValueError as e:
                print(e)
                chn = input("Veuillez entrer une chaîne valide (composée de A, T, C, G) : ")

    # -----------------------------------------------------------------------------
    # Partie Optimisation Mémoire
    # -----------------------------------------------------------------------------

    def compactRepresentation(self):
        """
        Convertit la séquence d'ADN (le brin principal) en une représentation compacte
        utilisant la bibliothèque bitarray.

        Chaque base est codée sur 2 bits comme suit :
            - A : '00'
            - T : '01'
            - C : '10'
            - G : '11'

        Retourne un objet bitarray représentant la molécule.
        """
        mapping = {"A": "00", "T": "01", "C": "10", "G": "11"}
        bits_string = ""
        for pont in self.brin:
            base = pont._baseGauche.symbol()
            
            # Vérifier que la base est dans le mapping pour éviter toute erreur inattendue.
            if base not in mapping:
                raise ValueError(f"Base inconnue dans la molécule: {base}")
            
            bits_string += mapping[base]
        
        ba = bitarray(endian='big')
        """La méthode `bitarray` crée un tableau de bits, et l'attribut `endian='big'` 
        spécifie que les bits les plus significatifs sont stockés en premier :
        
        Imaginons que vous voulez représenter le nombre 5 en binaire (101), et que vous utilisez un tableau de 8 bits :
        Avec endian='big', les bits sont stockés comme : 00000101 (les bits importants à gauche).
        Avec endian='little', les bits sont stockés comme : 10100000 (les bits importants à droite).
        """
        
        ba.extend(bits_string)
        """
        La méthode `extend` permet d'ajouter la chaîne de bits à l'objet bitarray.
        Fonctionnement :
        La méthode lit chaque caractère de la chaîne bits_string et l'ajoute comme un bit dans le tableau ba.
        Si bits_string = "1101", alors après cette opération, ba contiendra les bits [1, 1, 0, 1].        
        """
        print(f"- Représentation compacte de la chaine en écriture bitarray : {ba}")
        return ba

    def rawSize(self):
        """
        Calcule une taille approximative en mémoire de la représentation naïve
        de la molécule, c'est-à-dire la taille occupée par la liste contenant tous les objets.
        
        Remarque : sys.getsizeof ne prend pas en compte la totalité de la mémoire 
        utilisée par les objets imbriqués, mais donne une estimation suffisante pour comparer.
        """
        total = sys.getsizeof(self.brin)
        for pont in self.brin:
            total += sys.getsizeof(pont)
            total += sys.getsizeof(pont._baseGauche)
            total += sys.getsizeof(pont._baseDroite)
        print(f"- Taille approximative en mémoire de la molécule: {total} octets")
        return total

    def optimizedSize(self):
        """
        Renvoie la taille en mémoire de la représentation compacte obtenue grâce à bitarray.
        """
        compact = self.compactRepresentation()
        total =sys.getsizeof(compact)
        print(f"- Taille approximative en mémoire de représentation compacte: {total} octets")
        return total

    def optimizationFactor(self):
        """
        Calcule et renvoie le facteur d'optimisation obtenu grâce à la représentation compacte.
        
        Ce facteur est défini par le rapport : taille brute / taille optimisée.
        L'objectif est d'atteindre un facteur d'au moins 1/8.
        """
        raw = self.rawSize()
        compact = self.optimizedSize()
        try:
            factor = raw / compact
        except ZeroDivisionError:
            raise ValueError("La taille optimisée est nulle, vérification impossible.")
        return round(factor, 3)

def displayFragment(liste=None):
        """
        Affiche graphiquement un fragment récupéré de la molécule.
        L'affichage utilise des symboles pour représenter visuellement les ponts.
        """        
        # Dictionnaire pour choisir le type de liaison visuelle (p.ex. '=' ou '≡')
        egal = {"A": "=", "T": "=", "C": "≡", "G": "≡"}
        indice = 0
        for _ in range(len(liste)):
            # Récupération de la base gauche pour l'affichage.
            base = liste[indice]
            print("P       P")
            print(" \\     /")
            # Affiche le pont avec le symbole et le mot de liaison correspondant.
            print(f"  D{base}{egal[base]}{complements.get(base, '?')}D")
            print(" /     \\")
            #compare si l'on est arrivé à la fin de la liste
            indice+=4
            if indice >= len(liste): break
        print("P       P")
