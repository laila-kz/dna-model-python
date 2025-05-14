import time

from python.nucleotide import Nucleotide

#  1   TEST POUR LES NUCLEOTIDES
## 1.1 BASE BIEN DEFINIE
"""
A = Nucleotide("A")
print("1.1 BASE BIEN DEFINIE par l'utilisateur"); time.sleep(3)
print(f"La base azotée de l'actuel nucléotide est: {A.symbol()}"); time.sleep(3)
print(f"La base azotée complémentaire de l'actuel nucléotide est: {A.getComplementaire()}"); time.sleep(3)
print(f"La représentation complète de l'actuel nucléotide est: {A.toString()}"); time.sleep(3)
print("Test 1.1 REUSSI\n\n\n\n----\n\n"); time.sleep(5)

print("---TEST AVEC UNE BASE INCONNUE (sans paramètre)---\n")
## 1.2 BASE INCONNUE
B = Nucleotide()
print("BASE INCONNUE, non entrée par l'utilisateur: "), time.sleep(3)
print(f"La base azotée de l'actuel nucléotide est: {B.symbol()}"); time.sleep(3)
print(f"La base azotée complémentaire de l'actuel nucléotide est: {B.getComplementaire()}"); time.sleep(3)
print(f"La représentation complète de l'actuel nucléotide est: {B.toString()}"); time.sleep(3)
print("Test 1.2 REUSSI\n\n\n\n----\n\n"); time.sleep(5)
"""

############################################################################
############################################################################

#  2   TEST POUR LES PONTS
## 2.1 PONT à base BIEN DEFINIE
from python.pont_adn import PontADN

print("\n\n---TEST AVEC UN PONT BIEN DEFINI---\n")
A = PontADN("A", 2)
print("NUCLEOTIDE du pont BIEN DEFINI par l'utilisateur: A"); time.sleep(3)
print(f"La base gauche du pont est: {A.symbol_gauche()}"); time.sleep(3)
print(f"La base droite du pont est: {A.symbol_droite()}"); time.sleep(3)
print(f"La représentation complète du pont est: {A.toString()}"); time.sleep(3)
print(f"Le nombre de liaisons hydrogène est: {A.nbHydrogen()}"); time.sleep(3)
print("Test 2.1 REUSSI\n\n\n\n----\n\n"); time.sleep(5)


print("---TEST AVEC UN PONT INCONNU (sans paramètre)---\n")
## 2.2 PONT INCONNU
B = PontADN(); time.sleep(3)
print(f"La base gauche du pont est: {B.symbol_gauche()}"); time.sleep(3)
print(f"La base droite du pont est: {B.symbol_droite()}"); time.sleep(3)
print(f"La représentation complète du pont est: {B.toString()}"); time.sleep(3)
print(f"Le nombre de liaisons hydrogène est: {B.nbHydrogen()}"); time.sleep(3)
print("Test 2.2 REUSSI\n\n\n\n----\n\n"); time.sleep(5)




############################################################################
############################################################################

#  3 TEST POUR LA MOLECULE ADN
## 3.1 MOLECULE ADN BIEN DEFINIE

from python.molecule_adn import MoleculeADN
print("\n\n---TEST AVEC UNE MOLECULE ADN BIEN DEFINIE---\n")
molecule = MoleculeADN(5)
print("MOLECULE ADN BIEN DEFINIE par l'utilisateur"); time.sleep(3)

## 3.1.1 Affichage de la séquence ADN
print(f"La représentation complète de la molécule ADN est: {molecule.toString()}"); time.sleep(3)

## 3.1.2 Affichage de la première occurrence d'un pont
print("Affichage de la première occurrence d'un pont dans la molécule ADN..."); time.sleep(3)
exemple_pont = str(input("Entrez un pont X-Y dans la molécule ADN: "))
print(f"La première occurence de {exemple_pont} dans l'ADN est: {molecule.firstOccurence(exemple_pont)}"); time.sleep(3)

## 3.1.3 Affichage d'un fragment
# Note: On demande la position et la longueur qui sont ensuite vérifiées à lintérieur de la méthode
position = int(input("Entrer la position du fragment à afficher: "))
longueur = int(input("Entrer la longueur du fragment à afficher: "))
print(f"La partie du fragment correspondant à la position {position} et de longueur {longueur} est: {molecule.displayFragment(position, longueur)}"); time.sleep(3)

## 3.1.4 Extraction de la séquence ADN
print("Extraction de la séquence ADN correspondant à la position {position} et de longueur {longueur}...\n")
list_pont = molecule.getFragment(position, longueur); time.sleep(3)

## 3.1.5 Affichage du taux de fusion correspondant à une séquence ADN
print(f"Calcul du taux de fusion correspondant un fragment...\n")
print(f"Le taux de fusion correspondant à la séquence ADN est: {molecule.fusionRate()}"); time.sleep(3)
"""