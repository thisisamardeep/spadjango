import functools
import inspect


@functools.lru_cache(maxsize=512)
def _get_signature(func):
    return inspect.signature(func)


def func_accepts_kwargs(func):
    """Return True if function 'func' accepts keyword arguments **kwargs."""
    return any(
        p for p in _get_signature(func).parameters.values()
        if p.kind == p.VAR_KEYWORD
    )
