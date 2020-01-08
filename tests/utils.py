"""Test utilities."""

from collections.abc import Mapping

from _pytest.python_api import ApproxMapping

# from _pytest.python_api import approx as _pytest_approx


class ApproxMappingFlex(  # pylint: disable=too-few-public-methods
    ApproxMapping
):
    """More flexible ApproxMapping.

    This one will accept dicts with non-numeric values.
    """


def dict_approx(expected, rel=None, absolute=None, nan_ok=False):
    """Approximate for dicts."""
    if not isinstance(expected, Mapping):
        raise TypeError(
            "Can only use this method for a dict or another mapping"
        )
    return ApproxMappingFlex(expected, rel, absolute, nan_ok)
