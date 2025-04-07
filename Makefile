.PHONY: run
run:
	poetry run python manage.py runserver

.PHONY: makemigrations
makemigrations:
	poetry run python manage.py makemigrations

.PHONY: migrate
migrate: makemigrations
	poetry run python manage.py migrate

.PHONY: init-data
init-data:
	poetry run python manage.py shell -c "from inventory.models import UnitOfMeasure; UnitOfMeasure.objects.get_or_create(name='Piece', abbreviation='pc'); UnitOfMeasure.objects.get_or_create(name='Kilogram', abbreviation='kg'); UnitOfMeasure.objects.get_or_create(name='Liter', abbreviation='L'); UnitOfMeasure.objects.get_or_create(name='Box', abbreviation='box')"

.PHONY: setup
setup: migrate init-data
	@echo "Setup complete! Run 'make run' to start the server."

.PHONY: test
test:
	poetry run pytest

.PHONY: smoke-test
smoke-test:
	poetry run pytest tests/test_smoke.py -v
	
.PHONY: test-watch
test-watch:
	poetry run ptw --clear --afterrun "echo '\n\nWatching for changes...'"

.PHONY: docker-build
docker-build:
	docker build -t inventory-app:$(TAG) .

.PHONY: docker-run
docker-run:
	docker run -p 8000:8000 -v $(shell pwd)/db.sqlite3:/app/db.sqlite3 inventory-app:$(TAG)