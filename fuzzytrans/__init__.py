"""
FuzzyTrans - Library for fuzzy logic transformations.

This library provides implementations of triangular, Gaussian, and Bell fuzzy
functions, along with their transformations and inverse transformations.
"""

__version__ = "0.1.0"

# Import core fuzzy functions
from .core import (
    bell_function,
    gaussian_fuzzy_set,
    triangular_fuzzy_number,
)

# Import transformation functions
from .transformations import (
    F_A_downB,
    F_A_downG,
    F_A_downT,
    F_A_upB,
    F_A_upG,
    F_A_upT,
    f_A_downB,
    f_A_downG,
    f_A_downT,
    f_A_upB,
    f_A_upG,
    f_A_upT,
)

__author__ = "David"
__description__ = "Library for fuzzy logic transformations"

__all__ = [
    "F_A_downB",
    "F_A_downG",
    "F_A_downT",
    "F_A_upB",
    "F_A_upG",
    "F_A_upT",
    "bell_function",
    "f_A_downB",
    "f_A_downG",
    "f_A_downT",
    "f_A_upB",
    "f_A_upG",
    "f_A_upT",
    "gaussian_fuzzy_set",
    "triangular_fuzzy_number",
]
