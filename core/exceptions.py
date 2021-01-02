"""
Global Django exception and warning classes.
"""
import operator


class ImproperlyConfigured(Exception):
    """Django is somehow improperly configured"""
    pass