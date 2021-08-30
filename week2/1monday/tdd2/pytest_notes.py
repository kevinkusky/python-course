# *************************************************
# Pytest

# Test must be set up as a directory
#   - CD to directory - __init__.py
#           - pipenv install --python "$PYENV_ROOT/shims/python"
#                   - alias: new_pip
#           - pipenv shell
#                   - Ensure VSC is using correct python (from .venv)
#           - pipenv install --dev pycodestyle
#                   - installs linter to .venv
#           - pipenv install pytest

# Files must begin with test

# Pytest also reads unit tests!!
# pytest also allows for skipping tests globally:
#       import pytest
#           @pytest.mark.skip()
# or conditionally in a test:
#        if True:
#           pytest.skip()
# *************************************************
