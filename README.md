# Flexible approx for pytest

Development on a class for testing dicts with pytest.

 - `pytest.approx` currently accepts only shallow dicts where all
   `value`s are numbers.

 - This approx also accepts dicts that have a combination of numbers
   and e.g. strings.


## Installation

I like to use pyenv to specify a Python version

    % eval "$(pyenv init -)"
    % python3 --version
    3.8.1
    % python3 -m venv .venv
    % . .venv/bin/activate
    % pip install --upgrade pip
    % pip install .


## Development

    % python3 -m venv .venv
    % . .venv/bin/activate
    % pip install --upgrade pip
    % pip install -r requirements-dev.txt
