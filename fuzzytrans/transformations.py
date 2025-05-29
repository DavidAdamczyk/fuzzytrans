"""
Fuzzy logic transformation functions for FuzzyTrans library.

Reimplementation of UpperLowerApp fuzzy transformation functions.
"""


import numpy as np

from .core import bell_function, gaussian_fuzzy_set, triangular_fuzzy_number


# Triangular fuzzy transformations
def F_A_upT(
    params: list[tuple[float, float, float]],
    x_values: list[float],
    f_values: list[float],
) -> list[float]:
    """
    Calculate F_A^↑ for triangular fuzzy numbers.

    Args:
        params: List of (a, b, c) parameters for triangular fuzzy numbers
        x_values: List of x values
        f_values: List of f(x) values

    Returns:
        List of F_A^↑ values

    """
    F_A_up = []
    for a, b, c in params:
        products = np.array(
            [
                triangular_fuzzy_number(a, b, c, x) * f_x
                for x, f_x in zip(x_values, f_values, strict=False)
            ]
        )
        F_A_up.append(np.max(products))
    return F_A_up


def F_A_downT(
    params: list[tuple[float, float, float]],
    x_values: list[float],
    f_x_values: list[float],
) -> list[float]:
    """
    Calculate F_A^↓ for triangular fuzzy numbers.

    Args:
        params: List of (a, b, c) parameters for triangular fuzzy numbers
        x_values: List of x values
        f_x_values: List of f(x) values

    Returns:
        List of F_A^↓ values

    """
    F_A_down = []
    for a, b, c in params:
        ratios = np.array(
            [
                (
                    f_x_values[i] / triangular_fuzzy_number(a, b, c, x_values[i])
                    if triangular_fuzzy_number(a, b, c, x_values[i]) > 0
                    else np.inf
                )
                for i in range(len(x_values))
            ]
        )
        F_A_down.append(np.min(ratios))
    return F_A_down


# Gaussian fuzzy transformations
def F_A_upG(
    centers: list[float], sigma: float, x_values: list[float], f_x_values: list[float]
) -> list[float]:
    """
    Calculate F_A^↑ for Gaussian fuzzy sets.

    Args:
        centers: List of centers for Gaussian curves
        sigma: Standard deviation
        x_values: List of x values
        f_x_values: List of f(x) values

    Returns:
        List of F_A^↑ values

    """
    F_A_up = []
    for c in centers:
        products = np.array(
            [
                gaussian_fuzzy_set(x, sigma, c) * f_x
                for x, f_x in zip(x_values, f_x_values, strict=False)
            ]
        )
        F_A_up.append(np.max(products))
    return F_A_up


def F_A_downG(
    centers: list[float], sigma: float, x_values: list[float], f_x_values: list[float]
) -> list[float]:
    """
    Calculate F_A^↓ for Gaussian fuzzy sets.

    Args:
        centers: List of centers for Gaussian curves
        sigma: Standard deviation
        x_values: List of x values
        f_x_values: List of f(x) values

    Returns:
        List of F_A^↓ values

    """
    F_A_down = []
    for c in centers:
        ratios = np.array(
            [
                (
                    f_x_values[i] / gaussian_fuzzy_set(x_values[i], sigma, c)
                    if gaussian_fuzzy_set(x_values[i], sigma, c) > 0
                    else np.inf
                )
                for i in range(len(x_values))
            ]
        )
        F_A_down.append(np.min(ratios))
    return F_A_down


# Bell fuzzy transformations
def F_A_downB(
    centers: list[float],
    a: float,
    b: float,
    x_values: list[float],
    f_x_values: list[float],
) -> list[float]:
    """
    Calculate F_A^↓ for generalized bell functions.

    Args:
        centers: List of centers for bell functions
        a: Width parameter
        b: Shape parameter
        x_values: List of x values
        f_x_values: List of f(x) values

    Returns:
        List of F_A^↓ values

    """
    F_A_down = []
    for c in centers:
        ratios = np.array(
            [
                (
                    f_x / bell_function(x, a, b, c)
                    if bell_function(x, a, b, c) > 0
                    else np.inf
                )
                for x, f_x in zip(x_values, f_x_values, strict=False)
            ]
        )
        F_A_down.append(np.min(ratios))
    return F_A_down


def F_A_upB(
    centers: list[float],
    a: float,
    b: float,
    x_values: list[float],
    f_x_values: list[float],
) -> list[float]:
    """
    Calculate F_A^↑ for generalized bell functions.

    Args:
        centers: List of centers for bell functions
        a: Width parameter
        b: Shape parameter
        x_values: List of x values
        f_x_values: List of f(x) values

    Returns:
        List of F_A^↑ values

    """
    F_A_up = []
    for c in centers:
        products = np.array(
            [bell_function(x, a, b, c) * f_x for x, f_x in zip(x_values, f_x_values, strict=False)]
        )
        F_A_up.append(np.max(products))
    return F_A_up


# Inverse transformations - Triangular
def f_A_downT(
    x: float, F_A_down: list[float], params: list[tuple[float, float, float]]
) -> float:
    """
    Inverse downward transformation for triangular fuzzy numbers.

    Args:
        x: Input value
        F_A_down: List of F_A^↓ values
        params: List of (a, b, c) parameters

    Returns:
        Resulting transformation value

    """
    values = [
        triangular_fuzzy_number(a, b, c, x) * F_A
        for (a, b, c), F_A in zip(params, F_A_down, strict=False)
    ]
    return max(values)


def f_A_upT(
    x: float, F_A_up: list[float], params: list[tuple[float, float, float]]
) -> float:
    """
    Inverse upward transformation for triangular fuzzy numbers.

    Args:
        x: Input value
        F_A_up: List of F_A^↑ values
        params: List of (a, b, c) parameters

    Returns:
        Resulting transformation value

    """
    ratios = [
        (
            F_A / triangular_fuzzy_number(a, b, c, x)
            if triangular_fuzzy_number(a, b, c, x) > 0
            else np.inf
        )
        for (a, b, c), F_A in zip(params, F_A_up, strict=False)
    ]
    return min(ratios)


# Inverse transformations - Bell
def f_A_downB(
    x: float, F_A_down: list[float], centers: list[float], a: float, b: float
) -> float:
    """
    Inverse downward transformation for bell functions.

    Args:
        x: Input value
        F_A_down: List of F_A^↓ values
        centers: List of centers
        a: Width parameter
        b: Shape parameter

    Returns:
        Resulting transformation value

    """
    values = [bell_function(x, a, b, c) * F_A for c, F_A in zip(centers, F_A_down, strict=False)]
    return max(values)


def f_A_upB(
    x: float, F_A_up: list[float], centers: list[float], a: float, b: float
) -> float:
    """
    Inverse upward transformation for bell functions.

    Args:
        x: Input value
        F_A_up: List of F_A^↑ values
        centers: List of centers
        a: Width parameter
        b: Shape parameter

    Returns:
        Resulting transformation value

    """
    ratios = [
        F_A / bell_function(x, a, b, c) if bell_function(x, a, b, c) > 0 else np.inf
        for c, F_A in zip(centers, F_A_up, strict=False)
    ]
    return min(ratios)


# Inverse transformations - Gaussian
def f_A_upG(x: float, F_A_up: list[float], sigma: float, centers: list[float]) -> float:
    """
    Inverse upward transformation for Gaussian fuzzy sets.

    Args:
        x: Input value
        F_A_up: List of F_A^↑ values
        sigma: Standard deviation
        centers: List of centers

    Returns:
        Resulting transformation value

    """
    ratios = [
        (
            F_A / gaussian_fuzzy_set(x, sigma, c)
            if gaussian_fuzzy_set(x, sigma, c) > 0
            else np.inf
        )
        for c, F_A in zip(centers, F_A_up, strict=False)
    ]
    return min(ratios)


def f_A_downG(
    x: float, F_A_down: list[float], sigma: float, centers: list[float]
) -> float:
    """
    Inverse downward transformation for Gaussian fuzzy sets.

    Args:
        x: Input value
        F_A_down: List of F_A^↓ values
        sigma: Standard deviation
        centers: List of centers

    Returns:
        Resulting transformation value

    """
    values = [
        gaussian_fuzzy_set(x, sigma, c) * F_A for c, F_A in zip(centers, F_A_down, strict=False)
    ]
    return max(values)
