import time
import random
from .nucleotide import A, T, C, G, complements, Nucleotide

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

    def __init__(self, symbol=None, choix=None):
        
        # fonction appelée lors de la création des ponts.
        def creation(self, symbol):
            nucleotide_map = {"A": A, "T": T, "C": C, "G": G}
            self._baseGauche = nucleotide_map[symbol]()  # Base gauche
            self._baseDroite = nucleotide_map[complements.get(symbol, "A")]()
        
        attempt=1
        if choix==None :
            while True:    
                try:
                    choix = int(input("Comment désirez-vous créer votre pont ?\n[1] De façon aleatoire\n[2] Avec un symbole azoté bien défini\n==>Votre choix: "))
                except ValueError:
                    print("\nERREUR DE SAISIE ! Veuillez entrer un nombre entier.")
                    choix = None
                attempt+=1
                if (choix not in [1, 2] and attempt<6) :
                    print(f"\nIl vous reste {5-attempt} tentatives"); time.sleep(2)
                if (choix in [1, 2]) :
                    break
                if (attempt >= 6) :
                    print("\nEXCES DE TENTATIVES OU VALEUR INCORRECTE ! Choix aléatoire..."); time.sleep(2)
                    choix=1
                    break

        if (choix==1):
            symbol = random.choice(["A", "T", "C", "G"]) if symbol is None else symbol
            creation(self,symbol=symbol)
        elif (choix==2):
            if (symbol is None) :
                symbol=Nucleotide().symbol()
            creation(self,symbol=symbol)
                
    
    def symbol_droite(self):
        """
        Retourne le symbole de la base gauche.
        """
        return self._baseDroite.symbol()


    def symbol_gauche(self):
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

