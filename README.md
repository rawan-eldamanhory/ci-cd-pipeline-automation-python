# CI/CD Pipeline Automation (Python)

A comprehensive demonstration project showcasing professional CI/CD practices including automated testing, code quality checks, documentation generation, and deployment workflows.

## Project Overview

This project demonstrates:
- **Automated Testing** with pytest
- **Code Quality** checks (linting, formatting, type checking)
- **Pre-commit Hooks** for local validation
- **GitHub Actions** CI/CD workflows
- **Automated Documentation** generation
- **Changelog** generation from commits
- **Security Scanning** with bandit and safety
- **Multi-platform Testing** (Linux, Windows, macOS)
- **Code Coverage** reporting

## Project Structure

```
ci-cd-pipeline/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Main CI/CD workflow
├── scripts/
│   └── generate_changelog.py  # Changelog generator
├── calculator.py               # Sample application
├── test_calculator.py          # Comprehensive test suite
├── pyproject.toml              # Modern Python config
├── requirements-dev.txt        # Development dependencies
├── .pre-commit-config.yaml     # Pre-commit hooks config
```

## Features

### 1. **Automated Testing**
- Comprehensive test suite with pytest
- Parametrized tests for coverage
- Fixtures for test organization
- Code coverage reporting
- Test reports in HTML

### 2. **Code Quality**
- **black** - Code formatting
- **flake8** - Style guide enforcement
- **isort** - Import sorting
- **mypy** - Static type checking
- **pylint** - Code analysis
- **bandit** - Security linting

### 3. **CI/CD Pipeline**
- Multi-stage GitHub Actions workflow
- Parallel job execution
- Matrix testing (multiple Python versions & OS)
- Artifact uploads
- Automated releases

### 4. **Pre-commit Hooks**
- Local validation before commits
- Automatic code formatting
- Prevents committing bad code
- Fast feedback loop

### 5. **Documentation**
- Auto-generated API docs
- Sphinx documentation
- Changelog from commits
- GitHub Pages deployment

## Quick Start

### Prerequisites
- Python 3.9 or higher
- Git
- pip

### Installation

```bash
# Clone repository
git clone https://github.com/rawan-eldamanhory/ci-cd-pipeline-automation-python.git
cd ci-cd-pipeline

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov

# Run specific test file
pytest test_calculator.py

# Run tests matching pattern
pytest -k "test_addition"

# Run with markers
pytest -m smoke  # Only smoke tests
pytest -m "not slow"  # Exclude slow tests
```

### Code Quality Checks

```bash
# Format code with black
black .

# Sort imports
isort .

# Lint with flake8
flake8 .

# Type check with mypy
mypy .

# Security check with bandit
bandit -r .

# Run all pre-commit hooks
pre-commit run --all-files
```

---

**Built with Python | Automated with GitHub Actions | Tested with pytest**

**Demonstrates professional CI/CD practices for modern software development**
