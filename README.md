# pydantic-schema-sync

### Library Structure
- **sync.py:** Core functionality to sync schemas.
- **utilities.py:** Helper functions.
- **cli.py:** Command-line interface for convenience.
- **__init__.py:** Package initialization.

### sync.py

```python
import os
import json
from pydantic import BaseModel
from typing import Type

def synchronize_schema(model: Type[BaseModel], file_path: str) -> bool:
    """
    Synchronize the schema of a Pydantic model to a JSON file on disk.

    Args:
        model (Type[BaseModel]): The Pydantic model.
        file_path (str): The path to the JSON schema file.

    Returns:
        bool: True if the schema was updated, False if already up-to-date.
    """
    # Generate the new schema
    new_schema = model.schema()

    # Check if the schema file exists
    if os.path.exists(file_path):
        # Load the current schema from the file
        with open(file_path, 'r') as f:
            current_schema = json.load(f)

        # Compare the current schema with the new schema
        if current_schema != new_schema:
            # Overwrite the schema file if the schema has changed
            with open(file_path, 'w') as f:
                json.dump(new_schema, f, indent=2)
            return True
    else:
        # Schema file does not exist, write the new schema
        with open(file_path, 'w') as f:
            json.dump(new_schema, f, indent=2)
        return True

    return False
```

### utilities.py

```python
import os

def ensure_directory_exists(directory: str):
    """
    Ensure that a directory exists; if not, create it.

    Args:
        directory (str): The path to the directory.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
```

### cli.py

```python
import click
from sync import synchronize_schema
from utilities import ensure_directory_exists

@click.command()
@click.argument('model_name')
@click.argument('schema_path')
def sync(model_name, schema_path):
    """
    CLI command to synchronize Pydantic model schema to JSON file.

    Args:
        model_name (str): The dot path of the Pydantic model (e.g. mymodule.MyModel)
        schema_path (str): The file path where the schema should be saved.
    """
    module_name, class_name = model_name.rsplit('.', 1)
    module = __import__(module_name, fromlist=[class_name])
    model_class = getattr(module, class_name)

    ensured_directory = os.path.dirname(schema_path)
    ensure_directory_exists(ensured_directory)

    if synchronize_schema(model_class, schema_path):
        click.echo("Schema updated.")
    else:
        click.echo("Schema is already up to date.")

if __name__ == "__main__":
    sync()
```

### __init__.py

```python
from .sync import synchronize_schema
from .utilities import ensure_directory_exists
```

### Usage

With your library set up, users can easily synchronize their Pydantic model schema:

1. **Programmatically:**
    ```python
    from yourlibrary import synchronize_schema
    from yourmodels import MyModel

    synchronize_schema(MyModel, 'schema.json')
    ```

2. **Via Command Line:**
    ```sh
    pydantic-schema-sync mymodule.MyModel path/to/schema.json
