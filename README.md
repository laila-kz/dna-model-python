# DNA Model Project

A modern object-oriented Python project for modeling DNA molecules, nucleotides, and base-pair bridges. The repository demonstrates inheritance, composition, sequence analysis, and light memory optimization techniques in a compact educational codebase.

## Project Overview

This project models the basic building blocks of DNA using Python classes:

- `Nucleotide` represents a single nitrogenous base such as A, T, C, or G.
- `PontADN` models a complementary base pair and tracks the number of hydrogen bonds.
- `MoleculeADN` creates a sequence of bridges and provides operations such as fragment extraction, pattern matching, fusion-rate calculation, and memory-efficiency analysis.

The project is intentionally designed to be easy to understand while reinforcing key OOP principles in Python, including encapsulation, inheritance, and composition.

## Key Features

- Object-oriented modeling of nucleotide bases and DNA bridges.
- Complementary-base logic and hydrogen bond counting.
- DNA molecule sequence operations such as search, extraction, and fragment analysis.
- A lightweight memory optimization example using compact bit-style encoding.
- Clean class hierarchy with reusable base classes and specialized subclasses.
- Console-based interactive application for demonstration.

## Project Architecture

The repository is organized into a small set of focused modules:

- `App.py`: console entry point and interactive menu.
- `python/nucleotide.py`: nucleotide definitions and complement mapping.
- `python/pont_adn.py`: DNA bridge class representing complementary base pairs.
- `python/molecule_adn.py`: DNA molecule logic, search operations, and memory checks.
- `python/__init__.py`: package initialization.

Execution flow:

1. The application starts from `App.py`.
2. The menu instantiates nucleotide, bridge, and molecule examples.
3. `MoleculeADN` manages a list of `PontADN` objects.
4. Each bridge stores two nucleotide instances to represent the left and right DNA strands.
5. Sequence and optimization methods operate on the molecule as a whole.

## Installation and Setup

Clone the project and create a virtual environment:

```bash
git clone <repository-url>
cd dna-model-python
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Run the interactive application:

```bash
python App.py
```

To run the automated tests:

```bash
pytest
```

## Development Notes

This project follows modern Python conventions, including:

- snake_case naming for methods and variables.
- PascalCase naming for classes.
- type hints and explicit docstrings.
- deterministic construction options for testing.
- clean import handling for package execution.

## License

This project is intended for educational and demonstration purposes.
