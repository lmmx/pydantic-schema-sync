import pytest
from contextlib import suppress
from enum import Enum
from pydantic import BaseModel


class SchemaFieldInfo(BaseModel):
    enum_name: str
    field_name: str
    field_value: str


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "pydantic_schema_sync: mark test as needing pydantic schema synchronization",
    )


class PydanticSchemaSyncItem(pytest.Item):
    def __init__(
        self,
        name: str,
        parent: pytest.Collector,
        field_info: SchemaFieldInfo,
    ):
        super().__init__(name, parent)
        self.field_info = field_info

    def runtest(self):
        print(
            f"Syncing schema: {self.field_info.enum_name}.{self.field_info.field_name} = {self.field_info.field_value}",
        )


class PydanticSchemaSyncCollector(pytest.Collector):
    def __init__(self, name: str, parent: pytest.Collector, obj: type[Enum]):
        super().__init__(name, parent)
        self.obj = obj

    def collect(self):
        for field_name, field_value in self.obj.__members__.items():
            field_info = SchemaFieldInfo(
                enum_name=self.name,
                field_name=field_name,
                field_value=field_value.value,
            )
            yield PydanticSchemaSyncItem.from_parent(
                self,
                name=f"{self.name}::{field_name}",
                field_info=field_info,
            )


@pytest.hookimpl(tryfirst=True)
def pytest_pycollect_makeitem(collector, name, obj):
    with suppress(Exception):
        mark = pytest.mark.pydantic_schema_sync
        markers = vars(obj).get("pytestmark", [])
        is_marked = mark.name in [m.name for m in markers]
        assert is_marked
        assert issubclass(obj, Enum)  # Restrict the plugin to operate on Enums
        return PydanticSchemaSyncCollector.from_parent(collector, name=name, obj=obj)
