import random
complements = {"A": "T", "T": "A", "C": "G", "G": "C"}

class Nucleotide:
    def __init__(self, nom):
        if nom not in ["A", "T", "C", "G"]:
            print('Caractere entré invalide...\nChoix aléatoire de caractère')
            self._nom = random.choice(["A", "T", "C", "G"])
            print (f"Nouveau nucléotide : {self._nom}")
        else:
            self._nom = nom
            
        types={'A':'purine','G':'purine','T':'pyrimidine','C':'pyrimidine'}
        self._type = types.get(self._nom, None)
        self._complementaire = self.getComplementaire()
    
    def symbol(self):
        return self._nom

    def getComplementaire(self):
        return complements.get(self._nom, None)

    def toString(self):
        return f"P-D-{self._nom}"


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


# Fonctions pour générer un seul nucléotide
def generate_random_nucleotide():
    
    """ Generates a random nucleotide by selecting one of the four DNA bases: A, T, C, or G.
        Returns: A randomly selected nucleotide object (A, T, C, or G). """
    
    return random.choice([A(), T(), C(), G()])


class PontADN:
    def __init__(self, symbol=None):
        if symbol not in ["A", "T", "C", "G"]:
            print('Caractere entré invalide...\nChoix aléatoire de caractère')
            symbol = random.choice(["A", "T", "C", "G"])
        
        # Crée l'objet nucléotide correspondant
        nucleotide_map = {"A": A, "T": T, "C": C, "G": G}
        self._baseGauche = nucleotide_map[symbol]()  # Instance de la classe correspondante
        self._baseDroite = nucleotide_map[complements.get(symbol, "A")]()  # Instance de la classe complémentaire
    
    def toString(self):
        return f"{self._baseGauche.symbol()}-{self._baseDroite.symbol()}"
    
    def symbol(self):
        return f"{self._baseGauche.symbol()}"
    
    def nbHydrogen(self):
        if self._baseGauche.symbol() in ["A", "T"]:
            return 2
        elif self._baseGauche.symbol() in ["C", "G"]:
            return 3
        return 0

class MoleculeADN:
    def __init__(self, nb=50):
        while True:
            try:
                if nb <= 0:
                    raise ValueError("Le nombre de ponts ADN doit être supérieur à 0.")
                self.brin = [PontADN() for _ in range(nb)]
                break
            except ValueError as e:
                print(e)
                nb = int(input("Entrer un nombre valide: "))
        
    def getFragment(self, pos=1, leng=10):
        try:
            # Validate input parameters
            if pos < 1 or leng <= 0:
                raise ValueError("Position must be non-negative and length must be greater than 0.")
            # Adjust pos and leng to avoid index errors
            fragment = []
            pos-=1
            for i in range(pos, min(pos + leng, len(self.brin))):
                fragment.append(self.brin[i].toString())
            return "\n".join(fragment)
        except ValueError as e:
            print(e)
            # Prompt user for new input and retry
            pos = int(input("Enter a valid position (non-negative): "))
            leng = int(input("Enter a valid length (greater than 0): "))
            return self.getFragment(pos, leng)
    
    def firstOccurence(self, cara): #A-T, T-A
        while True:
            try:    
                if cara not in ["A", "T", "C", "G"]:
                    raise ValueError("ERREUR!\nLe caractère doit être soit A, T, C, ou G")
                print(f"Recherche de la première occurence de la liaison {PontADN(cara).toString()}")
                break
            except ValueError as e:
                print(e)
                cara = int(input("Veuillez entrer un caractère valide : "))
        pos = 0
        for elm in self.brin:
            if elm.toString() == cara:
                return f"Liaison {PontADN(cara).toString()} trouvé à la position {pos+1}"
            pos += 1
        return f"Liaison {PontADN(cara).toString()} non trouvée !"
    
    
    def displayFragment(self, pos=1, leng=10):
        while True:
            try:
                if (pos < 1 or leng <=0):
                    raise ValueError("La position doit être supérieure à 0 et la longueur positive")
                egal = {"A": "=", "T": "=", "C": "≡", "G": "≡"}
                pos-=1
                for i in range(pos, min(pos + leng, len(self.brin))):
                    base = self.brin[i].toString()
                    print("P       P")
                    print(" \\     /")
                    print(f"  D{base}{egal[base]}{complements.get(base, None)}D")
                    print(" /     \\")
                print("P       P")
                break
            except ValueError as e:
                print(e)
                pos = int(input("Veuillez entrer la position de premier élément du fragment à faire apparaître: "))
                leng = int(input("Veuillez entrer la longueur du fragment à faire apparaître: "))
    
    def fusionRate(self, pos=0, leng=10):
        while True:
            try :
                if (pos < 1 or leng <=0):
                    raise ValueError("La position doit être supérieure à 0 et la longueur positive")
                at = 0
                cg = 0
                for i in range(pos, min(pos + leng, len(self.brin))):
                    if self.brin[i].toString() in ["A", "T"]:
                        at += 1
                    else:
                        cg += 1
                # Prevent division by zero
                return at/cg if cg != 0 else float('infini !')
            except ValueError as e:
                print(e)
                pos = int(input("Veuillez entrer la position de premier élément du fragment à faire apparaître: "))
                leng = int(input("Veuillez entrer la longueur du fragment à faire apparaître: "))