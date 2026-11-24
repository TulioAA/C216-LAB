run:
	cd backend && poetry run uvicorn app.main:app --reload

test:
	cd backend && poetry run pytest -v

coverage:
	cd backend && poetry run pytest --cov=app

docker-build:
	docker compose build

docker-up:
	docker compose up -d

docker-down:
	docker compose down

e2e:
	cd frontend && npx playwright test