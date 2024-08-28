from pydantic import BaseModel

__all__ = ("InputModel", "OutputModel")


class InputModel(BaseModel):
    greeting: str
    count: int
    skip: list[int]


class OutputModel(BaseModel):
    messages: list[str]
