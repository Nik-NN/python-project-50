install:
	poetry install

gendiff:
	poetry run gendiff

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

.PHONY: all test clean