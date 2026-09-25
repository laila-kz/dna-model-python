"""DNA molecule model with sequence operations and memory optimization checks."""

from __future__ import annotations

import math
import random
import sys
from typing import Iterable

try:
    from .pont_adn import PontADN
    from .nucleotide import COMPLEMENTS
except ImportError:  # pragma: no cover - support direct execution
    from python.pont_adn import PontADN
    from python.nucleotide import COMPLEMENTS


class MoleculeADN:
    """Represent a DNA molecule as a sequence of complementary base bridges."""

    __slots__ = ("nb", "brin", "_rng")

    def __init__(self, nb: int = 50, *, rng: random.Random | None = None, seed: int | None = None) -> None:
        """Create a molecule composed of a sequence of bridges.

        Args:
            nb: number of bridges in the strand.
            rng: optional random generator.
            seed: seed for deterministic generation.
        """
        if nb <= 0:
            raise ValueError("The number of DNA bridges must be greater than zero.")

        self._rng = rng or random.Random(seed)
        self.nb = nb
        self.brin = [PontADN(rng=self._rng) for _ in range(nb)]

    @property
    def strands(self) -> list[PontADN]:
        """Return the bridges composing the molecule."""
        return self.brin

    def __len__(self) -> int:
        return len(self.brin)

    def __iter__(self) -> Iterable[PontADN]:
        return iter(self.brin)

    def to_string(self) -> str:
        """Return the full strand as a newline-separated sequence of bridge strings."""
        return "\n".join(pont.to_string() for pont in self.brin)

    def get_fragment(self, pos: int = 1, leng: int = 10) -> str:
        """Extract a fragment delimited by 1-based positions."""
        if pos < 1 or leng <= 0:
            raise ValueError("Position must be >= 1 and length must be > 0.")

        start_index = pos - 1
        end_index = min(len(self.brin), start_index + leng)
        return "\n".join(self.brin[i].to_string() for i in range(start_index, end_index))

    def first_occurrence(self, base: str) -> str:
        """Find the first bridge whose left base matches the provided base."""
        normalized = str(base).strip().upper()
        if normalized not in COMPLEMENTS:
            raise ValueError("Base must be one of A, T, C, or G.")

        for index, bridge in enumerate(self.brin, start=1):
            if bridge.symbol_gauche() == normalized:
                return f"Bridge {normalized} found at position {index}."

        return f"Bridge {normalized} not found in the molecule."

    def display_fragment(self, pos: int = 1, leng: int = 10) -> None:
        """Display a sequence of bridge symbols in a simple ASCII style."""
        fragment = self.get_fragment(pos, leng)
        for item in fragment.splitlines():
            left_base = item.split("-")[0]
            right_base = item.split("-")[1]
            connector = "=" if left_base in {"A", "T"} else "≡"
            print("P       P")
            print(" \\     /")
            print(f"  D{left_base}{connector}{right_base}D")
            print(" /     \\")
        print("P       P")

    def fusion_rate(self, pos: int = 1, leng: int = 10) -> float:
        """Return the fusion ratio of A/T versus C/G in a fragment."""
        if pos < 1 or leng <= 0:
            raise ValueError("Position must be >= 1 and length must be > 0.")

        start_index = pos - 1
        end_index = min(len(self.brin), start_index + leng)
        at_count = 0
        cg_count = 0

        for bridge in self.brin[start_index:end_index]:
            if bridge.symbol_gauche() in {"A", "T"}:
                at_count += 1
            else:
                cg_count += 1

        if cg_count == 0:
            return math.inf
        return at_count / cg_count

    def search_pattern(self, pattern: str) -> str:
        """Search for a DNA motif in the molecule's primary strand or its complement."""
        normalized = str(pattern).strip().upper()
        if not normalized or any(base not in COMPLEMENTS for base in normalized):
            raise ValueError("Pattern must contain only A, T, C, or G.")

        strand = "".join(bridge.symbol_gauche() for bridge in self.brin)
        complement = "".join(COMPLEMENTS[base] for base in strand)

        if len(normalized) == len(strand):
            if strand == normalized or complement == normalized:
                return "The entire molecule matches the pattern."
            return "The full molecule does not match the pattern."

        for index in range(len(strand) - len(normalized) + 1):
            window = strand[index : index + len(normalized)]
            complement_window = complement[index : index + len(normalized)]
            if window == normalized or complement_window == normalized:
                return f"Pattern found at position {index + 1}."

        return "Pattern not found."

    def compact_representation(self) -> str:
        """Pack the left-side bases using a 2-bit encoding scheme."""
        mapping = {"A": "00", "T": "01", "C": "10", "G": "11"}
        bits = "".join(mapping[bridge.symbol_gauche()] for bridge in self.brin)
        return bits

    def raw_size(self) -> int:
        """Estimate the memory footprint of the naïve object representation."""
        total = sys.getsizeof(self.brin)
        for bridge in self.brin:
            total += sys.getsizeof(bridge)
            total += sys.getsizeof(bridge._base_gauche)
            total += sys.getsizeof(bridge._base_droite)
        return total

    def optimized_size(self) -> int:
        """Estimate the footprint of the compact representation."""
        compact = self.compact_representation()
        return sys.getsizeof(compact)

    def optimization_factor(self) -> float:
        """Return the memory optimization factor versus the naïve representation."""
        raw = self.raw_size()
        optimized = self.optimized_size()
        if optimized == 0:
            return 0.0
        return round(raw / optimized, 3)

    def getFragment(self, pos: int = 1, leng: int = 10) -> str:
        """Backward-compatible alias for get_fragment()."""
        return self.get_fragment(pos, leng)

    def firstOccurence(self, base: str) -> str:
        """Backward-compatible alias for first_occurrence()."""
        return self.first_occurrence(base)

    def displayFragment(self, pos: int = 1, leng: int = 10) -> None:
        """Backward-compatible alias for display_fragment()."""
        self.display_fragment(pos, leng)

    def fusionRate(self, pos: int = 1, leng: int = 10) -> float:
        """Backward-compatible alias for fusion_rate()."""
        return self.fusion_rate(pos, leng)

    def searchPattern(self, pattern: str) -> str:
        """Backward-compatible alias for search_pattern()."""
        return self.search_pattern(pattern)

    def compactRepresentation(self) -> str:
        """Backward-compatible alias for compact_representation()."""
        return self.compact_representation()

    def rawSize(self) -> int:
        """Backward-compatible alias for raw_size()."""
        return self.raw_size()

    def optimizedSize(self) -> int:
        """Backward-compatible alias for optimized_size()."""
        return self.optimized_size()

    def optimizationFactor(self) -> float:
        """Backward-compatible alias for optimization_factor()."""
        return self.optimization_factor()

    def __str__(self) -> str:
        return self.to_string()


def displayFragment(liste: list[str] | str | None = None) -> None:
    """Display a DNA fragment in a simple graphical format."""
    if liste is None:
        return

    if isinstance(liste, str):
        rows = [line for line in liste.splitlines() if line.strip()]
    else:
        rows = [str(item) for item in liste]

    for item in rows:
        left_base = item.split("-")[0]
        right_base = item.split("-")[1]
        connector = "=" if left_base in {"A", "T"} else "≡"
        print("P       P")
        print(" \\     /")
        print(f"  D{left_base}{connector}{right_base}D")
        print(" /     \\")
    print("P       P")

