# dsiplib

EARFCN2freq and Haversine calculation functions are implemented in this package.

## Installation

### Installing the Package

To use the `dsiplib` package, install it directly from the GitHub repository using the following command:

```bash
pip install git+https://github.com/joshuaroy873/acms80870_project_palathinkal.git#subdirectory=dsiplib
```

## Example Usage

### Step 1: Create a Script
Create a Python script named `displib_use.py` in your project directory.

### Step 2: Add the Following Code
Add the following code to the `displib_use.py` file:

```python
from dsiplib import haversine, earfcn_to_freq

# Example usage
distance_2d, distance_3d = haversine(52.5200, 13.4050, 48.8566, 2.3522, 50)
print(f"2D Distance: {distance_2d}, 3D Distance: {distance_3d}")

freq = earfcn_to_freq(100)
print(f"Frequency: {freq}")
```

### Running the Script

Run the script using the following command:

```bash
python displib_use.py
```

### Expected Output

When you run the script, you should see output similar to the following:

```plaintext
2D Distance: 877463.3259175433, 3D Distance: 877463.3272579126
Frequency: 2120.0
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`dsiplib` was created by Joshua Roy Palathinkal. It is licensed under the terms of the MIT license.

## Credits

`dsiplib` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
