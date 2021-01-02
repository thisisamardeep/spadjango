from itertools import chain
from django.utils.inspect import func_accepts_kwargs


class Tags:
    """
    Built-in tags for internal checks.
    """
    admin = 'admin'
    async_support = 'async_support'
    caches = 'caches'
    compatibility = 'compatibility'
    database = 'database'
    models = 'models'
    security = 'security'
    signals = 'signals'
    sites = 'sites'
    staticfiles = 'staticfiles'
    templates = 'templates'
    translation = 'translation'
    urls = 'urls'


class CheckRegistry:

    def __init__(self):
        self.registered_checks = set()
        self.deployment_checks = set()

    def register(self, check=None, *tags, **kwargs):
        """
                Can be used as a function or a decorator. Register given function
                `f` labeled with given `tags`. The function should receive **kwargs
                and return list of Errors and Warnings.

                Example::

                    registry = CheckRegistry()
                    @registry.register('mytag', 'anothertag')
                    def my_check(app_configs, **kwargs):
                        # ... perform checks and collect `errors` ...
                        return errors
                    # or
                    registry.register(my_check, 'mytag', 'anothertag')
                """

        def inner(check):
            if not func_accepts_kwargs(check):
                raise TypeError(
                    'Check functions must accept keyword arguments (**kwargs).'
                )
            check.tags = tags
            checks = self.deployment_checks if kwargs.get('deploy') else self.registered_checks
            checks.add(check)
            return check

        if callable(check):
            return inner(check)
        else:
            if check:
                tags += (check,)
            return inner


def run_checks(self, app_configs=None, tags=None, include_deployment_checks=False, databases=None):
    pass


def tag_exists(self, tag, include_deployment_checks=False):
    pass


registry = CheckRegistry()
register = registry.register
run_checks = registry.run_checks
tag_exists = registry.tag_exists
