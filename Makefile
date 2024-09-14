install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	ruff check *.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

test:
	python -m pytest -vv --nbval -cov=mylib -cov=main test_*.py *.ipynb

all: install format lint test

generate_and_push:
	python python_main.py 
	git config --local user.email "action@github.com"; \
	git config --local user.name "GitHub Action"; \
	git add top_teams_wins.png win_clean_sheet_relation.png; \
	git commit -m "Add generated plots"; \
	git push; \
