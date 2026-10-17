.PHONY: install test lint format run help

BACKEND := cd backend
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

help:
	@echo "Comandos disponíveis:"
	@echo "  make install  - instala dependências"
	@echo "  make test     - executa testes"
	@echo "  make coverage  - executa testes com cobertura"
	@echo "  make lint      - verifica código"
	@echo "  make format    - formata código"
	@echo "  make run       - inicia servidor"
	@echo "  make build     - build docker"
	@echo "  make up        - sobe containers"
	@echo "  make down      - derruba containers"
	@echo "  make logs      - mostra logs"
	@echo "  make ps        - lista containers"