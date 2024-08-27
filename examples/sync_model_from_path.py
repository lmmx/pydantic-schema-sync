from os import sync

from pydantic_schema_sync import sync_schema_from_path

# This path must be in an installed package
path_to_model_cls = "pydantic_schema_sync.cli.SyncCLI"
sync_schema_from_path(model=path_to_model_cls, schema_path="schema.json", mjs_kwargs={})
