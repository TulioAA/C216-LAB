# C216-L1-Sistemas-Distribuidos
Repositório para atividades práticas da matéria de Sistemas Distribuídos

## Projeto Backend
Este projeto utiliza FastAPI, Poetry para gerenciamento de dependências, Pytest para testes e Docker para containerização.

## Testes
Rodar os testes localmente:
make test

Rodar com cobertura:
make coverage

Os testes também são executados automaticamente no GitHub Actions em cada push ou pull_request.

## Lint e formatação
Verificar estilo de código:
make lint

Formatar código automaticamente:
make format

## Rodar servidor local
Iniciar o servidor FastAPI:
make run

O servidor ficará disponível em:
http://localhost:8000

## Docker
Build dos containers:
make build

Subir containers:
make up

Derrubar containers:
make down

Ver logs:
make logs

Listar containers ativos:
make ps

## CI/CD
O workflow de CI está configurado em .github/workflows/ci-backend.yml e executa:
- Instalação de dependências com Poetry
- Execução dos testes com Pytest
- Relatório de cobertura
