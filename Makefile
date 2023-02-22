lint:
	poetry run flake8

install:
	poetry install

run:
	poetry run python manage.py runserver

test:
	poetry run python manage.py test

migrate:
	poetry run python manage.py migrate
