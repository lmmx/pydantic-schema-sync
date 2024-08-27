from argparse import ArgumentParser
from pathlib import Path

from pydantic import BaseModel, ImportString, Json
from pydantic.fields import Field

from .sync import sync_schema

__all__ = ("SyncCLI", "run_sync")


class SyncCLI(BaseModel):
    model: ImportString = Field(description="Dotted import path to the Pydantic model")
    schema_path: Path = Field(description="File path to save the schema at")
    mjs_kwargs: Json[dict] | dict = Field(
        description="Kwargs to pass `.model_json_schema()`"
    )


parser = ArgumentParser(
    description="Config for syncing Pydantic model schemas to disk."
)
for field in SyncCLI.model_fields:
    parser.add_argument(f"--{field}", type=str, help=f"Input for {field}")


def run_sync():
    args = parser.parse_args()
    cli_config = SyncCLI.model_validate(vars(args))
    sync_schema(**cli_config.model_dump())
