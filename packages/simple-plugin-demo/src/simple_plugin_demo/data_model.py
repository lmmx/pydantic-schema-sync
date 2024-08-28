from pydantic import BaseModel, Field

__all__ = ("In", "Message", "Out")


class In(BaseModel):
    greeting: str
    count: int
    skip: list[int]


class Message(BaseModel):
    content: str = Field(alias="text")


class Out(BaseModel):
    messages: list[Message]
