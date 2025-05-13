import random

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

