import pytest
from pathlib import Path
from pydantic_schema_sync import sync_schema_from_path
from .config import get_config, SchemaLocation

def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "pydantic_schema_sync: mark test to run pydantic schema synchronization",
    )

def pytest_collect_file(parent, path):
    if path.ext == ".py" and path.basename.startswith("test_"):
        return PydanticSchemaSyncFile.from_parent(parent, fspath=path)

class PydanticSchemaSyncFile(pytest.File):
    def collect(self):
        for name in self.config.pluginmanager.get_plugin("pydantic_schema_sync").models:
            yield PydanticSchemaSyncItem.from_parent(self, name=name)

class PydanticSchemaSyncItem(pytest.Item):
    def runtest(self):
        config = get_config(self.config)
        if not config:
            pytest.skip("Pydantic Schema Sync config not found")

        model_path = config.models[self.name]
        package_name = model_path.split('.')[0]

        if config.schema_location == SchemaLocation.REPO_ROOT:
            schema_dir = Path(self.config.rootdir) / config.schema_dir / package_name
        else:
            schema_dir = Path(self.config.rootdir) / config.src_dir / package_name / config.schema_dir

        schema_dir.mkdir(parents=True, exist_ok=True)
        schema_path = schema_dir / f"{self.name}.json"

        sync_schema_from_path(
            model=model_path,
            schema_path=schema_path,
            mjs_kwargs={"by_alias": False}
        )

    def reportinfo(self):
        return self.fspath, 0, f"pydantic_schema_sync: {self.name}"

@pytest.hookimpl(tryfirst=True)
def pytest_pycollect_makeitem(collector, name, obj):
    if pytest.mark.pydantic_schema_sync.name in getattr(obj, "pytestmark", []):
        return PydanticSchemaSyncItem.from_parent(collector, name=name)