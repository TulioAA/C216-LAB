run:
	cd Backend && poetry run uvicorn app.main:app --reload

test:
	cd Backend && poetry run pytest

docker-build:
	docker compose build

docker-up:
	docker compose up