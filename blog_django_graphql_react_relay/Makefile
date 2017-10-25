.PHONY: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

.PHONY: clean-artifacts
clean-artifacts:
	rm -fr film_api/.tox/
	rm -fr film_api/.cache/

.PHONY: clean-node-modules
clean-node-modules:
	rm -rf film_ui/node_modules

.PHONY: clean
clean: clean-pyc clean-artifacts clean-node-modules

.PHONY: build-api
build-api:
	docker-compose build

.PHONY: build-ui
build-ui:
	cd film_ui; yarn

.PHONY: run-api
run-api:
	docker-compose up

.PHONY: run-ui
run-ui:
	cd film_ui; yarn run start

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
	docker-compose run film_api python manage.py loaddata data.json

.PHONY: enter-film_api
enter-film_api:
	film_api-compose run film_api bash

.PHONY: isort
isort:
	docker-compose exec film_api sh -c 'isort --skip-glob=.?* -rc .'

.PHONY: lint-api
lint-api:
	docker-compose exec film_api sh -c 'flake8 .'

.PHONY: generate-schema
generate-schema:
	docker-compose run film_api python manage.py graphql_schema
	mv film_api/schema.json film_ui/schema.json
