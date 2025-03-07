PYTHONPATH := $(shell pwd)

install:
	@PYTHONPATH="${PYTHONPATH}" poetry install

linter: clean format
	@PYTHONPATH="${PYTHONPATH}" poetry run bandit ./src && poetry run ruff check ./src && poetry run black --check ./src

format:
	@PYTHONPATH="${PYTHONPATH}" poetry run isort ./src && poetry run black ./src

security:
	@PYTHONPATH="${PYTHONPATH}" poetry run bandit -v -r ./src -c "pyproject.toml"

test: clean
	@PYTHONPATH="${PYTHONPATH}" poetry run -vvv coverage run -vvv -m pytest && poetry run coverage report -m

test-cov: test
	@PYTHONPATH="${PYTHONPATH}" poetry run pytest -xs --cov src/app --cov-report html --cov-report=xml --cov-report term-missing --cov-config .coveragerc

test-report: test
	@PYTHONPATH="${PYTHONPATH}" poetry run coverage html || true && open ./htmlcov/index.html

clean:
	@find . | grep -E '.pyc|.pyo|pycache' | xargs rm -rf
	@find . | grep -E '.pyc|.pyo|pycache|pytest_cache' | xargs rm -rf
	@rm -rf ./htmlcov
	@rm -rf ./pycache
	@rm -rf ./pycache
	@rm -rf ./.pytest_cache
	@rm -rf ./.mypy_cache
	@find . -name 'unit_test.db' -exec rm -r -f {} +
	@find . -name '.coverage' -exec rm -r -f {} +

run-containers:
	docker-compose -f .docker/docker-compose.yml up -d

run:
	 poetry run python main.py

run-create:
	python3 scripts/create_tables.py