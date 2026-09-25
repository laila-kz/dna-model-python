"""DNA nucleotide models."""

from __future__ import annotations

import random
from typing import Final

VALID_BASES: Final[tuple[str, ...]] = ("A", "T", "C", "G")
COMPLEMENTS: Final[dict[str, str]] = {"A": "T", "T": "A", "C": "G", "G": "C"}


class Nucleotide:
    """Represent a single DNA base and its complementary base."""

    __slots__ = ("_symbol", "_complement")

    def __init__(self, symbol: str | None = None, *, rng: random.Random | None = None) -> None:
        """Create a nucleotide.

        Args:
            symbol: One of A, T, C, or G. When omitted, a base is chosen randomly.
            rng: Optional random generator for deterministic tests.
        """
        if symbol is None:
            randomizer = rng or random
            symbol = randomizer.choice(VALID_BASES)

        normalized = str(symbol).strip().upper()
        if normalized not in VALID_BASES:
            raise ValueError("Nucleotide must be one of: A, T, C, G.")

        self._symbol = normalized
        self._complement = COMPLEMENTS[normalized]

    def symbol(self) -> str:
        """Return the nucleotide symbol."""
        return self._symbol

    def complement(self) -> str:
        """Return the complementary base."""
        return self._complement

    def getComplementaire(self) -> str:
        """Backward-compatible alias for complement()."""
        return self.complement()

    def to_string(self) -> str:
        """Return a human-readable representation of the nucleotide."""
        return f"P-D-{self._symbol}"

    def __str__(self) -> str:
        return self.to_string()


class A(Nucleotide):
    """Adenine nucleotide."""

    def __init__(self) -> None:
        super().__init__("A")


class T(Nucleotide):
    """Thymine nucleotide."""

    def __init__(self) -> None:
        super().__init__("T")


class C(Nucleotide):
    """Cytosine nucleotide."""

    def __init__(self) -> None:
        super().__init__("C")


class G(Nucleotide):
    """Guanine nucleotide."""

    def __init__(self) -> None:
        super().__init__("G")


def generate_random_nucleotide(rng: random.Random | None = None) -> Nucleotide:
    """Generate a random nucleotide instance from the supported DNA bases."""
    randomizer = rng or random
    base = randomizer.choice(VALID_BASES)
    return {"A": A(), "T": T(), "C": C(), "G": G()}[base]


complements = COMPLEMENTS
