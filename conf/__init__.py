"""
Settings and configuration for Django.

Read values from the module specified by the DJANGO_SETTINGS_MODULE environment
variable, and then from django.conf.global_settings; see the global_settings.py
for a list of all possible variables.
"""

import importlib
import os
import time
import traceback
import warnings
from pathlib import Path
import django
from django.conf import global_settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.deprecation import RemovedInDjango40Warning
from django.utils.functional import LazyObject,empty


class LazySettings(LazyObject):
    """
        A lazy proxy for either global Django settings or a custom settings object.
        The user can manually configure settings prior to using them. Otherwise,
        Django uses the settings module pointed to by DJANGO_SETTINGS_MODULE.
        """
