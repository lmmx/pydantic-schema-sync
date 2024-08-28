from enum import Enum
from pytest import mark

@mark.pydantic_schema_sync
class SyncedSchemas(Enum):
    input = "demo_test_package.data_model.InputModel"
    output = "demo_test_package.data_model.OutputModel"
