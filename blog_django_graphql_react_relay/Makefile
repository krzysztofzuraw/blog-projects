.PHONY: help

help:
	@echo "Help"

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-artifacts:
	rm -fr .tox/
	rm -fr .cache/

clean: clean-build clean-pyc clean-artifacts

build:
	docker-compose build

run:
	docker-compose up

make-migrations:
	docker-compose run django python manage.py makemigrations

migrate:
	docker-compose run django python manage.py migrate

createsuperuser:
	docker-compose run django python manage.py createsuperuser

dumpdata:
	docker-compose run django python manage.py dumpdata --exclude=auth --exclude=contenttypes --exclude=sessions --output=data.json

loaddata:
	docker-compose run django python manage.py loaddata data.json

enter-docker:
	docker-compose run django bash

isort:
	docker-compose exec django sh -c 'isort --skip-glob=.?* -rc .'

lint:
	docker-compose exec django sh -c 'flake8 .'
