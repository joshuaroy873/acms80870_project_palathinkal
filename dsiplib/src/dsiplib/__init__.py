# read version from installed package
from importlib.metadata import version
__version__ = version("dsiplib")

# Import public functions
from .haversine import haversine
from .earfcn_to_freq import earfcn_to_freq

# Define the public API
__all__ = ['haversine', 'earfcn_to_freq']