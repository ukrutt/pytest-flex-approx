"""Program stub."""


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
