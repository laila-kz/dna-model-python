import random
from .nucleotide import A, T, C, G, complements

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

