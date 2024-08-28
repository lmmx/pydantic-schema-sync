import pytest
from contextlib import suppress
from enum import Enum

from .config import PluginConfig
from .data_model import SchemaFieldInfo as Info
from pydantic_schema_sync import sync_schema_from_path as sync


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "pydantic_schema_sync: mark test as needing Pydantic Schema Synchronisation",
    )


class PSSItem(pytest.Item):
    def __init__(self, name: str, parent: pytest.Collector, field: Info):
        super().__init__(name, parent)
        self.field = field
        self.plugin_config = PluginConfig()

    def runtest(self):
        field = self.field
        print(f"Schema sync: {field.enum_cls}.{field.schema_stem} = {field.target}")
        config = self.plugin_config
        match config.schema_location:
            case "package_root":
                hint = ".git"
            case "repo_root":
                hint = "pyproject.toml"
        try:
            root_dir = next(p for p in self.path.parents if any(p.glob(hint)))
        except StopIteration:
            msg = f"Unable to find {config.schema_location} via {hint} above {__file__}"
            raise FileNotFoundError(msg)
        else:
            schema_path = root_dir / config.schema_dir / f"{field.schema_stem}.json"
            sync(model=field.target, schema_path=schema_path)


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
