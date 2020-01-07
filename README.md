# Project template for Python projects

Folder structure, setup file, CI integration, etc. for a generic Python project

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
