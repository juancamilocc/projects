from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from models import Todo, TodoItem, TodoItems
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/todo", tags=["Todos items"], responses={404: {"Message": "Not found"}})
templates = Jinja2Templates(directory="templates")

todo_list = []

#C
@router.post("", status_code = status.HTTP_201_CREATED)
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)) -> dict:
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list
    })

#R
@router.get("", response_model = TodoItems)
async def get_todo(request: Request) -> dict:
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list
    })

#R
@router.get("/{todo_id}")
async def get_id_todo_path(request: Request, todo_id: int = Path(title="Return item for ID", 
    description="Search item for ID")) -> dict:
    
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse("todo.html", {
                "request": request,
                "todo": todo
            })    
    raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "This ID not exists")

#U
@router.put("/{todo_id}", status_code = status.HTTP_205_RESET_CONTENT)
async def update_todo(todo_data: TodoItem, todo_id: int = Path(title="Update item", 
    description="Update item for ID")) -> dict:
    
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "Message": "Todo item update successfuly"
            }    
    raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "This item not exists")

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
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "This item not exists")

#D
@router.delete("")
async def delete_all_items() -> dict:
    todo_list.clear()
    return {
        "Message": "All items deleted"
    }