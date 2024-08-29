from ast import literal_eval
from contextlib import suppress
from enum import Enum
from typing import Literal

import pytest
from pydantic import DirectoryPath, validate_call
from pydantic_schema_sync import sync_schema_from_path as sync

from .config import PluginConfig
from .data_model import SchemaFieldInfo as Info


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "pydantic_schema_sync: mark test as needing Pydantic Schema Synchronisation",
    )
    global pss_ini
    pss_ini = literal_eval(config.getini("pydantic_schema_sync"))  # safe eval


def pytest_addoption(parser):
    """Add `[tool.pytest.ini_options]` section `pydantic_schema_sync` setting."""
    parser.addini(
        "pydantic_schema_sync",
        "A custom option for the pytest-pydantic-schema-sync plugin",
        default=str(PluginConfig().model_dump()),
    )


class PSSItem(pytest.Item):
    def __init__(self, name: str, parent: pytest.Collector, field: Info):
        super().__init__(name, parent)
        self.field = field
        global pss_ini
        plugin_config = PluginConfig.model_validate(pss_ini)
        self.plugin_config = plugin_config

    @validate_call
    def get_root_dir(self, root: Literal["package_root", "repo_root"]) -> DirectoryPath:
        match root:
            case "package_root":
                hint = "pyproject.toml"
            case "repo_root":
                hint = ".git"
        try:
            return next(d for d in self.path.parents if any(d.glob(hint)))
        except StopIteration:
            msg = f"Unable to find {root} (no {hint} in directories above {self.path})"
            raise FileNotFoundError(msg)

    def runtest(self):
        field = self.field
        print(f"Schema sync: {field.enum_cls}.{field.schema_stem} = {field.target}")
        config = self.plugin_config
        root_dir = self.get_root_dir(root=config.schema_location)
        if config.schema_location == "repo_root" and not config.repo_flatten:
            package_root_dir = self.get_root_dir("package_root")
            schema_dir = root_dir / config.schema_dir / package_root_dir.name
            # Note: otherwise could fall back to first part of dotted import path
        else:
            schema_dir = root_dir / config.schema_dir
        schema_path = schema_dir / f"{field.schema_stem}.json"
        sync(model=field.target, schema_path=schema_path, mjs_kwargs=config.mjs_kwargs)


class PSSCollector(pytest.Collector):
    def __init__(self, name: str, parent: pytest.Collector, obj: type[Enum]):
        super().__init__(name, parent)
        self.obj = obj

    def collect(self):
        for schema, target in self.obj.__members__.items():
            yield PSSItem.from_parent(
                self,
                name=f"{self.name}::{schema}",
                field=Info(enum_cls=self.name, schema_stem=schema, target=target.value),
            )


@pytest.hookimpl(tryfirst=True)
def pytest_pycollect_makeitem(collector, name, obj):
    with suppress(Exception):
        mark = pytest.mark.pydantic_schema_sync
        markers = vars(obj).get("pytestmark", [])
        is_marked = mark.name in [m.name for m in markers]
        assert is_marked
        assert issubclass(obj, Enum)  # Restrict the plugin to operate on Enums
        return PSSCollector.from_parent(collector, name=name, obj=obj)
