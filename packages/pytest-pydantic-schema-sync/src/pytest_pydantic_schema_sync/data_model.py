from pydantic import BaseModel

__all__ = ("SchemaFieldInfo",)

class SchemaFieldInfo(BaseModel):
    enum_name: str
    field_name: str
    field_value: str
