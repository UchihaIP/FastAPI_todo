from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    item: str

    class Config:
        schema_extra = {
            "Example": {
                "id": 1,
                "item": "Example schema!"
            }
        }


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Watch the next series Naruto"
            }
        }