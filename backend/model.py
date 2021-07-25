from pydantic import BaseModel

class Todo(BaseModel):
    user: str
    title: str
    description: str