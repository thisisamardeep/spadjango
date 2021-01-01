
from django.utils.functional import LazyObject


class LazySettings(LazyObject):
    """
        A lazy proxy for either global Django settings or a custom settings object.
        The user can manually configure settings prior to using them. Otherwise,
        Django uses the settings module pointed to by DJANGO_SETTINGS_MODULE.
        """