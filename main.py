from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()
fake_db = []

class Todo(BaseModel):
    title: str
    description:Optional[str]= None
    completed:bool = False

@app.get("/")
def read():
   return {"Hoşgeldiniz"}

@app.post("/todos")
def create_todo(todo:Todo):
 fake_db.append(todo)
 return {"mesaj": "Görev başarıyla eklendi!", "veri": todo}

@app.get("/todos")
def get_todos():
   return fake_db

@app.put("/todos/{index}")
def update_todos(index:int,todo:Todo):
   if index < len(fake_db):
      fake_db[index] = todo
      return {"mesaj": "Görev başarıyla güncellendi!", "veri": todo}
   return {"hata": "Bu sırada bir görev bulunamadı!"}

@app.delete("/todos/{index}")
def delete_todos(index:int,todo:Todo):
   if index < len(fake_db):
      fake_db.pop(index)
      return {"Silindi"}

@app.get("/todos/{index}")
def readtodos(index:int):
   if index < len(fake_db):
      return fake_db[index]            