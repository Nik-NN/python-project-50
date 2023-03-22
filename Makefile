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

make lint:
	poetry run flake8 gendiff
	
package-install:
	python3 -m pip install --user dist/*.whl

.PHONY: install test lint selfcheck check build