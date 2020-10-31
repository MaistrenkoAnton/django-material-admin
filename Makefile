up:
	docker-compose -f docker-compose.yml up

build:
	docker-compose -f docker-compose.yml up --build

down:
	docker-compose -f docker-compose.yml down

migrations:
	docker exec -it material_app sh -c './manage.py makemigrations'

static:
	docker exec -it material_app sh -c './manage.py collectstatic'

migrate:
	docker exec -it material_app sh -c './manage.py migrate'

test:
	docker exec -it material_app sh -c './manage.py test'

coverage:
	docker exec -it material_app sh -c 'coverage run --source='.' manage.py test'

report:
	docker exec -it material_app sh -c 'coverage report'
