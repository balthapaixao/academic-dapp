from contextlib import contextmanager
# from dataclasses import dataclass
# from typing import List

import brownie
from brownie.project import *


@contextmanager
def get_project():
    if not brownie.network.is_connected():
        try:
            brownie.network.connect('development')
        except:
            raise

    if not brownie.project.get_loaded_projects():
        try:
            yield myproject
            print(f"myproject is already loaded {myproject}")
        except:
            myproject=brownie.project.load('.')
            yield myproject
            print(f"myproject is loaded {myproject}")

    else:
        try:
            yield brownie.project.get_loaded_projects()[0]
            print(f"myproject is already loaded {brownie.project.get_loaded_projects()[0]}")
        except:
            raise