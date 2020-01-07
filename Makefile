PACKAGES = python_project_template tests

.PHONY: ci
ci: check test

.PHONY: check
check: check-black check-isort flake lint

.PHONY: format
format:
	black --line-length 79 *.py $(PACKAGES)
	isort --recursive $(PACKAGES) *.py

.PHONY: check-black
check-black:
	black --line-length 79 *.py $(PACKAGES) --check

.PHONY: check-isort
check-isort:
	isort --recursive $(PACKAGES) *.py --check-only

.PHONY: flake
flake:
	flake8 --max-complexity 10 *.py $(PACKAGES)

.PHONY: lint
lint:
	pylint *.py $(PACKAGES) --disable=fixme

.PHONY: test
test:
	python setup.py test
