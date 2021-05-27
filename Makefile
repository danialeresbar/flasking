bash:
	docker exec -it flasking bash

dev-up:
	docker-compose up --build

dev-stop:
	docker-compose down -v

prod-up-attached:
	docker-compose -f docker-compose.prod.yml up --build

prod-up-detached:
	docker-compose -f docker-compose.prod.yml up -d --build
