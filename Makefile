MODULE_VERSION := $(shell cat redmx/VERSION )

all: lint build test

clean:
	rm -rf dist/

build:
	PYTHONPATH=. python3 -m build
	gitchangelog > CHANGELOG.md
	make -C docs html

lint:
	yamllint -s .
	flake8

publish:
	python3 -m twine upload dist/*

test:
	@echo $(MODULE_VERSION)
	PYTHONPATH=.:.. pytest
