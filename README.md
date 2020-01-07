# Test mixed dicts with `pytest.approx()`

Development on a class for testing dicts with pytest.

 - Pytest currently tests dicts, however, for testing with
   `pytest.approx()` it only accepts shallow dicts where all `value`s
   are numbers.

 - We want to accept dicts where there can be a
   combination of numbers and e.g. strings.


## Installation

I like to use pyenv to specify a Python version

    % eval "$(pyenv init -)"
    % python3 --version
    3.7.4
    % python3 -m venv .venv
    % . .venv/bin/activate
    % pip install --upgrade pip
    % pip install .


## Development

    % python3 -m venv .venv
    % . .venv/bin/activate
    % pip install --upgrade pip
    % pip install -r requirements-dev.txt
