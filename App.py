#!/usr/bin/env python
import time
import sys

from python.nucleotide import Nucleotide
from python.pont_adn import PontADN
from python.molecule_adn import MoleculeADN, displayFragment


class App:
    def __init__(self):
        self.molecule = None

    def wait(self, seconds=2):
        """Simulation d'un délai pour rendre l'expérience interactive."""
        time.sleep(seconds)

    def run(self):
        """Boucle principale de l'application."""
        while True:
            print("\n===== Menu Principal =====")
            print("1. Tester les Nucléotides")
            print("2. Tester les Ponts d'ADN")
            print("3. Tester la Molécule d'ADN")
            print("4. Quitter l'application")
            choice = input("Choisissez une option (1-4): ").strip()
            if choice == "1":
                self.menu_nucleotides()
            elif choice == "2":
                self.menu_pont_adn()
            elif choice == "3":
                self.menu_molecule_adn()
            elif choice == "4":
                print("Au revoir !")
                break
            else:
                print("Option invalide. Veuillez réessayer.")
            self.wait()

    # ---------------------------------------------------------------------------
    # Menu pour les tests de Nucléotides
    # ---------------------------------------------------------------------------
    def menu_nucleotides(self):
        while True:
            print("\n--- Menu Nucléotides ---")
            print("1. Test de Nucleotide avec base bien définie ('A')")
            print("2. Test de Nucleotide avec base inconnue (saisie interactive)")
            print("3. Retour au menu principal")
            choice = input("Choisissez une option (1-3): ").strip()
            if choice == "1":
                self.test_nucleotide_defined()
            elif choice == "2":
                self.test_nucleotide_unknown()
            elif choice == "3":
                break
            else:
                print("Option invalide. Veuillez réessayer.")
            self.wait()

    def test_nucleotide_defined(self):
        print("\nCréation d'un nucléotide avec la base 'A'...")
        nuc = Nucleotide("A")
        self.wait(2)
        print(f"La base définie est : {nuc.symbol()}")
        self.wait(2)
        print(f"La base complémentaire est : {nuc.getComplementaire()}")
        self.wait(2)
        print(f"Représentation complète : {nuc.toString()}")

    def test_nucleotide_unknown(self):
        print("\nCréation d'un nucléotide sans paramètre (choix interactif ou aléatoire)...")
        nuc = Nucleotide()
        self.wait(2)
        print(f"La base obtenue est : {nuc.symbol()}")
        self.wait(2)
        print(f"La base complémentaire est : {nuc.getComplementaire()}")
        self.wait(2)
        print(f"Représentation complète : {nuc.toString()}")

    # ---------------------------------------------------------------------------
    # Menu pour les tests de PontADN
    # ---------------------------------------------------------------------------
    def menu_pont_adn(self):
        while True:
            print("\n--- Menu Pont d'ADN ---")
            print("1. Test avec un pont bien défini (base 'A')")
            print("2. Test avec un pont inconnu (choix aléatoire)")
            print("3. Retour au menu principal")
            choice = input("Choisissez une option (1-3): ").strip()
            if choice == "1":
                self.test_pont_defined()
            elif choice == "2":
                self.test_pont_unknown()
            elif choice == "3":
                break
            else:
                print("Option invalide. Veuillez réessayer.")
            self.wait()

    def test_pont_defined(self):
        print("\nCréation d'un pont d'ADN avec la base 'A' (option 2 pour base définie)...")
        pont = PontADN("A", 2)
        self.wait(2)
        print(f"Base gauche : {pont.symbol_gauche()}")
        self.wait(2)
        print(f"Base droite : {pont.symbol_droite()}")
        self.wait(2)
        print(f"Représentation du pont : {pont.toString()}")
        self.wait(2)
        print(f"Nombre de liaisons hydrogène : {pont.nbHydrogen()}")

    def test_pont_unknown(self):
        print("\nCréation d'un pont d'ADN sans paramètre (choix aléatoire)...")
        pont = PontADN()
        self.wait(2)
        print(f"Base gauche : {pont.symbol_gauche()}")
        self.wait(2)
        print(f"Base droite : {pont.symbol_droite()}")
        self.wait(2)
        print(f"Représentation du pont : {pont.toString()}")
        self.wait(2)
        print(f"Nombre de liaisons hydrogène : {pont.nbHydrogen()}")

    # ---------------------------------------------------------------------------
    # Menu pour les tests de MoleculeADN
    # ---------------------------------------------------------------------------
    def menu_molecule_adn(self):
        # Création d'une nouvelle molécule d'ADN
        while True:
            try:
                nb = int(input("\nEntrez le nombre de ponts pour la molécule d'ADN: "))
                if nb <= 0:
                    print("Le nombre de ponts doit être supérieur à 0.")
                    continue
                break
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")
        print("\nCréation de la molécule d'ADN...")
        self.molecule = MoleculeADN(nb)
        self.wait(2)

        # Sous-menu pour les fonctionnalités de la molécule d'ADN
        while True:
            print("\n--- Menu Molécule d'ADN ---")
            print("1. Afficher la représentation complète de la molécule")
            print("2. Rechercher la première occurrence d'un pont par base (base gauche)")
            print("3. Extraire et afficher un fragment de la molécule")
            print("4. Rechercher un motif dans la molécule")
            print("5. Calculer le taux de fusion d'un fragment")
            print("6. Afficher le facteur d'optimisation mémoire")
            print("7. Retour au menu principal")
            choice = input("Choisissez une option (1-7): ").strip()
            if choice == "1":
                self.display_full_molecule()
            elif choice == "2":
                self.search_first_occurrence()
            elif choice == "3":
                self.extract_and_display_fragment()
            elif choice == "4":
                self.search_pattern()
            elif choice == "5":
                self.calculate_fusion_rate()
            elif choice == "6":
                self.display_optimization_factor()
            elif choice == "7":
                break
            else:
                print("Option invalide. Veuillez réessayer.")
            self.wait()

    def display_full_molecule(self):
        print("\nReprésentation complète de la molécule d'ADN:")
        fragment = self.molecule.getFragment()
        print(fragment)

    def search_first_occurrence(self):
        char = input("\nEntrez le caractère (A, T, C, G) pour rechercher la première occurrence d'un pont: ").strip()
        self.molecule.firstOccurence(char)

    def extract_and_display_fragment(self):
        try:
            pos = int(input("\nEntrez la position du début du fragment à extraire (>= 1): "))
            leng = int(input("Entrez la longueur du fragment à extraire: "))
        except ValueError:
            print("Entrée invalide. Veuillez entrer des valeurs numériques.")
            return
        fragment = self.molecule.getFragment(pos, leng)
        print("\nFragment extrait:")
        print(fragment)
        choice = input("\nSouhaitez-vous l'afficher graphiquement ? (1. Oui / 2. Non): ").strip()
        if choice == "1":
            displayFragment(liste=fragment)

    def search_pattern(self):
        pattern = input("\nEntrez le motif à rechercher (ex: 'aTa', 'Tgc', etc.): ").strip()
        self.molecule.searchPattern(pattern)

    def calculate_fusion_rate(self):
        try:
            pos = int(input("\nEntrez la position de départ pour le calcul du taux de fusion (>= 1): "))
            leng = int(input("Entrez la longueur du fragment: "))
        except ValueError:
            print("Entrée invalide. Veuillez entrer des valeurs numériques.")
            return
        rate = self.molecule.fusionRate(pos, leng)
        print(f"\nLe taux de fusion pour le fragment est : {rate}")

    def display_optimization_factor(self):
        print("\nCalcul du facteur d'optimisation mémoire...")
        factor = self.molecule.optimizationFactor()
        print(f"Le facteur d'optimisation est de : {factor}")


if __name__ == '__main__':
    app = App()
    app.run()
