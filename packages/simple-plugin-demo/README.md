# demo-test-package

Simple program to demonstrate the use of `pytest-pydantic-schema-sync` pytest plugin:

- Prints a `greeting` then counts up to the given number `count` and skips any of the numbers in `skip`.
- Input is specified as a Pydantic model `InputModel`
- Output is simply a list of `messages` as specified by the Pydantic model `OutputModel`

These two models' schemas are synced as JSON files under the `schemas` directory

## Configuration

The `pyproject.toml` demonstrates configuration of the plugin:

```
[tool.pytest.ini_options]
pydantic_schema_sync = {schema_location = "package_root", schema_dir = "schemas", repo_flatten = false, mjs_kwargs = {}}
```

These are the defaults, but it demonstrates use of JSON to configure the plugin.
