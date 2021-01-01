import os

from . import Error, Tags, register


E001 = Error(
    'You should not set the DJANGO_ALLOW_ASYNC_UNSAFE environment variable in '
    'deployment. This disables async safety protection.',
    id='async.E001',
)



def check_async_unsafe(app_configs, **kwargs):
    pass