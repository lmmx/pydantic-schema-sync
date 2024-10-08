# pytest-pydantic-schema-sync

`pytest-pydantic-schema-sync` is a pytest plugin that automates the process of saving JSON schemas for Pydantic
models during test execution. It builds upon the functionality provided by the `pydantic-schema-sync` package.

## Features

- Automatically syncs JSON schemas for Pydantic models during pytest execution
- Configurable schema storage location (package root or repository root)
- Easy setup using pytest markers and Enum-based configuration

## Installation

You can install `pytest-pydantic-schema-sync` using pip:

```
pip install pytest-pydantic-schema-sync
```

## Usage

Define an Enum class with your Pydantic model paths, marked with the `pydantic_schema_sync` marker:

```python
from pytest import mark
from enum import Enum

@mark.pydantic_schema_sync
class ModelSchemas(Enum):
    user = "myapp.models.User"
    product = "myapp.models.Product"
```

Running your pytest suite will generate tests for each of these, which fail if the sync is unsuccessful.
The plugin will automatically generate and sync JSON schemas for the specified models using `pydantic-schema-sync`.

## Configuration

You can configure the plugin behavior in your `pytest.ini` or `pyproject.toml` file:

```ini
[tool.pytest.ini_options]
pydantic_schema_sync = {schema_location = "package_root", schema_dir = "schemas", repo_flatten = false, mjs_kwargs = {}}
```

These are the defaults, but it demonstrates use of JSON to configure the plugin.

- `schema_location`: Where to store schema files. Options are "package_root" (default) or "repo_root".
  - `repo_flatten`: If "repo_root" is chosen, then if this option is set to True (default: False)
    all JSON files will be written to a single directory rather than in subfolders per-package.
- `schema_dir`: Name of the directory to store schema files under whichever schema location root. Default is "schemas".
- `mjs_kwargs`: Keyword arguments to pass to the Pydantic models' `model_json_schema()` method.
  Default is `{}` (i.e. do not override any kwargs).
  - A common kwarg you may wish to set is `by_alias` (default: True)

## How It Works

The plugin uses the `pydantic-schema-sync` package to generate JSON schemas for your Pydantic models.
It creates a separate test item for each model specified in your Enum, ensuring that schemas are synced
even if no other tests are run for those models.

## Example

Check out the [simple-plugin-demo](https://github.com/lmmx/pydantic-schema-sync/tree/master/packages/simple-plugin-demo)
for a working example of how to use this plugin.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
