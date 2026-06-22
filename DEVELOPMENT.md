# Development Guide

This guide provides instructions for setting up a development environment for the Network Intrusion Detection System.

## Prerequisites

- Python 3.7 or higher
- Git
- pip (Python package manager)
- Virtual environment (venv, virtualenv, or conda)

## Setting Up Development Environment

### 1. Clone the Repository

```bash
git clone https://github.com/syednawazali01/NIDS.git
cd NIDS
```

### 2. Create Virtual Environment

```bash
# Using venv (built-in)
python -m venv .venv

# Or using conda
conda create -n nids python=3.10
```

### 3. Activate Virtual Environment

**Windows (PowerShell)**:
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD)**:
```cmd
.venv\Scripts\activate.bat
```

**Linux/Mac**:
```bash
source .venv/bin/activate
```

### 4. Install Development Dependencies

```bash
# Install base dependencies
pip install -r requirements.txt

# Install development tools
pip install -e ".[dev]"
```

Or install all optional dependencies:
```bash
pip install -e ".[dev,packet-sniffing]"
```

## Development Tools

### Code Formatting

Use `black` for consistent code formatting:

```bash
# Format all Python files
black .

# Format specific file
black app.py
```

### Linting

Use `flake8` to check code style:

```bash
# Check all files
flake8 .

# Check specific file
flake8 app.py
```

Use `pylint` for detailed code analysis:

```bash
# Analyze all Python files
pylint app.py train_model.py test_models.py

# Analyze specific file
pylint app.py
```

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_models.py
```

### Security Analysis

```bash
# Check for security vulnerabilities
bandit -r . -ll

# Check for outdated dependencies
pip-audit
```

## Code Style Guide

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use meaningful variable and function names
- Add docstrings to functions and classes

### Docstring Format

Use Google-style docstrings:

```python
def example_function(arg1: str, arg2: int) -> bool:
    """Brief description of the function.
    
    Longer description if needed, explaining the function in more detail.
    
    Args:
        arg1: Description of arg1
        arg2: Description of arg2
    
    Returns:
        Description of the return value
    
    Raises:
        ValueError: Description of when this is raised
    
    Example:
        >>> result = example_function("test", 42)
        >>> print(result)
        True
    """
    pass
```

### Comments

- Use clear, concise comments
- Avoid obvious comments
- Explain the "why", not just the "what"

```python
# Good comment
# Skip zero values to avoid division by zero
if denominator != 0:
    result = numerator / denominator

# Avoid obvious comments
# Increment i
i += 1
```

## File Structure

```
NIDS/
├── app.py                    # Main Streamlit application
├── train_model.py            # Model training script
├── test_models.py            # Model testing script
├── requirements.txt          # Python dependencies
├── pyproject.toml            # Project metadata and config
├── setup.cfg                 # Package configuration
├── CHANGELOG.md              # Version history
├── CONTRIBUTING.md           # Contribution guidelines
├── CODE_OF_CONDUCT.md        # Community guidelines
├── DEVELOPMENT.md            # This file
├── LICENSE                   # MIT License
├── README.md                 # Project documentation
├── SECURITY.md               # Security policy
├── .gitignore                # Git ignore patterns
├── .gitattributes            # Git attributes
├── .editorconfig             # Editor configuration
├── .github/                  # GitHub configuration
│   ├── workflows/            # CI/CD workflows
│   │   └── tests.yml         # Test automation
│   ├── ISSUE_TEMPLATE/       # Issue templates
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── question.md
│   ├── pull_request_template.md
│   └── FUNDING.yml           # Sponsorship options
├── data/                     # Dataset directory
│   ├── KDDTrain+.txt         # Training data
│   └── KDDTest+.txt          # Test data
└── models/                   # Trained models directory
    ├── best_model.joblib
    ├── encoders.joblib
    ├── scaler.joblib
    └── feature_names.joblib
```

## Making Changes

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

- Write clean, documented code
- Follow the code style guide
- Test your changes thoroughly

### 3. Format and Lint

```bash
# Format code
black .

# Check for style issues
flake8 .

# Run static analysis
pylint app.py train_model.py test_models.py
```

### 4. Commit Your Changes

```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "Add feature: description of changes"
```

Use clear, descriptive commit messages:
- Use present tense ("Add feature" not "Added feature")
- Be specific ("Add user authentication" not "Update code")
- Mention related issues (if any): "Fixes #123"

### 5. Push and Create Pull Request

```bash
# Push to your fork
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- Clear title and description
- Reference to related issues
- List of changes made
- Testing information

## Running the Application

### Development Mode

```bash
# Run with auto-reload
streamlit run app.py --logger.level=debug
```

### Training Models

```bash
# Train all models
python train_model.py
```

### Testing Models

```bash
# Run tests
python test_models.py
```

## Troubleshooting

### Virtual Environment Not Activating

```bash
# Check which Python is active
which python

# Verify virtual environment
ls -la .venv/bin/python
```

### Module Import Errors

```bash
# Verify installation
pip list

# Reinstall requirements
pip install --force-reinstall -r requirements.txt
```

### Port Already in Use

```bash
# Run on different port
streamlit run app.py --server.port 8502
```

## Performance Profiling

```bash
# Profile script execution
python -m cProfile -s cumulative train_model.py | head -20
```

## Debugging

### Using pdb (Python Debugger)

```python
import pdb; pdb.set_trace()  # Set breakpoint
```

### Using print debugging

```python
import sys
print("Debug:", variable, file=sys.stderr)  # Print to stderr
```

### Using logging

```python
import logging
logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
```

## Documentation

When adding new features:

1. Update relevant docstrings
2. Update README.md if adding new user-facing features
3. Update CHANGELOG.md
4. Update this DEVELOPMENT.md if process changes

## Questions?

- Review existing code comments
- Check the [CONTRIBUTING.md](CONTRIBUTING.md) guide
- Open a GitHub issue or discussion
- Contact the maintainers

---

Happy coding! 🚀
