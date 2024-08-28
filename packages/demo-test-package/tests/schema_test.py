from enum import Enum
from pytest import mark


@mark.pydantic_schema_sync
class SyncedSchemas(Enum):
    input = "demo_test_package.data_model.In"
    message = "demo_test_package.data_model.Message"
    output = "demo_test_package.data_model.Out"
