.PHONY: install test coverage lint format run build up down logs ps help \
frontend-install frontend-lint frontend-format frontend-build \
frontend-test frontend-test-e2e check-all

BACKEND := cd backend
FRONTEND := cd frontend

POETRY := $(BACKEND) && poetry run
PYTEST := $(POETRY) pytest

install:
	$(BACKEND) && poetry install

test:
	$(PYTEST)

coverage:
	$(PYTEST) --cov=app --cov-report=term-missing

lint:
	$(POETRY) ruff check .

format:
	$(POETRY) ruff format .

run:
	$(POETRY) uvicorn app.main:app --reload

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

ps:
	docker compose ps

# =====================
# FRONTEND
# =====================

frontend-install:
	$(FRONTEND) && npm install

frontend-lint:
	$(FRONTEND) && npm run lint

frontend-format:
	$(FRONTEND) && npm run format

frontend-build:
	$(FRONTEND) && npm run build

frontend-test:
	$(FRONTEND) && npm run test

frontend-test-e2e:
	$(FRONTEND) && npm run test:e2e

# =====================
# CHECK GERAL
# =====================

check-all:
	make lint
	make test
	make frontend-lint
	make frontend-test
	make frontend-build

help:
	@echo "=== BACKEND ==="
	@echo "make install"
	@echo "make test"
	@echo "make coverage"
	@echo "make lint"
	@echo "make format"
	@echo "make run"
	@echo ""
	@echo "=== DOCKER ==="
	@echo "make build"
	@echo "make up"
	@echo "make down"
	@echo "make logs"
	@echo "make ps"
	@echo ""
	@echo "=== FRONTEND ==="
	@echo "make frontend-install"
	@echo "make frontend-lint"
	@echo "make frontend-format"
	@echo "make frontend-build"
	@echo "make frontend-test"
	@echo "make frontend-test-e2e"
	@echo ""
	@echo "=== GERAL ==="
	@echo "make check-all"