from enum import Enum
from pathlib import Path

from pydantic import BaseModel, Field

__all__ = ("SchemaLocation", "PluginConfig", "get_config")


class SchemaLocation(str, Enum):
    REPO_ROOT = "repo_root"
    PACKAGE_ROOT = "package_root"


class PluginConfig(BaseModel):
    src_dir: Path = Field(Path("src"), description="Source directory")
    schema_location: SchemaLocation = Field(
        SchemaLocation.REPO_ROOT, description="Location to store schema files"
    )
    schema_dir: str = Field(
        "schemas", description="Name of the directory to store schema files"
    )
    models: dict[str, str] = Field(
        description="Dictionary of schema names to model paths"
    )


def get_config(pytestconfig) -> PluginConfig | None:
    config_dict = pytestconfig.getini("pydantic_schema_sync") or {}
    return PluginConfig(**config_dict) if config_dict else None
