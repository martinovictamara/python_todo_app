from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todo_items = []

class Item(BaseModel):
    id: int
    name:str
    done: bool

item1 = Item(id="1",name="milk",done = False)
todo_items.append(item1)

@app.get("/get_items/")
def get_items():
    return todo_items


@app.post("/create_item/")
def create_item(item: Item  ):
    
    todo_items.append(item)
    return item


@app.delete("/delete_item{id}")
def delete_item(id: int):
    for item in todo_items:
        if (id == item.id):
            todo_items.remove(item)
            break
    

@app.put("/update_item{id}")
def update_item(id: int,name: str):
    for item in todo_items:
        if(id==item.id):
            item.name=name
            break

@app.put("/mark_as_done{id}")
def mark_as_done(id: int):
    for item in todo_items:
        if(id == item.id):
            if(item.done==False): 
                item.done = True
                break
            else:
                item.done = False 
                break

