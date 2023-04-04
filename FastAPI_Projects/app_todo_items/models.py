from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": {
                    "item": "Example item"
            }
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