# pydantic-schema-sync

Synchronise Pydantic model schemas with JSONSchema files.

## Usage

### Python

From a model class:

```py
from pydantic_schema_sync import sync_schema

sync_schema(model=DemoModel, schema_path="schema.json")
```

From a path to a model class:

```py
from pydantic_schema_sync import sync_from_model_path

path_to_model_cls = "pydantic_schema_sync.cli.SyncCLI"
sync_from_model_path(
    {"model": path_to_model_cls, "schema_path": "schema.json", "mjs_kwargs": {}}
)
```

### CLI

To serialise the schema of the model named `ExampleModel` (in the package `my_pkg`'s module
`my_module`) to the file `test.json`, passing the `by_alias=False` param to `.model_json_schema()`:

```sh
model-schema-sync \
  --model my_pkg.my_module.ExampleModel \
  --schema_path test.json \
  --mjs_kwargs '{"by_alias":false}'
```
