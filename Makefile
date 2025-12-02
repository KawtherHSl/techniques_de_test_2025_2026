test:
	pytest

unit_test:
	pytest -m "not slow"

perf_test:
	pytest -m slow

coverage:
	coverage run -m pytest
	coverage html

lint:
	ruff check .

doc:
	pdoc3 -o docs triangulator
