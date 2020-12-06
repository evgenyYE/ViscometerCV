import os
from pathlib import Path


def the_local_path() -> str:
    path = str(Path(os.path.dirname(os.path.realpath(__file__))).parent)
    return path


def the_parent_path() -> str:
    path = str(os.path.dirname(os.path.realpath(__file__)))
    return path
