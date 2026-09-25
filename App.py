#!/usr/bin/env python3
"""Interactive console application for the DNA modeling project."""

from __future__ import annotations

from typing import Optional

from python.molecule_adn import MoleculeADN
from python.nucleotide import Nucleotide
from python.pont_adn import PontADN


class App:
    """Small console interface used to demonstrate the DNA classes."""

    def __init__(self) -> None:
        self.molecule: Optional[MoleculeADN] = None

    def _pause(self, seconds: float = 0.3) -> None:
        """Pause briefly to keep the console output readable."""
        import time

        time.sleep(seconds)

    def run(self) -> None:
        """Run the main application loop."""
        while True:
            print("\n=== DNA Model Menu ===")
            print("1. Test nucleotide")
            print("2. Test DNA bridge")
            print("3. Test DNA molecule")
            print("4. Exit")

            choice = input("Select an option (1-4): ").strip()

            if choice == "1":
                self.menu_nucleotides()
            elif choice == "2":
                self.menu_pont_adn()
            elif choice == "3":
                self.menu_molecule_adn()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

            self._pause()

    def menu_nucleotides(self) -> None:
        """Menu for nucleotide demonstrations."""
        while True:
            print("\n--- Nucleotide Menu ---")
            print("1. Create a nucleotide with an explicit base")
            print("2. Create a random nucleotide")
            print("3. Back")

            choice = input("Select an option (1-3): ").strip()
            if choice == "1":
                base = input("Enter a base (A, T, C, G): ").strip().upper()
                nucleotide = Nucleotide(base)
                print(f"Symbol: {nucleotide.symbol()}")
                print(f"Complement: {nucleotide.complement()}")
                print(f"Display: {nucleotide.to_string()}")
            elif choice == "2":
                nucleotide = Nucleotide()
                print(f"Random symbol: {nucleotide.symbol()}")
                print(f"Complement: {nucleotide.complement()}")
            elif choice == "3":
                return
            else:
                print("Invalid option. Please try again.")

    def menu_pont_adn(self) -> None:
        """Menu for DNA-bridge demonstrations."""
        while True:
            print("\n--- DNA Bridge Menu ---")
            print("1. Build a bridge for a specific base")
            print("2. Build a random bridge")
            print("3. Back")

            choice = input("Select an option (1-3): ").strip()
            if choice == "1":
                base = input("Enter a base (A, T, C, G): ").strip().upper()
                bridge = PontADN(base)
                print(f"Left base: {bridge.symbol_gauche()}")
                print(f"Right base: {bridge.symbol_droite()}")
                print(f"Bridge: {bridge.to_string()}")
                print(f"Hydrogen bonds: {bridge.nb_hydrogen()}")
            elif choice == "2":
                bridge = PontADN()
                print(f"Bridge: {bridge.to_string()}")
                print(f"Hydrogen bonds: {bridge.nb_hydrogen()}")
            elif choice == "3":
                return
            else:
                print("Invalid option. Please try again.")

    def menu_molecule_adn(self) -> None:
        """Menu for DNA molecule demonstrations."""
        while True:
            try:
                length = int(input("\nEnter the number of bridges to generate: ").strip())
                if length <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a positive integer.")

        self.molecule = MoleculeADN(length)
        print(f"Generated molecule with {len(self.molecule)} bridges.")

        while True:
            print("\n--- DNA Molecule Menu ---")
            print("1. Display molecule")
            print("2. Search first occurrence by left base")
            print("3. Display fragment")
            print("4. Search a pattern")
            print("5. Compute fusion rate")
            print("6. Display optimization factor")
            print("7. Back")

            choice = input("Select an option (1-7): ").strip()
            if choice == "1":
                print(self.molecule.to_string())
            elif choice == "2":
                left_base = input("Base to look for (A, T, C, G): ").strip().upper()
                print(self.molecule.first_occurrence(left_base))
            elif choice == "3":
                pos = int(input("Starting index (1-based): ").strip())
                length = int(input("Length: ").strip())
                print(self.molecule.get_fragment(pos, length))
            elif choice == "4":
                pattern = input("Pattern to search: ").strip().upper()
                print(self.molecule.search_pattern(pattern))
            elif choice == "5":
                pos = int(input("Starting index (1-based): ").strip())
                length = int(input("Length: ").strip())
                print(f"Fusion rate: {self.molecule.fusion_rate(pos, length)}")
            elif choice == "6":
                print(f"Optimization factor: {self.molecule.optimization_factor()}")
            elif choice == "7":
                return
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    app = App()
    app.run()

