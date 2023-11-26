.PHONY: install check

install:
	poetry install --no-interaction

check:
	poetry run ruff check --fix .
	poetry run ruff format .
	poetry run mypy --explicit-package-bases .
	poetry run pytest --cov=.