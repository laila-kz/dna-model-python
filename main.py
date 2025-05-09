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

