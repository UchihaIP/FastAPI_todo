from fastapi import Form
from pydantic import BaseModel

from typing import List, Optional


class Todo(BaseModel):
    id: Optional[int]
    item: str

    @classmethod
    def as_form(cls,
                item: str = Form(...)
                ):
        return cls(item=item)

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
            "Example": {
                "item": "Example schema!"
            }
        }


class TodoItems(BaseModel):
    item: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Rasengan!"
                    },
                    {
                        "item": "Chidori"
                    }
                ]
            }
        }
