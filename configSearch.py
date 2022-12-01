import argparse
import Enum
import os


__author__ = "Dennis Biber <decibelsTechnology>"

_CONFIG_TEMPLATE = "{0}_particleManipulation.{1}"
_ROOT_PATH = os.getcwd()
_CONFIG_DIR_PATH = f"{_ROOT_PATH}/data/configs"

class ConfigTypes(Enum):
    "_config.py": 1
    "_report.py": 2
    "_test.py": 3
    "_analytic.py": 4
    "_sqlConfig.py": 5
    "_fluidPlan.py": 6


def main():
    poop = 1

if __name__ == "__main__":
    main()