# Install dependencies
install:
	pip install --upgrade pip && pip install -r requirements.txt

# Format code using Black
format:
	black *.py

# Lint code using Ruff (instead of pylint)
lint:
	ruff check *.py mylib/*.py

# Test Python notebook using nbval
test_notebook:
	pytest --nbval python_main_notebook.ipynb

# Test Python scripts with pytest
test_scripts:
	pytest --cov=main test_main.py

# Run all tests (notebook + scripts)
test: test_notebook test_scripts

# Run all commands in sequence
all: install format lint test
