
from dagster_project.constants import dbt_manifest_path
from dagster import AssetExecutionContext
from dagster_dbt import (
    DbtCliResource,
    dbt_assets,
)


@dbt_assets(
    manifest=dbt_manifest_path,
)
def dagster_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

