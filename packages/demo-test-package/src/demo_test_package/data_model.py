from pydantic import BaseModel

__all__ = ("In", "Message", "Out")


class In(BaseModel):
    greeting: str
    count: int
    skip: list[int]


class Message(BaseModel):
    text: str


class Out(BaseModel):
    messages: list[Message]
