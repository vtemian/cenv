.PHONY: install test test-cov typecheck lint format check clean

install:
	uv pip install -e ".[dev]"

test:
	pytest tests/ -v

test-cov:
	pytest --cov=src/cenv --cov-report=term-missing --cov-report=xml -v

typecheck:
	mypy src/cenv --strict

lint:
	ruff check src/cenv tests/

format:
	ruff check --fix src/cenv tests/

check: lint typecheck test-cov
	@echo "✅ All checks passed!"

clean:
	rm -rf build/ dist/ *.egg-info
	rm -f coverage.xml .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +
	find . -type d -name .ruff_cache -exec rm -rf {} +
