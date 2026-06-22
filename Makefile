.PHONY: help install dev-install clean test lint format run train test-models check all

help:
	@echo "NIDS - Network Intrusion Detection System"
	@echo ""
	@echo "Available commands:"
	@echo "  make install          - Install dependencies"
	@echo "  make dev-install      - Install dependencies with dev tools"
	@echo "  make run              - Run the Streamlit app"
	@echo "  make train            - Train models"
	@echo "  make test-models      - Test models"
	@echo "  make format           - Format code with black"
	@echo "  make lint             - Check code style with flake8"
	@echo "  make pylint           - Analyze code with pylint"
	@echo "  make test             - Run pytest tests"
	@echo "  make coverage         - Run tests with coverage report"
	@echo "  make check            - Run all checks (lint, format check, security)"
	@echo "  make clean            - Remove cache and build files"
	@echo "  make venv             - Create virtual environment"
	@echo "  make all              - Run all checks and tests"
	@echo ""

venv:
	python -m venv .venv
	@echo "Virtual environment created. Activate with: .venv\\Scripts\\activate (Windows) or source .venv/bin/activate (Linux/Mac)"

install:
	pip install -r requirements.txt

dev-install:
	pip install -r requirements.txt
	pip install -e ".[dev]"

dev-install-all:
	pip install -r requirements.txt
	pip install -e ".[dev,packet-sniffing]"

run:
	streamlit run app.py

train:
	python train_model.py

test-models:
	python test_models.py

format:
	black .
	@echo "Code formatted with black"

check-format:
	black . --check
	@echo "Code format check passed"

lint:
	flake8 . --max-line-length=100 --exclude=.venv,build,dist
	@echo "Flake8 check passed"

pylint:
	pylint app.py train_model.py test_models.py || true
	@echo "Pylint analysis complete"

security:
	bandit -r . -ll || true
	pip-audit || true
	@echo "Security check complete"

test:
	pytest -v

coverage:
	pytest --cov=. --cov-report=html --cov-report=term-missing
	@echo "Coverage report generated in htmlcov/index.html"

check: format lint security
	@echo "All checks passed!"

check-all: lint pylint security check-format test
	@echo "All comprehensive checks passed!"

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".coverage" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "dist" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "build" -exec rm -rf {} + 2>/dev/null || true
	@echo "Cleaned up cache and build files"

all: clean install dev-install check test
	@echo "All tasks completed successfully!"

.DEFAULT_GOAL := help
