.PHONY: install brain-games build publish package-install lint

check: lint test build package-install

release: lint test
	poetry version patch
	poetry build
	poetry publish -r testpypi
	rm dist/*.whl
	rm dist/*.tar.gz
	python3 -m pip install --user --upgrade --index-url https://test.pypi.org/simple/ python-project-lvl1-by-okeangel
	git status

release-minor: lint test
	poetry version minor
	poetry build
	poetry publish -r testpypi
	rm dist/*.whl
	rm dist/*.tar.gz
	python3 -m pip install --user --upgrade --index-url https://test.pypi.org/simple/ python-project-lvl1-by-okeangel
	git status

install:
	poetry install

lint:
	poetry run flake8 brain_games

test:

build:
	poetry build

publish:
	poetry publish -r testpypi

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl
	rm dist/*.whl
	rm dist/*.tar.gz

brain-games:
	poetry run brain-games

