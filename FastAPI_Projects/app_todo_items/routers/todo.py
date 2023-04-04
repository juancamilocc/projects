from fastapi import APIRouter, Path
from models import Todo, TodoItem

router = APIRouter(prefix="/todo", tags=["Todos items"], responses={404: {"Message": "Not found"}})

todo_list = []

#C
@router.post("")
async def add_todo(todo: Todo) -> dict:
    try:
        todo_list.append(todo)
        return {
            "Message": "Todo added successfuly"
        }
    except IndexError:
        return {
            "Message": "Not allowed"
        }
    

#R
@router.get("")
async def get_todo() -> dict:
    return {
        "todos": todo_list
    }

#R
@router.get("/{todo_id}")
async def get_id_todo_path(todo_id: int = Path(title="Return item for ID", 
    description="Search item for ID")) -> dict:
    
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }    
    return {
        "Message": "This id no exists"
    }

#U
@router.put("/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(title="Update item", 
    description="Update item for ID")) -> dict:
    
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "Message": "Todo item update successfuly"
            }    
    return {
        "Message": "ID no exists, imposible update"
    }

#D
@router.delete("/{todo_id}")
async def delete_item(todo_id: int = Path(title="Delete an item", 
    description="Delete specific item")) -> dict:

    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "Message": "The item with ID:"+str(todo.id)+" ,deleted successfuly"
            }
    return {
        "Message": "The ID no exitsts, imposible delete item"
    }

#D
@router.delete("")
async def delete_all_items() -> dict:
    todo_list.clear()
    return {
        "Message": "All items deleted"
    }