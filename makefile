# Makefile do prostego zarządzania projektem: lint + testy

# ===============================
# Linting: Black + Flake8
# ===============================
.PHONY: lint
lint:
	@echo "Running Black..."
	black --exclude "pgdata|notebooks" --check .
	@echo "Running Flake8..."
	flake8 .
	@echo "Linting finished!"

# ===============================
# Testy jednostkowe z pytest
# ===============================
.PHONY: test
test:
	@echo "Running tests..."
	PYTHONPATH=. pytest -v tests/
	@echo "Tests finished!"
