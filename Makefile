# Install dependencies
install:
	pip install --upgrade pip && pip install -r requirements.txt

# Format code using Black
format:
	black *.py

# Lint code using Ruff (instead of pylint)
lint:
	ruff check *.py mylib/*.py

# Test notebook and Python files using pytest and nbval for notebook
test:
	pytest --nbval python_main_notebook.ipynb -cov=main test_main.py 

# Run all commands in sequence
all: install format lint test
