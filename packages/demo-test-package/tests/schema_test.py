from enum import Enum
from pytest import mark


@mark.pydantic_schema_sync
class SyncedSchemas(Enum):
    input = "demo_test_package.data_model.In"
    output = "demo_test_package.data_model.Out"


@mark.pydantic_schema_sync
class SyncedSchemasExtra(Enum):
    extra = "demo_test_package.data_model.Extra"
    etc = "demo_test_package.data_model.Etc"
