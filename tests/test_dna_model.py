from python.molecule_adn import MoleculeADN
from python.nucleotide import Nucleotide
from python.pont_adn import PontADN


def test_nucleotide_complement_and_symbol():
    nucleotide = Nucleotide("A")

    assert nucleotide.symbol() == "A"
    assert nucleotide.complement() == "T"


def test_pont_dna_pair():
    bridge = PontADN("C")

    assert bridge.symbol_gauche() == "C"
    assert bridge.symbol_droite() == "G"
    assert bridge.nb_hydrogen() == 3


def test_molecule_structure_and_memory_optimization():
    molecule = MoleculeADN(4, seed=7)

    assert len(molecule.strands) == 4
    assert all(pont.symbol_gauche() in {"A", "T", "C", "G"} for pont in molecule.strands)
    assert isinstance(molecule.to_string(), str)
    assert molecule.optimization_factor() > 0
