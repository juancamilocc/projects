from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form

class Todo(BaseModel):
    id: Optional[int]
    item: str

    @classmethod
    def as_form(
        cls,
        item: str = Form(...)
    ):
        return cls(item=item)


    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Example item"
            } 
        }
        
class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Read next chapter book"
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "todos": [
                {
                    "item": "Example schema 1"
                },
                {
                    "item": "Example schema 2"
                }
            ]
        }