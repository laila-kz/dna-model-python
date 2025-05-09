class nucleotide :
    def __init__ (self,nom, type, complementaire):
        self.nom = nom
        self.type= type
        self.complementaire = complementaire
    
    def toString(self):
        return self.complementaire
    

    def geComplemantaire(self):
        return self.complementaire
    
class A(nucleotide):
    def __init__(self):
        super().__init__('A', 'purine', 'T')

class T(nucleotide):
    def __init__(self):
        super().__init__('T', 'purine', 'A')

class C(nucleotide):
    def __init__(self):
        super().__init__('C', 'purine', 'G')


class G(nucleotide):
    def __init__(self):
        super().__init__('G', 'purine', 'C')


class pontADN:
    def __init__(self,baseGauche, baseDroite, liaisons_h):
        self.baseGauche= baseGauche
        self.baseDroite= baseDroite
        if self.gauche.getComplementaire() != self.baseDroite:
            raise ValueError("Les bases ne sont pas complémentaires !")
        self._typePont= f"{self.baseGauche}-{self.baseDroite}"
        self.liasions_h= liaisons_h

        

    def getType(self):
        return self._typePont

    def toString(self):
        if self.liaisons_h == 2:
            return f"{self.baseGauche} = {self.baseDroite}"
        elif self.liaisions_h == 3:
            return f"{self.baseGauche} ≡ {self.baseDroite}"

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
    
    # def searchPattern(self, pattern):
    #     def check(x):
    #         if x not in ["A","T","C","G"] :
    #             return f"ERREUR ! {x} n'est pas une base"
    #     a= list(map(check,pattern))
    #     a=len(a)
        
    #     for i in range(len(self.brin)):
    #         ind=0
    #         if self.