"""Sample test file."""

from pytest_mix_dict import main


def test_add_two():
    """Sample test routine."""
    arg_x = 0.2
    arg_y = 0.1
    ans_z = main.add_two(arg_x, arg_y)
    assert ans_z == 0.3
