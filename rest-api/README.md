This project is a REST API built with FastAPI and SQLAlchemy, designed to run in a Docker environment. It includes database migrations managed with Alembic and uses PostgreSQL as the database system.

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

## Installation and Usage

1. Build and start the services with Docker Compose:

   docker-compose up --build

2. The API will be available at `http://localhost:8000`.

## Database Migrations

- Create a new migration:

  alembic revision --autogenerate -m "migration message"

- Apply migrations:

  alembic upgrade head

## Interactive Documentation

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)
