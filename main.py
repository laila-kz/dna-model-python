import random

class Nucleotide:
    def __init__(self, nom, type_base, complementaire):
        self.nom = nom
        self.type = type_base
        self.complementaire = complementaire

    def getComplementaire(self):
        return self.complementaire

    def toString(self):
        return f"P-D-{self.nom}"


class A(Nucleotide):
    def __init__(self):
        super().__init__('A', 'purine', 'T')

class T(Nucleotide):
    def __init__(self):
        super().__init__('T', 'pyrimidine', 'A')

class C(Nucleotide):
    def __init__(self):
        super().__init__('C', 'pyrimidine', 'G')

class G(Nucleotide):
    def __init__(self):
        super().__init__('G', 'purine', 'C')


def generate_random_nucleotide():
    return random.choice([A(), T(), C(), G()])


class PontADN:
    def __init__(self, symbol=None):
        if symbol not in ["A", "T", "C", "G"]:
            print('Caractere entré invalide...\nChoix aléatoire de caractère')
            symbol = random.choice(["A", "T", "C", "G"])
        self.baseGauche = symbol  # define the left base
        self.baseDroite = Nucleotide(symbol).getComplement()
    
    def toString(self):
        return f"{self.baseGauche}-{self.baseDroite}"
    
    def nbHydrogen(self):
        if self.baseGauche in ["A", "T"]:
            return 2
        elif self.baseGauche in ["C", "G"]:
            return 3
        return 0

HEAD
#############################
#### WILLY'S CODE  ##########
#############################

import random

class Nucleotide:
    def __init__(self, symbol=None):
        if symbol not in ["A", "T", "C", "G"]:
            print('Caractere entré invalide...\nChoix aléatoire de caractère')
            self.symbol = random.choice(["A", "T", "C", "G"])
        else:
            self.symbol = symbol
        self.complement = self.getComplement()

    def getComplement(self):
        complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
        return complements.get(self.symbol, None)
    
    def toString(self):
        return f"P-D-{self.symbol}"


class PontADN:
    def __init__(self, symbol=None):
        if symbol not in ["A", "T", "C", "G"]:
            print('Caractere entré invalide...\nChoix aléatoire de caractère')
            symbol = random.choice(["A", "T", "C", "G"])
        self.baseGauche = symbol  # define the left base
        self.baseDroite = Nucleotide(symbol).getComplement()
    
    def toString(self):
        return f"{self.baseGauche}-{self.baseDroite}"
    
    def nbHydrogen(self):
        if self.baseGauche in ["A", "T"]:
            return 2
        elif self.baseGauche in ["C", "G"]:
            return 3
        return 0


 7fd39ce (changed the first class using heritage)
class MoleculeADN:
    def __init__(self, nb=50):
        self.brin = [PontADN() for _ in range(nb)]
        
    def getFragment(self, pos=0, leng=10):
        # Adjust pos and leng to avoid index errors
        fragment = []
        for i in range(pos, min(pos + leng, len(self.brin))):
            fragment.append(self.brin[i].toString())
        return "\n".join(fragment)
    
    def firstOccurence(self, cara): #A-T, T-A
        if cara not in ["A", "T", "C", "G"]:
            print("ERREUR!\nLe caractère doit être soit A, T, C, ou G")
            return
        print(f"Recherche de la première occurence de la liaison {PontADN(cara).toString()}")
        
        pos = 0
        for elm in self.brin:
            if elm.baseGauche == cara:
                return f"Liaison {PontADN(cara).toString()} trouvé à la position {pos+1}"
            pos += 1
        return f"Liaison {PontADN(cara).toString()} non trouvée !"
    
    def displayFragment(self, pos=0, leng=10):
        egal = {"A": "=", "T": "=", "C": "≡", "G": "≡"}
        for i in range(pos, min(pos + leng, len(self.brin))):
            base = self.brin[i].baseGauche
            print("P       P")
            print(" \\     /")
            print(f"  D{base}{egal[base]}{self.brin[i].baseDroite}D")
            print(" /     \\")
        print("P       P")
    
    def fusionRate(self, pos=0, leng=10):
        at = 0
        cg = 0
        for i in range(pos, min(pos + leng, len(self.brin))):
            if self.brin[i].baseGauche in ["A", "T"]:
                at += 1
            else:
                cg += 1
        # Prevent division by zero
        return at/cg if cg != 0 else float('infini !')
<<<<<<< HEAD
    
    # def searchPattern(self, pattern):
    #     def check(x):
    #         if x not in ["A","T","C","G"] :
    #             return f"ERREUR ! {x} n'est pas une base"
    #     a= list(map(check,pattern))
    #     a=len(a)
        
    #     for i in range(len(self.brin)):
    #         ind=0
    #         if self.
=======

    # def searchPattern(self, pattern):
    #      def check(x):
    #          if x not in ["A","T","C","G"] :
    #              return f"ERREUR ! {x} n'est pas une base"
    #      a= list(map(check,pattern))
    #      a=len(a)
        
    #      for i in range(len(self.brin)):
    #          ind=0
    #          if self.
    
>>>>>>> 7fd39ce (changed the first class using heritage)
