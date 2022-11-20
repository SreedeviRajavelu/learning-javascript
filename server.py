from fastapi import FastAPI

app = FastAPI()

todos_dict = {1: 'learn python', 2: 'learn http'}

@app.get("/my-first-route")
def my_first_api():
    return { "message": "Hello World" }


@app.get("/todos/{todo_id}")
def todos(todo_id):
    if int(todo_id) in todos_dict.keys():
      return (todo_id, todos_dict[int(todo_id)])
    return todos_dict
