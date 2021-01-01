import functools
import os
import pkgutil
import sys
from argparse import (
    _AppendConstAction, _CountAction, _StoreConstAction, _SubParsersAction,
)

from collections import defaultdict
from difflib import get_close_matches
from importlib import import_module

import django
from django.apps import apps
# from django.conf import settings



class ManagementUtility:
    pass

def execute_from_command_line(argv=None):
    """Run a ManagementUtility."""
    utility = ManagementUtility(argv)
    utility.execute()

