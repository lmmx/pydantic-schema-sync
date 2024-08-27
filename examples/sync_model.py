from pydantic import BaseModel, Field
from pydantic_schema_sync import sync_schema


class FooModel(BaseModel):
    foo: int = Field(1, alias="bar")


# Using field alias (default)
sync_schema(model=FooModel, schema_path="FooModel_1.json")

# Unaliased field
sync_schema(
    model=FooModel, schema_path="FooModel_2.json", mjs_kwargs={"by_alias": False}
)
