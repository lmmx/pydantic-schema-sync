# pydantic-schema-sync

Synchronise Pydantic model schemas with JSONSchema files.

## Usage

### CLI

```
usage: model-schema-sync [-h] [--model MODEL] [--schema_path SCHEMA_PATH]
                         [--mjs_kwargs MJS_KWARGS]

Config for syncing Pydantic model schemas to disk.

options:
  -h, --help            show this help message and exit
  --model MODEL         Dotted import path to the Pydantic model
  --schema_path SCHEMA_PATH
                        File path to save the schema at
  --mjs_kwargs MJS_KWARGS
                        Kwargs to pass `.model_json_schema()`
```

To serialise the schema of the model named `SyncCLI` (in the package `pydantic_schema_sync`'s `cli` module)
to the file `schema.json`, passing the `by_alias=False` param to `.model_json_schema()`:

```sh
model-schema-sync \
  --model pydantic_schema_sync.cli.SyncCLI \
  --schema_path schema.json \
  --mjs_kwargs '{"by_alias": false}'
```

### Python

From a model class:

```py
from pydantic_schema_sync import sync_schema

# Using field alias (default)
sync_schema(model=Foo, schema_path="schema.json")

# Unaliased field
sync_schema(model=Foo, schema_path="schema.json", mjs_kwargs={"by_alias": False})
```

From a path to a model class:

```py
from pydantic_schema_sync import sync_schema_from_path

# This path must be in an installed package
path_to_model_cls = "pydantic_schema_sync.cli.SyncCLI"
sync_schema_from_path(model=path_to_model_cls, schema_path="schema.json")
```
