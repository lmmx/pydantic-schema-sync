from typing import Literal

from pydantic import BaseModel, Field

__all__ = ("PluginConfig", "get_config")


class PluginConfig(BaseModel):
    schema_location: Literal["repo_root", "package_root"] = Field(
        "repo_root",
        description="Location to store schema files",
    )
    schema_dir: str = Field(
        "schemas",
        description="Name of the directory to store schema files",
    )


def get_config(pytestconfig) -> PluginConfig | None:
    config_dict = pytestconfig.getini("pydantic_schema_sync") or {}
    return PluginConfig(**config_dict)
