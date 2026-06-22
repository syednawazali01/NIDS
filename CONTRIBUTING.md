# Contributing to Network Intrusion Detection System

Thank you for your interest in contributing to the NIDS project! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please be respectful and constructive in all interactions with other contributors and maintainers.

## How to Contribute

### Reporting Bugs

When reporting a bug, please include:

1. **Clear description** of the issue
2. **Steps to reproduce** the problem
3. **Expected behavior** vs. actual behavior
4. **Environment details**:
   - Operating System
   - Python version
   - Python packages versions (run `pip list`)
5. **Error messages or logs** if applicable
6. **Screenshots** (if relevant)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please include:

1. **Clear description** of the proposed feature
2. **Use case** - why this enhancement would be useful
3. **Possible implementation** approaches (if you have ideas)
4. **Alternative solutions** you considered

### Pull Requests

We love pull requests! Here's the process:

1. **Fork the repository**
   ```bash
   # Click the "Fork" button on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/syednawazali01/NIDS.git
   cd NIDS
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

4. **Make your changes**
   - Keep commits atomic and well-documented
   - Follow PEP 8 style guide
   - Add comments for complex logic
   - Test your changes thoroughly

5. **Install development dependencies** (if needed)
   ```bash
   pip install -r requirements.txt
   ```

6. **Test your changes**
   ```bash
   python train_model.py  # For training changes
   python test_models.py  # For model changes
   streamlit run app.py   # For UI changes
   ```

7. **Commit your changes**
   ```bash
   git commit -m "Add brief description of changes"
   git commit -m "
   - Detailed explanation
   - Additional context
   - Related issue: #123
   "
   ```

8. **Push to your fork**
   ```bash
   git push origin feature/amazing-feature
   ```

9. **Open a Pull Request**
   - Provide a clear description of what you changed and why
   - Reference any related issues using `#issue_number`
   - Include before/after comparison if applicable

## Development Setup

### Environment Setup

```bash
# Create virtual environment
python -m venv .venv

# Activate it
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
# Windows (CMD)
.venv\Scripts\activate.bat
# Linux/Mac
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Code Style

Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/):

```bash
# Use tools like autopep8 or black
pip install black
black *.py
```

### Testing

Test your changes before submitting a PR:

```bash
# Test model training
python train_model.py

# Test model evaluation
python test_models.py

# Test the web app (access http://localhost:8501)
streamlit run app.py
```

## Project Structure

```
├── app.py                 # Streamlit application
├── train_model.py         # Model training
├── test_models.py         # Model testing
├── requirements.txt       # Dependencies
├── data/                  # Dataset
│   ├── KDDTrain+.txt
│   └── KDDTest+.txt
└── models/                # Trained models
    ├── best_model.joblib
    ├── encoders.joblib
    ├── scaler.joblib
    └── feature_names.joblib
```

## Contribution Types

### 1. Bug Fixes
- Fix reported issues
- Add regression tests
- Document the fix in commit message

### 2. Features
- New ML models
- UI improvements
- Performance optimizations
- New datasets support

### 3. Documentation
- README improvements
- Code comments
- Docstrings
- Tutorials
- Examples

### 4. Tests
- Unit tests
- Integration tests
- Edge case testing

### 5. Refactoring
- Code cleanup
- Performance improvements
- Better error handling
- Dependency updates

## What Gets Priority

- **High Priority**:
  - Security issues
  - Critical bugs
  - Performance improvements
  - Accessibility improvements

- **Medium Priority**:
  - Feature requests
  - Documentation
  - Code refactoring
  - Test coverage

- **Lower Priority**:
  - Nice-to-have features
  - Minor UI improvements
  - Dependency updates (unless critical)

## Review Process

1. Automated checks must pass
2. At least one maintainer review
3. All feedback must be addressed
4. Once approved, PR will be merged

## Questions?

- Open a GitHub Discussion
- Open an Issue with the `question` label
- Check existing Issues and PRs

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be recognized in:
- README.md contributors section
- GitHub contributors page
- Release notes

---

Thank you for contributing to NIDS! 🎉
