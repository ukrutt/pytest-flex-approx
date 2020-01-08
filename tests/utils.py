"""Test utilities."""

from collections.abc import Mapping

from _pytest.python_api import ApproxMapping
from _pytest.python_api import approx as _pytest_approx


class ApproxMappingFlex(ApproxMapping):
    """More flexible ApproxMapping.

    This one will accept dicts with non-numeric values.
    """

    # pylint: disable=too-few-public-methods
    def _check_type(self):
        # TODO: check if this next variable is in fact necessary.
        __tracebackhide__ = True  # pylint: disable=unused-variable
        for _key, value in self.expected.items():
            if isinstance(value, type(self.expected)):
                # Defer this error check to the original ApproxMapping
                super()._check_type()


def dict_approx(expected, rel=None, absolute=None, nan_ok=False):
    """Approximate for dicts."""
    if isinstance(expected, Mapping):
        return ApproxMappingFlex(expected, rel, absolute, nan_ok)
    return _pytest_approx(expected, rel, absolute, nan_ok)
