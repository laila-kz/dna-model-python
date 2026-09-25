"""DNA bridge representation."""

from __future__ import annotations

import random
from typing import Final

try:
    from .nucleotide import A, C, G, T, COMPLEMENTS, Nucleotide
except ImportError:  # pragma: no cover - support direct script execution
    from python.nucleotide import A, C, G, T, COMPLEMENTS, Nucleotide

NUCLEOTIDE_MAP: Final[dict[str, type[Nucleotide]]] = {"A": A, "T": T, "C": C, "G": G}


class PontADN:
    """Represent a complementary DNA base pair, also called a bridge."""

    __slots__ = ("_base_gauche", "_base_droite")

    def __init__(self, symbol: str | None = None, choice: int | None = None, *, rng: random.Random | None = None) -> None:
        """Create a DNA bridge.

        Args:
            symbol: base on the left side of the bridge.
            choice: retained for backward compatibility; 1 means random, 2 means explicit.
            rng: optional random generator for deterministic behavior.
        """
        if choice is not None and choice not in (1, 2):
            raise ValueError("Choice must be 1 or 2 when provided.")

        generator = rng or random
        if symbol is None:
            symbol = generator.choice(tuple(COMPLEMENTS.keys()))

        normalized = str(symbol).strip().upper()
        if normalized not in COMPLEMENTS:
            raise ValueError("A bridge must use one of: A, T, C, G.")

        self._base_gauche = NUCLEOTIDE_MAP[normalized]()
        self._base_droite = NUCLEOTIDE_MAP[COMPLEMENTS[normalized]]()

    def symbol_gauche(self) -> str:
        """Return the left-side base symbol."""
        return self._base_gauche.symbol()

    def symbol_droite(self) -> str:
        """Return the right-side complementary base symbol."""
        return self._base_droite.symbol()

    def to_string(self) -> str:
        """Return a readable representation like A-T."""
        return f"{self._base_gauche.symbol()}-{self._base_droite.symbol()}"

    def nb_hydrogen(self) -> int:
        """Return the number of hydrogen bonds in the base pair."""
        if self._base_gauche.symbol() in {"A", "T"}:
            return 2
        if self._base_gauche.symbol() in {"C", "G"}:
            return 3
        return 0

    def nbHydrogen(self) -> int:
        """Backward-compatible alias for nb_hydrogen()."""
        return self.nb_hydrogen()

    def toString(self) -> str:
        """Backward-compatible alias for to_string()."""
        return self.to_string()


complements = COMPLEMENTS

