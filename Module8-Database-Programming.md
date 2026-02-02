# Module 8: Database Programming & Tooling

This module teaches pragmatic database programming across PostgreSQL, MySQL, and SQLite. You will configure local instances, explore schemas with DBeaver, and build Python data-access layers that respect performance and security best practices.

## Learning Objectives
- Install and configure PostgreSQL, MySQL, and SQLite for local development.
- Model schemas, constraints, and migrations with repeatable workflows.
- Use DBeaver for visual exploration, ER diagrams, and administrative tasks.
- Connect from Python using `psycopg`, `mysql-connector-python`, and the built-in `sqlite3` module with parameterized queries and connection pooling.
- Implement transactional logic, batching, and basic ORM patterns.

---

## 1. Environment Setup Overview

| Database | Install Notes | Default Port | Local Auth Tip |
| --- | --- | --- | --- |
| PostgreSQL | `apt/brew install postgresql` or Docker image `postgres:16-alpine` | 5432 | Create dev role via `createuser --interactive` |
| MySQL | `apt install mysql-server` or Docker `mysql:8` | 3306 | Set root password, enable native password plugin if needed |
| SQLite | Built-in binary/database file | N/A | Database is a single `.db` file |

Sample Docker compose snippet:

```yaml
services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: dev
      POSTGRES_PASSWORD: devpass
      POSTGRES_DB: course_db
    ports:
      - "5432:5432"
  mysql:
    image: mysql:8
    command: ["--default-authentication-plugin=mysql_native_password"]
    environment:
      MYSQL_ROOT_PASSWORD: rootpass
      MYSQL_DATABASE: course_db
    ports:
      - "3306:3306"
```

---

## 2. Schema Design & Migration Basics

1. **Normalization & Keys**
   - Use primary keys, foreign keys, and unique constraints to preserve integrity.
   - Employ check constraints for domain-specific rules (e.g., `CHECK (quantity >= 0)`).
2. **Migration Tooling**
   - PostgreSQL/MySQL: use Alembic or Flyway for versioned migrations.
   - SQLite: maintain SQL scripts; consider `alembic` with `BatchOperations` for limited ALTER support.
3. **Sample Migration (PostgreSQL)**

```sql
CREATE TABLE inventory (
  id SERIAL PRIMARY KEY,
  sku TEXT NOT NULL UNIQUE,
  quantity INTEGER NOT NULL DEFAULT 0,
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

---

## 3. PostgreSQL Programming Essentials

- **psql Cheatsheet**
  - Connect: `psql postgresql://dev:devpass@localhost:5432/course_db`
  - List tables: `\dt`
  - Inspect schema: `\d+ inventory`
  - Export query: `\copy (SELECT * FROM inventory) TO 'inventory.csv' CSV HEADER`
- **Performance Tips**
  - Use `EXPLAIN ANALYZE` to evaluate query plans.
  - Create indexes on foreign keys and frequently filtered columns.
- **Python (psycopg)**

```python
import psycopg

dsn = "postgresql://dev:devpass@localhost:5432/course_db"
with psycopg.connect(dsn, autocommit=False) as conn:
    with conn.cursor() as cur:
        cur.execute("INSERT INTO inventory (sku, quantity) VALUES (%s, %s)", ("ABC-1", 100))
        conn.commit()
```

- **Pooling**
  - Use `psycopg_pool.ConnectionPool` for web apps to reuse connections safely.

---

## 4. MySQL Programming Essentials

- **mysql CLI**
  - Connect: `mysql -u root -p -h 127.0.0.1 -P 3306 course_db`
  - Show tables: `SHOW TABLES;`
  - Describe structure: `DESCRIBE orders;`
  - Import dump: `mysql -u root -p course_db < backup.sql`
- **Transaction Notes**
  - Ensure tables use InnoDB to support transactions and row-level locking.
  - Adjust isolation level per workload: `SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;`
- **Python (`mysql-connector-python`)**

```python
import mysql.connector

conn = mysql.connector.connect(user="root", password="rootpass", host="127.0.0.1", database="course_db")
cur = conn.cursor(dictionary=True)
cur.execute("SELECT * FROM orders WHERE status = %s", ("pending",))
rows = cur.fetchall()
conn.commit()
cur.close()
conn.close()
```

- **Prepared Statements**
  - Always use parameter placeholders (`%s`) to avoid SQL injection.

---

## 5. SQLite Programming Essentials

- **When to Use**
  - Embedded apps, prototyping, local-first PWAs, CLI tools.
- **Shell Basics**
  - Enter shell: `sqlite3 course.db`
  - List tables: `.tables`
  - Enable headers + column mode: `.headers on` / `.mode column`
- **Python (`sqlite3`)**

```python
import sqlite3

conn = sqlite3.connect("course.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, title TEXT, body TEXT)")
cur.execute("INSERT INTO notes (title, body) VALUES (?, ?)", ("Idea", "Prototype"))
conn.commit()
for row in cur.execute("SELECT * FROM notes"):
    print(dict(row))
conn.close()
```

- **Concurrency Considerations**
  - SQLite allows one writer at a time; use WAL mode for better concurrency: `PRAGMA journal_mode = WAL;`

---

## 6. DBeaver Workflow

1. Install DBeaver (community edition) from https://dbeaver.io/download/.
2. Create connections for PostgreSQL/MySQL/SQLite using saved credentials.
3. Use the Database Navigator to:
   - Browse schemas, tables, views, procedures.
   - Generate ER diagrams (right-click → "Create new ER diagram").
   - Run SQL scripts with syntax highlighting and auto-complete.
4. Export data via right-click → "Export Data" to CSV, JSON, or SQL insert scripts.
5. Manage connections via folders (dev/staging/prod) and leverage DBeaver's SSH tunnels for secure access.

Lab: connect to the Docker-compose databases, visualize relationships, and generate a schema compare report.

---

## 7. Python Data-Access Patterns

### Core Guidelines
- Centralize DSN/credentials via environment variables or config files.
- Use context managers to ensure cursors and connections close even on error.
- Prefer parameterized SQL or query builders to avoid injection.

### Async Examples
- `asyncpg` for PostgreSQL, `aiomysql` for MySQL – wrap queries in `async with pool.acquire()` blocks.
- Use `asyncio.to_thread` to interact with SQLite since it is blocking.

### Lightweight ORM Option
- Use SQLAlchemy Core or ORM to map models across PostgreSQL/MySQL/SQLite with one codebase.

```python
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine, select

engine = create_engine("postgresql+psycopg://dev:devpass@localhost/course_db", future=True)
metadata = MetaData()

customers = Table(
    "customers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(255), unique=True),
)

with engine.begin() as conn:
    metadata.create_all(conn)
    conn.execute(customers.insert().values(email="user@example.com"))
    rows = conn.execute(select(customers)).all()
    print(rows)
```

---

## 8. Capstone Project

Build a mini CRM that:
1. Uses PostgreSQL in production, MySQL replica for analytics, and SQLite for offline desktop mode.
2. Provides DBeaver project files documenting schemas and ERDs.
3. Offers Python scripts (CLI or FastAPI) that detect the target database via config and run identical CRUD operations.
4. Implements migrations, seed scripts, tests for SQL queries, and deployment instructions referencing Modules 6 & 7.

Deliverables include ER diagrams, SQL migrations, Python client code, and automation to spin up databases via Docker compose.
