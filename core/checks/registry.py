from itertools import chain


class Tags:
    pass


class CheckRegistry:

    def __init__(self):
        self.registered_checks = set()
        self.deployment_checks = set()

    def register(self, check=None, *tags, **kwargs):
        pass

    def run_checks(self, app_configs=None, tags=None, include_deployment_checks=False, databases=None):
        pass

    def tag_exists(self, tag, include_deployment_checks=False):
        pass


registry = CheckRegistry()
register = registry.register
run_checks = registry.run_checks
tag_exists = registry.tag_exists
