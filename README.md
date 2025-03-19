# Pydantic Schema Sync

A toolkit for synchronising Pydantic model schemas with JSONSchema files.

## Overview

This repository contains a collection of packages that work together to help maintain synchronised JSON schema files from Pydantic models in your Python projects. It follows a monorepo structure with the following components:

### Packages

- [**pydantic-schema-sync**](packages/pydantic-schema-sync/README.md): The core library that provides functionality to generate and synchronise JSON schemas from Pydantic models.
- [**pytest-pydantic-schema-sync**](packages/pytest-pydantic-schema-sync/README.md): A pytest plugin that automates the process of generating and maintaining JSON schemas during test runs.
- [**simple-plugin-demo**](packages/simple-plugin-demo/README.md): A demonstration project showing how to use the pytest plugin in a real-world scenario.

## Features

- Automatically generate JSON schemas from Pydantic models
- Keep schemas synchronised with model definitions
- Choose between standard and aliased field names in schemas
- Easy integration with your test suite via pytest plugin
- Configurable schema storage locations
- Command-line interface for manual schema generation

## Installation

### Core Library

```bash
pip install pydantic-schema-sync
```

### Pytest Plugin

```bash
pip install pytest-pydantic-schema-sync
```

## Quick Start

### Using the Core Library

```python
from pydantic import BaseModel, Field
from pydantic_schema_sync import sync_schema

class UserModel(BaseModel):
    user_id: int = Field(description="User identifier")
    user_name: str = Field(description="User's full name", alias="name")

# Synchronise the schema to a JSON file
sync_schema(model=UserModel, schema_path="user_schema.json")

# Use non-aliased field names
sync_schema(
    model=UserModel,
    schema_path="user_schema_no_alias.json",
    mjs_kwargs={"by_alias": False}
)
```

### Using the CLI

```bash
model-schema-sync \
  --model your_package.models.UserModel \
  --schema_path user_schema.json \
  --mjs_kwargs '{"by_alias": false}'
```

### Using the Pytest Plugin

1. Define a marker for Pydantic models to synchronise:

```python
# tests/schema_test.py
from enum import Enum
from pytest import mark

@mark.pydantic_schema_sync
class SyncedSchemas(Enum):
    user = "your_package.models.UserModel"
    product = "your_package.models.ProductModel"
```

2. Configure in your `pyproject.toml` (optional):

```toml
[tool.pytest.ini_options]
pydantic_schema_sync = {schema_location = "package_root", schema_dir = "schemas", mjs_kwargs = {by_alias = false}}
```

3. Run your tests:

```bash
pytest
```

## Project Structure

```
pydantic-schema-sync/
├── packages/
│   ├── pydantic-schema-sync/         # Core library
│   ├── pytest-pydantic-schema-sync/  # Pytest plugin
│   └── simple-plugin-demo/           # Example implementation
├── pyproject.toml                    # Workspace configuration
└── README.md                         # This file
```

## Requirements

- Python 3.10+
- Pydantic v2+

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.