import os
from os.path import dirname

PROJECT_ROOT = dirname(dirname(os.path.dirname(__file__)))


class InvokeError(Exception):
    pass
