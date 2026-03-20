# Module 18 – Data Build Tool (dbt)

## Learning Objectives
- Understand the role of dbt in modern data engineering pipelines.
- Install and configure dbt (core and dbt Cloud).
- Build a dbt project from scratch: models, seeds, snapshots, tests, and documentation.
- Write reusable SQL with Jinja macros and refactoring patterns.
- Deploy dbt pipelines with CI/CD (GitHub Actions, GitLab CI, Azure DevOps).
- Scale dbt with incremental models, exposures, and packages.
- Debug, profile, and monitor dbt runs.

---

## 1. What is dbt?

Data Build Tool (dbt) is a **SQL‑first** transformation framework that enables analysts and engineers to **write modular, testable, version‑controlled data models**. It sits in the **ELT** layer, turning raw data in a warehouse into curated, analytics‑ready tables.

Key concepts:
- **Models** – `.sql` files that compile to `SELECT` statements.
- **Sources** – definitions of raw tables/views.
- **Seeds** – CSV files loaded as tables.
- **Snapshots** – point‑in‑time versioning of slowly changing dimensions.
- **Tests** – assertions on data quality.
- **Docs** – auto‑generated documentation site.
- **Macros** – reusable Jinja‑templated SQL snippets.

---

## 2. Installation

### 2.1 dbt‑Core (Python package)
```bash
# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate

# Install dbt core for your warehouse (example: PostgreSQL)
pip install "dbt-postgres==1.8.*"
```

### 2.2 dbt‑Cloud (hosted SaaS)
- Sign up at https://cloud.getdbt.com/.
- Create an account, link your Git repository, and configure a warehouse connection.
- Use the web UI for job scheduling and run monitoring.

---

## 3. Project Structure

```text
my_dbt_project/
├─ dbt_project.yml          # project configuration
├─ profiles.yml             # connection profiles (usually in ~/.dbt/)
├─ models/                  # SQL models
│   ├─ staging/            # raw‑to‑staging transformations
│   └─ marts/              # business‑logic models
├─ seeds/                   # CSV files loaded as tables
├─ snapshots/               # snapshot definitions
├─ macros/                  # Jinja macros
├─ tests/                   # custom data tests
└─ analyses/               # ad‑hoc queries (not materialized)
```

### 3.1 `dbt_project.yml`
```yaml
name: my_dbt_project
version: "1.0"
config-version: 2
profile: my_profile

model-paths: ["models"]
seed-paths: ["seeds"]
snapshot-paths: ["snapshots"]
macro-paths: ["macros"]

target-path: "target"
clean-targets: ["target", "dbt_modules"]
```

---

## 4. Defining Sources and Models

### 4.1 Sources (`sources.yml`)
```yaml
version: 2
sources:
  - name: raw
    tables:
      - name: events
        description: Raw event data landing in `public.events_raw`
```

### 4.2 A Staging Model (`models/staging/stg_events.sql`)
```sql
{{ config(materialized='view') }}

with source as (
    select * from {{ source('raw', 'events') }}
),
cleaned as (
    select
        cast(event_timestamp as timestamp) as event_timestamp,
        user_id,
        event_type,
        json_extract_path_text(event_payload, 'product_id') as product_id,
        json_extract_path_text(event_payload, 'price')::numeric as price
    from source
    where event_timestamp is not null
)
select * from cleaned
```

### 4.3 A Fact Model (`models/marts/fct_sales.sql`)
```sql
{{ config(materialized='incremental', unique_key='order_id') }}

with events as (
    select * from {{ ref('stg_events') }}
),
orders as (
    select
        event_timestamp::date as order_date,
        user_id,
        product_id,
        price as order_amount,
        generate_uuid() as order_id
    from events
    where event_type = 'purchase'
)
select * from orders
{% if is_incremental() %}
where event_timestamp > (select max(event_timestamp) from {{ this }})
{% endif %}
```

---

## 5. Seeds (CSV → Table)

Place `seeds/region_lookup.csv`:
```csv
region_id,region_name
1,North America
2,Europe
3,Asia
```

Add `seeds.yml` to configure:
```yaml
version: 2
seeds:
  my_dbt_project:
    region_lookup:
      column_types:
        region_id: integer
```

Run:
```bash
dbt seed
```

---

## 6. Snapshots (Slowly Changing Dimensions)

`snapshots/snap_customer.sql`:
```sql
{% snapshot customer_snapshot %}
{{ config(
    target_schema='snapshots',
    unique_key='customer_id',
    strategy='timestamp',
    updated_at='updated_at'
) }}

select * from {{ source('raw', 'customers') }}
{% endsnapshot %}
```

Run:
```bash
dbt snapshot
```

---

## 7. Tests

### 7.1 Built‑in tests (schema.yml)
```yaml
version: 2
models:
  - name: fct_sales
    columns:
      - name: order_id
        tests:
          - unique
          - not_null
      - name: order_amount
        tests:
          - not_null
          - relationships:
              to: ref('dim_product')
              field: product_id
```

### 7.2 Custom test (`tests/not_future_dates.sql`)
```sql
select *
from {{ ref('stg_events') }}
where event_timestamp > current_timestamp
```
Add to `schema.yml` under `tests`.

Run all tests:
```bash
dbt test
```

---

## 8. Documentation

Add doc blocks in model files:
```sql
{{
    config(
        description="Aggregated daily sales per product",
        meta={"owner": "analytics"}
    )
}}
```

Generate docs site:
```bash
dbt docs generate
```
Serve locally:
```bash
dbt docs serve
```

---

## 9. Macros (Reusable Jinja)

`macros/date_dim.sql`:
```sql
{% macro date_dim(start_date, end_date) %}
with dates as (
    select generate_series('{{ start_date }}'::date,
                         '{{ end_date }}'::date,
                         interval '1 day') as date_day
)
select
    date_day as date,
    extract(isodow from date_day) as iso_weekday,
    extract(dow from date_day) as weekday,
    extract(day from date_day) as day,
    extract(month from date_day) as month,
    extract(year from date_day) as year,
    to_char(date_day, 'YYYY-MM-DD') as date_iso
from dates
{% endmacro %}
```
Use in a model:
```sql
{{ date_dim('2020-01-01', '2025-12-31') }}
```

---

## 10. CI/CD Integration (GitHub Actions example)

Create `.github/workflows/dbt.yml`:
```yaml
name: dbt CI
on: [push, pull_request]
jobs:
  run-dbt:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install dbt
        run: |
          python -m venv .venv
          source .venv/bin/activate
          pip install "dbt-postgres==1.8.*"
      - name: Run dbt deps
        run: |
          source .venv/bin/activate
          dbt deps
      - name: Run dbt test
        env:
          DBT_PROFILES_DIR: ${{ github.workspace }}
          # Set warehouse credentials as secrets
          POSTGRES_HOST: ${{ secrets.PG_HOST }}
          POSTGRES_USER: ${{ secrets.PG_USER }}
          POSTGRES_PASSWORD: ${{ secrets.PG_PASS }}
          POSTGRES_DB: ${{ secrets.PG_DB }}
        run: |
          source .venv/bin/activate
          dbt test
```

---

## 11. Advanced Topics

### 11.1 Incremental Models (already shown) – use `is_incremental()` and `unique_key`.
### 11.2 Exposures – document downstream BI tools:
```yaml
exposures:
  - name: sales_dashboard
    type: dashboard
    url: https://looker.company.com/dashboards/123
    description: Dashboard that visualizes `fct_sales`.
    depends_on:
      - ref('fct_sales')
```
### 11.3 Packages – reuse community models:
```bash
dbt deps --packages "dbt-labs/dbt_utils"
```
Add to `packages.yml`:
```yaml
packages:
  - package: dbt-labs/dbt_utils
    version: [">=0.9.0", "<1.0.0"]
```
### 11.4 dbt Cloud vs. dbt Core – when to choose SaaS (job scheduling, UI) vs. self‑hosted.
### 11.5 Performance profiling – `dbt run --profiles-dir . --target dev --vars '{"debug": true}'` and use `dbt debug`.

---

## 12. Mini‑Lab Walkthrough

1. **Initialize** a new project:
   ```bash
   dbt init my_dbt_project
   ```
2. **Add a source** for `raw.events` and a staging model `stg_events.sql`.
3. **Create a fact model** `fct_sales.sql` with incremental materialization.
4. **Load a seed** `region_lookup.csv` and reference it in a dimension model.
5. **Write a custom test** to ensure no future timestamps.
6. **Generate docs** and browse the site.
7. **Push to GitHub** and enable the CI workflow.
8. **Schedule a dbt Cloud job** (or a cron) to run nightly.

---

## 13. Resources
- Official docs: https://docs.getdbt.com/
- dbt Learn (free interactive tutorials): https://learn.getdbt.com/
- dbt Slack Community: https://community.getdbt.com/
- Book: *Analytics Engineering with dbt* – Tristan Handy
- GitHub repo with example project: https://github.com/fishtown-analytics/dbt-example-project

---

*End of Module 18 – Data Build Tool (dbt)*
