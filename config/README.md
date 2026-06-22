# Configuration Files

This directory contains all project configuration files.

## Configuration Files

- **pyproject.toml** - Modern Python project metadata
- **setup.cfg** - Package configuration & tool settings
- **setup.py** - Installation script
- **tox.ini** - Multi-version testing configuration
- **.editorconfig** - Editor consistency settings
- **.pre-commit-config.yaml** - Git pre-commit hooks
- **Makefile** - Convenient development commands

## Usage

### Install Dependencies
```bash
pip install -r ../requirements.txt
```

### Format & Lint Code
```bash
make format    # Format with black
make lint      # Check with flake8
```

### Run Tests
```bash
pytest
tox            # Test multiple Python versions
```

## Key Configurations

### pyproject.toml
- Project metadata (name, version, author)
- Dependencies specification
- Tool configurations (black, isort, mypy)
- Entry points

### Makefile
Quick commands for common tasks:
- `make install` - Install dependencies
- `make run` - Run application
- `make train` - Train models
- `make clean` - Remove cache files

### .editorconfig
Ensures consistent coding style across:
- Python files (4-space indentation)
- YAML files (2-space indentation)
- Markdown files
- JSON files

See the individual files for detailed configuration options.
