from fastapi import APIRouter, Path, Query
from models import Todo, TodoItem

router = APIRouter()

todo_list = []

@router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "Todo added successfuly"
    }

@router.get("/todo")
async def get_todo() -> dict:
    return {
        "todos": todo_list
    }

@router.get("/todo/{todo_id}")
async def get_id_todo_path(todo_id: int = Path(title="The ID of the todo retrieve", 
    description="Search item for ID")) -> dict:
    
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }    
    return {
        "Message": "This id no exists"
    }

@router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(title="The ID of the todo retrieve", 
    description="Update item for ID")) -> dict:
    
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item == todo_data
            print(todo.item)
            return {
                "Message": "Todo item update successfuly"
            }    
    return {
        "Message": "ID no exists, imposible update"
    }
