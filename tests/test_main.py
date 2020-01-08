"""Sample test file."""

import pytest

from pytest_mix_dict import main


@pytest.mark.xfail(
    raises=AssertionError,
    reason="Because of floating point arithmetic, 0.1 + 0.2 != 0.3",
)
def test_add_two():
    """Sample test routine."""
    arg_x = 0.2
    arg_y = 0.1
    ans_z = main.add_two(arg_x, arg_y)
    assert ans_z == 0.3


def test_add_two_int():
    """Sample test routine."""
    arg_x = 2
    arg_y = 1
    ans_z = main.add_two(arg_x, arg_y)
    assert ans_z == 3
