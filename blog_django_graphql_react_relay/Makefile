.PHONY: help
help:
	@echo "Help"

.PHONY: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

.PHONY: clean-pyc
clean-build:
	rm -fr film_api/build/
	rm -fr film_api/dist/
	rm -fr film_api/*.egg-info

.PHONY: clean-artifacts
clean-artifacts:
	rm -fr film_api/.tox/
	rm -fr film_api/.cache/

.PHONY: clean-node-modules
clean-node-modules:
	rm -fr film_ui/node_modules

.PHONY: clean
clean: clean-build clean-pyc clean-artifacts clean-node-modules

.PHONY: build
build:
	docker-compose build

.PHONY: run
run:
	docker-compose up

.PHONY: make-migrations
make-migrations:
	docker-compose run film_api python manage.py makemigrations

.PHONY: migrate
migrate:
	docker-compose run film_api python manage.py migrate

.PHONY: shell
shell:
	docker-compose run film_api python manage.py shell

.PHONY: createsuperuser
createsuperuser:
	docker-compose run film_api python manage.py createsuperuser

.PHONY: dumpdata
dumpdata:
	docker-compose run film_api python manage.py dumpdata --exclude=auth --exclude=contenttypes --exclude=sessions --output=data.json

.PHONY: loaddata
loaddata:
	docker-compose run django python manage.py loaddata data.json

.PHONY: enter-docker
enter-docker:
	docker-compose run film_api bash

.PHONY: isort
isort:
	docker-compose exec film_api sh -c 'isort --skip-glob=.?* -rc .'

.PHONY: lint
lint:
	docker-compose exec film_api sh -c 'flake8 .'
