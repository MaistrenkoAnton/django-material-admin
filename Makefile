up:
	docker-compose -f docker-compose.yml up

build:
	docker-compose -f docker-compose.yml up --build

down:
	docker-compose -f docker-compose.yml down

migrations:
	docker exec -it nect_world_app bash -c './manage.py makemigrations'

migrate:
	docker exec -it nect_world_app bash -c './manage.py migrate'

test:
	docker exec -it nect_world_app bash -c './manage.py test'

coverage:
	docker exec -it nect_world_app bash -c 'coverage run --source='.' manage.py test'

report:
	docker exec -it nect_world_app bash -c 'coverage report'
