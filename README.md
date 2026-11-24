# AgroManutenção

Sistema web para gerenciamento de máquinas agrícolas e controle de manutenções preventivas e corretivas.

## Objetivo

O AgroManutenção foi desenvolvido para auxiliar no controle de máquinas agrícolas, registrando informações operacionais e acompanhando manutenções realizadas e futuras.

## Tecnologias Utilizadas

### Backend

- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Poetry
- Pytest

### Frontend

- React
- Vite
- Axios

### Infraestrutura

- Docker
- Docker Compose

### Testes

- Pytest
- Playwright

---

## Funcionalidades

### Máquinas

- Cadastro de máquinas
- Listagem de máquinas
- Edição de máquinas
- Exclusão de máquinas

### Manutenções

- Cadastro de manutenções
- Listagem de manutenções
- Edição de manutenções
- Exclusão de manutenções

### Controle de manutenção

- Verificação automática de manutenção atrasada
- Exibição do status da máquina

---

## Executando com Docker

Na raiz do projeto:

```bash
docker compose up --build
```

---

## Frontend

Disponível em:

http://localhost:5173

---

## Backend

Disponível em:

http://localhost:8000

---

## Swagger

Documentação da API:

http://localhost:8000/docs

---

## Executar Testes Backend

```bash
docker compose exec backend pytest -v
```

---

## Cobertura de Testes

```bash
docker compose exec backend pytest --cov=app
```

---

## Testes E2E

Entrar na pasta frontend:

```bash
cd frontend
```

Executar:

```bash
npx playwright test
```

---

## Banco de Dados

PostgreSQL 16

Banco:

agromanutencao

---
## Link do vídeo 
https://youtu.be/FgAd1R4YykI

## Autor

Tulio Augusto