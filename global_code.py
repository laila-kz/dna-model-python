import random
import sys
from bitarray import bitarray

# Dictionnaire de complémentarité pour les bases ADN.
# Il sera utilisé pour déterminer la base complémentaire d'une entrée donnée.
complements = {"A": "T", "T": "A", "C": "G", "G": "C"}


# =============================================================================
# Classe Nucleotide
# =============================================================================
class Nucleotide:
    """
    Représente un nucléotide avec une base (A, T, C ou G) et un type (purine/pyrimidine).
    La classe gère la conversion en majuscules et vérifie la validité de l'entrée.
    """

    def __init__(self, nom):
        # Vérifier que le paramètre 'nom' est un caractère.
        while True:
            try:
                if not isinstance(nom, str):
                    raise ValueError("Le nucléotide doit être fourni en tant que chaîne (par exemple 'A', 'T', 'C' ou 'G').")
                break
            except ValueError as e:
                nom=int(input("Veuillez entrer le symbole d'une base azotée: "))
        
        # Conversion de l'entrée en majuscules (même si ce n'est pas une base azotée) pour uniformiser l'information.
        nom = nom.upper()

        # Si le caractère n'est pas valide, on choisit aléatoirement une base parmi A, T, C, G.
        if nom not in ["A", "T", "C", "G"]:
            print("Caractère entré invalide...\nChoix aléatoire de caractère")
            self._nom = random.choice(["A", "T", "C", "G"])
            print(f"Nouveau nucléotide : {self._nom}")
        else:
            self._nom = nom
        
        # Dictionnaire pour déterminer le type de la base (purine ou pyrimidine).
        types = {'A': 'purine', 'G': 'purine', 'T': 'pyrimidine', 'C': 'pyrimidine'}
        self._type = types.get(self._nom, None)
        
        # Calcul de la base complémentaire.
        self._complementaire = self.getComplementaire()

    def symbol(self):
        """
        Retourne le symbole de la base (ex: 'A').
        """
        return self._nom

    def getComplementaire(self):
        """
        Retourne la base complémentaire selon le dictionnaire 'complements'.
        """
        return complements.get(self._nom, None)

    def toString(self):
        """
        Retourne une représentation textuelle de ce nucléotide.
        Par exemple, "P-D-A" pour une base A.
        """
        return f"P-D-{self._nom}"


# =============================================================================
# Classes spécialisées pour chaque base (A, T, C, G)
# Ils héritent de Nucleotide pour simplifier la création d'instances valides.
# =============================================================================
class A(Nucleotide):
    def __init__(self):
        super().__init__('A')


class T(Nucleotide):
    def __init__(self):
        super().__init__('T')


class C(Nucleotide):
    def __init__(self):
        super().__init__('C')


class G(Nucleotide):
    def __init__(self):
        super().__init__('G')


# =============================================================================
# Fonction utilitaire pour générer un nucléotide aléatoire.
# =============================================================================
def generate_random_nucleotide():
    """
    Génère un nucléotide au hasard parmi A, T, C et G.
    Retourne une instance de A, T, C ou G.
    """
    return random.choice([A(), T(), C(), G()])


# =============================================================================
# Classe PontADN
# =============================================================================
class PontADN:
    """
    Représente une paire de bases complémentaires (un pont d'ADN).
    On construit la paire à partir d'une base fournie. La base gauche et
    sa complémentaire (base droite) sont instanciées via le mapping vers les
    classes spécialisées. La conversion de l'entrée en majuscule est effectuée.
    """

    def __init__(self, symbol=None):
        # Vérifier que le paramètre 'symbol' est un caractère.
        while True:
            try:
                if not isinstance(symbol, str):
                    raise ValueError("Le nucléotide doit être fourni en tant que chaîne (par exemple 'A', 'T', 'C' ou 'G').")
                break
            except ValueError as e:
                symbol=int(input("Veuillez entrer le symbole d'une base azotée: "))

        # Conversion en majuscules.
        symbol = symbol.upper()
        
        # Si le symbole n'est pas valide, on en choisit un aléatoirement.
        if symbol not in ["A", "T", "C", "G"]:
            print("Caractère entré invalide...\nChoix aléatoire de caractère")
            symbol = random.choice(["A", "T", "C", "G"])
        
        # Création des instances de base selon le mapping.
        nucleotide_map = {"A": A, "T": T, "C": C, "G": G}
        self._baseGauche = nucleotide_map[symbol]()  # Base gauche
        self._baseDroite = nucleotide_map[complements.get(symbol, "A")]()  # Base droite complémentaire

    def symbol(self):
        """
        Retourne le symbole de la base gauche.
        """
        return self._baseGauche.symbol()
    
    def toString(self):
        """
        Renvoie la représentation sous forme "A-T", "C-G", etc.
        """
        return f"{self._baseGauche.symbol()}-{self._baseDroite.symbol()}"


    def nbHydrogen(self):
        """
        Retourne le nombre de liaisons hydrogène en fonction de la base gauche.
            - 2 liaisons pour A et T.
            - 3 liaisons pour C et G.
        """
        if self._baseGauche.symbol() in ["A", "T"]:
            return 2
        elif self._baseGauche.symbol() in ["C", "G"]:
            return 3
        return 0


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
                self.brin = [PontADN() for _ in range(nb)]
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
                    raise ValueError("Le paramètre doit être une chaîne de caractères.")
                
                # Conversion en majuscules pour traitement uniforme.
                cara = cara.upper()
                if cara not in ["A", "T", "C", "G"]:
                    raise ValueError("ERREUR! Le caractère doit être soit A, T, C, ou G.")
                
                # Affichage préliminaire de la liaison recherchée.
                print(f"Recherche de la première occurrence de la liaison {PontADN(cara).toString()}...")
                pos = 0
                for elm in self.brin:
                    if elm._baseGauche.symbol() == cara:
                        return f"Liaison {PontADN(cara).toString()} trouvée à la position {pos+1}"
                    pos += 1
                return f"Liaison {PontADN(cara).toString()} non trouvée !"
            
            except ValueError as e:
                print(e)
                cara = input("Veuillez entrer un caractère valide (A, T, C, G): ")

    def displayFragment(self, pos=1, leng=10):
        """
        Affiche graphiquement un fragment de la molécule.
        L'affichage utilise des symboles pour représenter visuellement les ponts.
        """
        while True:
            try:
                if pos < 1 or leng <= 0:
                    raise ValueError(
                        "La position doit être supérieure à 0 et la longueur positive."
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
                        return "Il s'agit de la molécule entière !"
                    else:
                        return "La chaîne ne correspond pas à la molécule entière."
                
                # Recherche du motif dans le brin principal ou dans son complément.
                for i in range(self.nb - len(chn) + 1):
                    if brinChn[i:i+len(chn)] == chn or complement_brinChn[i:i+len(chn)] == chn:
                        return f"Motif trouvé à la position {i + 1}"
                
                return "Motif non trouvé."
            
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
        return total

    def optimizedSize(self):
        """
        Renvoie la taille en mémoire de la représentation compacte obtenue grâce à bitarray.
        """
        compact = self.compactRepresentation()
        return sys.getsizeof(compact)

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
        return factor


# =============================================================================
# Exemple d'utilisation et test du module
# =============================================================================
if __name__ == "__main__":
    # Création d'une molécule d'ADN avec 50 ponts
    molecule = MoleculeADN(nb=50)
    
    # Affichage d'un fragment de la molécule (positions 1 à 10)
    print("Fragment de la molécule (positions 1 à 10) :")
    print(molecule.getFragment(1, 10))
    
    # Recherche d'un motif dans la molécule (ici 'aaa' en minuscules, qui sera converti en majuscules)
    print("\nRecherche du motif 'aaa' (entrée en minuscules) :")
    res = molecule.searchPattern("aaa")
    print(res)
    
    # Affichage graphique d'un fragment de la molécule (positions 1 à 5)
    print("\nAffichage d'un fragment de la molécule :")
    molecule.displayFragment(1, 5)
    
    # Calcul du taux de fusion pour un fragment de la molécule (positions 1 à 10)
    print("\nCalcul du taux de fusion (positions 1 à 10) :")
    print(molecule.fusionRate(1, 10))
    
    # Partie d'optimisation mémoire
    print("\n--- Optimisation Mémoire ---")
    compact_ba = molecule.compactRepresentation()
    print("Représentation compacte (bitarray):", compact_ba)
    
    raw_size = molecule.rawSize()
    opt_size = molecule.optimizedSize()
    print(f"Taille brute approximative: {raw_size} octets")
    print(f"Taille optimisée (bitarray): {opt_size} octets")
    
    factor = molecule.optimizationFactor()
    print(f"Facteur d'optimisation: {factor:.2f} (objectif: 1/8 ou mieux)")