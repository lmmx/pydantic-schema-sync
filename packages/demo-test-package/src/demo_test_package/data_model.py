from pydantic import BaseModel

__all__ = ("InputModel", "OutputModel")


class In(BaseModel):
    greeting: str
    count: int
    skip: list[int]

class Message(BaseModel):
    text: str

class Out(BaseModel):
    messages: list[Message]
