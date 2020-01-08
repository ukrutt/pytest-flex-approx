"""Program stub."""

from pytest import approx as pytest_approx

from . import flex_approx


def add_two(arg_x, arg_y):
    """Add arguments.  Return result."""
    return arg_x + arg_y


def hello_world():
    """Say hello to the world"""
    arg_x = arg_y = 3
    print(
        f"Hello World, we've determined that "
        f"{arg_x} + {arg_y} = {add_two(arg_x, arg_y)}"
    )
    main()


def main():
    """Do some informal tests."""
    num_a = 0.1
    num_b = 0.2
    num_c = 0.3
    print(
        f"We know that {num_a} + {num_b} == {num_c} "
        f"is {num_a + num_b == num_c} due to numerics"
    )
    print(
        f"But {num_a} + {num_b} == {pytest_approx(num_c)} "
        f"is {num_a + num_b == pytest_approx(num_c)}"
    )
    act_c = {"c": num_a + num_b}
    exp_c = {"c": num_c}
    print(
        f"We know that {act_c} == {exp_c} "
        f"is {act_c == exp_c} due to numerics"
    )
    print(
        f"But {act_c} == {pytest_approx(exp_c)} "
        f"is {act_c == pytest_approx(exp_c)}"
    )
    act_cm = {"c": num_a + num_b, "d": "d"}
    exp_cm = {"c": num_c, "d": "d"}
    print(
        f"Unfortunately, {act_cm} == pytest.approx({exp_cm}) fails"
    )
    assert act_cm == flex_approx(exp_cm)
    print(
        f"but, {act_cm} == flex_approx({exp_cm}) "
        f"is {act_cm == flex_approx(exp_cm)}"
    )
