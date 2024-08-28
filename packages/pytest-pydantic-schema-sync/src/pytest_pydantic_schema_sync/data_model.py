from pydantic import BaseModel, Field

__all__ = ("SchemaFieldInfo",)


class SchemaFieldInfo(BaseModel):
    enum_cls: str = Field(description="Name of the test module enum it came from")
    schema_stem: str = Field(description="Filename stem for the saved JSON schema")
    target: str = Field(description="Dotted import path to the target Pydantic model")
