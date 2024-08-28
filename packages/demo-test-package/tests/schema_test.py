from enum import Enum
from pytest import mark


@mark.pydantic_schema_sync
class SyncedSchemas(Enum):
    input = "demo_test_package.data_model.InputModel"
    output = "demo_test_package.data_model.OutputModel"


@mark.pydantic_schema_sync
class SyncedSchemasExtra(Enum):
    extra = "demo_test_package.data_model.ExtraModel"
    etc = "demo_test_package.data_model.EtcModel"

