from database.database import db
from models.Todo import Todo
from controlers.get_todos import get_todos

def create_todo():
    body = request.json
    new_todo = Todo(
        label=body["label"],
        done=body["done"]
    )
    db.session.add(new_todo)
    db.session.commit()
    todos = get_todos()
    return todos


        
    