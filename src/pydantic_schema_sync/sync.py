from __future__ import annotations

from json import dumps, loads
from typing import TypeVar

from pydantic import BaseModel, FilePath, ImportString, NewPath, validate_call

__all__ = ("write_schema", "sync_schema", "sync_schema_from_path")

T = TypeVar("T", bound=BaseModel)


@validate_call
def write_schema(model_schema: dict, schema_path: NewPath | FilePath) -> None:
    schema_path.parent.mkdir(exist_ok=True)
    schema_json = dumps(model_schema, indent=2)
    schema_path.write_text(schema_json)
    return


@validate_call
def sync_schema(
    model: type[T], schema_path: NewPath | FilePath, mjs_kwargs: dict = {}
) -> None:
    """
    Synchronize the schema of a Pydantic model to a JSON file on disk.

    Args:
        model: The Pydantic model.
        schema_path: The path to the existing JSON schema file.
        mjs_kwargs: The kwargs to pass to the `model_json_schema()` method.
    """
    fresh = model.model_json_schema(**mjs_kwargs)
    if exists := schema_path.exists():
        previous = loads(schema_path.read_text())
    if not exists or previous != fresh:
        write_schema(model_schema=fresh, schema_path=schema_path)
    return


@validate_call
def sync_schema_from_path(
    model: ImportString, schema_path: NewPath | FilePath, mjs_kwargs: dict = {}
) -> None:
    """Trivial wrapper using an ImportString to load the model class."""
    return sync_schema(model=model, schema_path=schema_path, mjs_kwargs=mjs_kwargs)
