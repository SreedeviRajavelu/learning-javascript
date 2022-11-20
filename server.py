from fastapi import FastAPI

app = FastAPI()

todos_dict = {1: 'learn python', 2: 'learn http'}

@app.get("/my-first-route")
def my_first_api():
    return { "message": "Hello World" }


@app.get("/todos/{todo_id}")
def todos(todo_id):
    # Homework
    # if todo_id is passed in the path, check if todo_id is in dictionary
    # if todo_id is not in dictionary return []
    # else return what is being returned now
    # if todo_id is not passed, return whole dict
    if int(todo_id) in todos_dict.keys():
      return (todo_id, todos_dict[int(todo_id)])
    return todos_dict
