.PHONY: install typecheck test

install:
	poetry install --no-interaction

typecheck:
	poetry run ruff check --fix .
	poetry run ruff format .
	poetry run mypy --explicit-package-bases .

test:
	poetry run pytest --cov=.
