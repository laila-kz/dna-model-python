from python.molecule_adn import MoleculeADN
# On importe la classe permettant de gérer la molécule d’ADN. 
# Cette classe est définie dans un autre fichier du projet.

def run():
    """
    Lance l'application et affiche l'exemple d'utilisation de la molécule d'ADN.
    """
    # Création d'une molécule d'ADN avec un nombre de ponts spécifié
    molecule = MoleculeADN(nb=50)
    
    # On affiche un texte en vert et en gras pour indiquer ce qui va suivre, ici le fragment d’ADN de la position 1 à 10
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

if __name__ == "__main__":
    run()