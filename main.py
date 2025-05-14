import time
import random
from python.molecule_adn import MoleculeADN
# On importe la classe permettant de gérer la molécule d’ADN. 
# Cette classe est définie dans un autre fichier du projet.

appreciations = [
    "Continuez, vous progressez !",
    "Ne lâchez rien, vous êtes sur la bonne voie !",
    "Chaque pas compte, bravo pour vos efforts !",
    "Vous faites un excellent travail, continuez ainsi !",
    "Courage, le succès est à portée de main !"
]

def run():
    print("""
          =============================
          Lancement de l'application...
          =============================
          """)
    # Création d'une molécule d'ADN avec un nombre de ponts spécifié
    time.sleep(5)
    
    print("Bienvenue dans Lilliw's DNA, où vous pouvez créer et manipuler un ADN à votre guise !")
    time.sleep(10)
    print("Par quoi souhaiteriez vous commencer ?\n")
    while True:
        choice1 = int(input('Menu : \n\n [1]Je souhaite modéliser un nucléotide\n[2]Les relations entre nucléotides me conviendraient\n[3]Passons directement à l\'ADN\n[4]Quitter==>Votre choix: '))
        if not choice1:
            raise ValueError("Veuillez faire un choix svp :")
        
        # A partir de Python3.10 (celui de notre environnement est 3.12), il y a la boucle switch
        match choice1:
            case 1:
                pass # A remplacer par les méthodes disponibles ; en python, il n'y a pas de break à la fin
            case 2:
                pass
            case 3:
                print(f"Molecule ADN :\n{random.choice(appreciations)}, nous allons commencer la modélisation de la molécule d'ADN de \"50\" ponts")
                molecule = MoleculeADN(nb=50)
                #Ensuite, tu mets un boucle pour les fonctions relatives à MoleculeADN ici, ex:
                print("[bold green]Fragment de la molécule (positions 1 à 10):[/bold green]")
                print(molecule.getFragment(1, 10))
            case 4:
                print("Merci... [A modifier selon tes préférences]")
                break

    """
    # Exemples de fonctions à mettre:
    print("[bold green]Fragment de la molécule (positions 1 à 10):[/bold green]")
    print(molecule.getFragment(1, 10))
    
    print("\n[bold green]Recherche du motif 'aaa' (sera converti en majuscules):[/bold green]")
    res = molecule.searchPattern("aaa")
    print(res)
    
    print("\n[bold green]Affichage d'un fragment de la molécule (positions 1 à 5):[/bold green]")
    molecule.displayFragment(1, 5)
    
    print("\n[bold green]Calcul du taux de fusion (positions 1 à 10):[/bold green]")
    print(molecule.fusionRate(1, 10))
    
    print("\n[bold green]--- Optimisation Mémoire ---[/bold green]")
    compact_ba = molecule.compactRepresentation()
    print("Représentation compacte (bitarray):", compact_ba)
    raw_size = molecule.rawSize()
    opt_size = molecule.optimizedSize()
    print(f"Taille brute approximative: {raw_size} octets")
    print(f"Taille optimisée (bitarray): {opt_size} octets")
    factor = molecule.optimizationFactor()
    print(f"Facteur d'optimisation: {factor:.2f} (objectif: 1/8 ou mieux)")
    """
    
    
if __name__ == "__main__":
    run()