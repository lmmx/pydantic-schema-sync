from typing import Literal

from pydantic import BaseModel, Field

__all__ = ("PluginConfig",)


class PluginConfig(BaseModel):
    schema_location: Literal["repo_root", "package_root"] = Field(
        "package_root",
        description="Location to store schema files",
    )
    schema_dir: str = Field(
        "schemas",
        description="Name of the directory to store schema files",
    )
    repo_flatten: bool = Field(
        False,
        description="Put all schemas in one directory when synced under repo root",
    )
