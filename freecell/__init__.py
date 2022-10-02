import os

INPUT_FILE = os.path.expanduser("~/.config/gnome-games/aisleriot")
from .statistics import Statistics
from .data_provider import DataProvider

__all__ = [
    INPUT_FILE,
    'Statistics',
    'DataProvider',
]
