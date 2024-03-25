# Base Python Async Database
Personal repo to spin up a Python project with scaffolding for utilizing an async database. Currently, it is using postgresql.

---

# Features

- Environment variables manager
- Connection string via environment variables
- UUID for IDs
- SQLAlchemy Relationship Examples:
  - Foreign key (one-to-many)
  - Many-to-many

---

# Setup
```bash
python -m venv venv
source venv/bin/activate
(venv) pip install -r requirements.txt

cp env .env

# setup postgresql database
# make sure your .env has the correct values for connection string
# complete your models
./migrate.sh add "message"
./migrate.sh run
```

---

# Commands

```
./migrate.sh init
./migrate.sh add "initial migration"
./migrate.sh run
./migrate.sh revert
```

---

# Deps

- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)
- [alembic](https://pypi.org/project/alembic/)
- [asyncpg](https://github.com/MagicStack/asyncpg)
- [python-dot-env](https://github.com/theskumar/python-dotenv)
