# Installation

use poetry to install main, dev or test group dependencies


refer - https://python-poetry.org/docs/master/managing-dependencies/

poetry add pytest --group test
poetry add coverage --group dev

poetry remove pytest --group test

poetry install --only test

poetry install --with test

# Pytest

refer - https://docs.pytest.org/en/6.2.x/reference.html#command-line-flags

pytest --help

Run test command : pytest -rA

-r chars  show extra test summary info as specified by chars:
            (f)ailed, (E)rror, (s)kipped, (x)failed, (X)passed,
            (p)assed, (P)assed with output, (a)ll except passed
            (p/P), or (A)ll. (w)arnings are enabled by default
            (see --disable-warnings), 'N' can be used to reset
            the list. (default: 'fE').

View all fixtures: pytest --fixtures

