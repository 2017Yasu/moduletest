"""モジュール練習05
"""

from ._module05 import hello as hello05
from .module06 import hello as hello06

__all__ = ["hello05", "hello06"]

hello05("__init__.py")
hello06("__init__.py")
