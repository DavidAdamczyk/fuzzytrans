# FuzzyTrans

**FuzzyTrans** is a Python library for fuzzy set theory inspired transformations, reimplementing the functionality of the [UpperLowerApp](https://github.com/ZahraAlijani/UpperLowerApp) licensed under the MIT License and developed by Zahra Alijani and Martina Daňková. It provides implementations of triangular, Gaussian, and Bell fuzzy sets, along with their transformation components (F_A_up/down) and inverse transformations.

## Installation

You can install FuzzyTrans using pip:

```bash
pip install fuzzytrans
```

Alternatively, for development purposes, you can install it from the source:

```bash
pip install -e '.[dev]'
```

## Usage

FuzzyTrans provides a simple API for working with fuzzy logic functions and transformations. Below is a basic example of how to use the library:

```python
import numpy as np
from fuzzytrans import triangular_fuzzy_number, F_A_upT

# Define parameters for a triangular fuzzy number
a, b, c = 1, 2, 3
x = 1.5

# Calculate membership value
membership = triangular_fuzzy_number(a, b, c, x)
print(f'Membership value at x={x}: {membership}')

# Example of transformation
params = [(1, 2, 3)]
x_values = [1, 1.5, 2, 2.5, 3]
f_values = [0.1, 0.2, 0.3, 0.4, 0.5]
result = F_A_upT(params, x_values, f_values)
print(f'F_A_upT result: {result}')
```

## Examples

For more detailed examples, check out the Jupyter notebooks in the `examples` directory:
- [Fuzzy Logic Transformations Examples](examples/lower_upper_functions_examples.ipynb)
- [Fuzzy Differential Equations](examples/differential_equations.ipynb)

## API Reference

### Core Fuzzy Functions
- `triangular_fuzzy_number(a, b, c, x)`: Calculate membership value for a triangular fuzzy number.
- `gaussian_fuzzy_set(x, sigma, c)`: Calculate membership value for a Gaussian fuzzy set.
- `bell_function(x, a, b, c)`: Calculate membership value for a Bell-shaped fuzzy function.

### Transformations
- `F_A_upT(params, x_values, f_values)`: Calculate F_A^↑ for triangular fuzzy numbers.
- `F_A_downT(params, x_values, f_values)`: Calculate F_A^↓ for triangular fuzzy numbers.
- And more for Gaussian and Bell functions...

## Development

If you want to contribute to FuzzyTrans, clone the repository and install the development dependencies:

```bash
git clone https://github.com/yourusername/fuzzytrans.git
cd fuzzytrans
pip install -e '.[dev]'
```

Run tests and linting:

```bash
pytest
ruff check .
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or issues, please contact David at davidadamczyk@icloud.com or open an issue on GitHub.
