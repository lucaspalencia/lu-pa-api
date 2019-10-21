# Flask API

## Requirements

To run this project you need to install:

- [docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/)

## Running

All what you need is packed on docker-compose.

Setup the project:

```bash
make build
```

Start application:

```bash
make up
```

This command will launch these services:

- The API, accessible on [http://localhost:5000/health](http://localhost:5000/health)
- Postgres on port 5432

## Migrations and Seeds

Apply migrations on database:

```bash
make db-upgrade
```

Run seeds to create teams and simulate groups / playoff matches:

```bash
make db-seed
```

Endpoints with data:

- Events GET: [http://localhost:5000/events/1](http://localhost:5000/events/1)
- Groups GET: [http://localhost:5000/events/1/groups](http://localhost:5000/events/1/groups)
- Playoff matches GET: [http://localhost:5000/events/1/playoff](http://localhost:5000/events/1/playoff)

> When making API calls, you need to send x-api-key in request header with the value that is on your .env file.

## Tests

To run linter:

```bash
make lint
```

To run tests:

```bash
make test
```
