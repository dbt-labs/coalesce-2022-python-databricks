# dbt Python models on Databricks demo for Coalesce 2022

This repository contains a demo of dbt Python models on Databricks for the Coalesce 2022 conference. It will not be actively maintained. See the repository it was forked from for a current version -- we will work to merge the Python models into the `main` branch there after Coalesce.

## Cool gifs

What a cool DAG! Python and SQL side-by-side in dbt!

![DAG](etc/dag.gif)

Python models in dbt Cloud!

![py_gif](etc/py_gif.gif)

## Challenges

See [the challenges directory's README.md](models/challenges/README.md).

## Non-workshop dev setup

TODO: rework this

### Get started

Follow these instructions to run yourself.

### Environment

If you're running in dbt Cloud, ensure your environment(s) that need to run Python models are on v1.3+.

To run locally, you need to update `dbt-core` and `dbt-databricks` to 1.3 or later. We recommend creating a fresh `venv` and `pip install`ing the packages. The exact steps may vary by your platform, but as an example with an environment named `dbt_py`:

```bash
$ python3 -m venv dbt_py
$ source dbt_py/bin/activate
$ (dbt_py) pip install --upgrade 'dbt-core~=1.3.0' 'dbt-databricks~=1.3.0'
$ (dbt_py) which python3
```

You can run `dbt --version` to ensure you have v1.3 installed.

To deactivate:

```bash
$ (dbt_py) deactivate
$ which python3
```

### dbt deps

Run `dbt deps`.

### Source external tables

Admin setup: create the `ecommerce` schema in Databricks:

```sql
create schema if not exists ecommerce
```

Run the external tables operation:

```bash
$ (dbt_py) dbt run-operation stage_external_sources
```

### Run or build

Run individual models or build the entire project!

```bash
$ (dbt_py) dbt run -s describe_py
$ (dbt_py) dbt build
```

And generate the docs!

```bash
$ (dbt_py) dbt docs generate && dbt docs serve
```

## Contributing

We'd welcome contributions to this demo project. However, we will likely archive this repository sometime after Coalesce 2022. Consider contributing to the repository this one is forked from instead!
