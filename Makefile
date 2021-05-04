.PHONY: install brain-games build publish package-install lint

check: lint build package-install

release: check
	poetry version minor
	git status

install:
	poetry install

lint:
	poetry run flake8 brain_games

build:
	poetry version patch
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl
	rm dist/*.whl
	rm dist/*.tar.gz

brain-games:
	poetry run brain-games

