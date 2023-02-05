build:
	docker compose down
	docker compose build
	docker compose up -d

up:
	docker compose up -d

down:
	docker compose down

bash:
	docker exec -it python bash

pip:
	docker exec -it python pip3 $(CMD)

log:
	docker logs -t -f python