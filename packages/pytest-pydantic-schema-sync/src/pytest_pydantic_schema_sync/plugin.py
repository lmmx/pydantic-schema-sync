import pytest
from contextlib import suppress
from enum import Enum


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "pydantic_schema_sync: mark test as needing pydantic schema synchronization",
    )


class PydanticSchemaSyncItem(pytest.Item):
    def runtest(self):
        print(f"Running pydantic schema sync for: {self.name}")


@pytest.hookimpl(tryfirst=True)
def pytest_pycollect_makeitem(collector, name, obj):
    with suppress(Exception):
        mark = pytest.mark.pydantic_schema_sync
        markers = vars(obj).get("pytestmark", [])
        is_marked = mark.name in [m.name for m in markers]
        assert is_marked
        assert issubclass(obj, Enum)  # Restrict the plugin to operate on Enums
        return PydanticSchemaSyncItem.from_parent(collector, name=name)
