from enum import Enum

from pytest import mark


@mark.pydantic_schema_sync
class SyncedSchemas(Enum):
    input = "simple_plugin_demo.data_model.In"
    message = "simple_plugin_demo.data_model.Message"
    output = "simple_plugin_demo.data_model.Out"
