from typing import Union
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import json
from pydantic import BaseModel
import uvicorn
from urls import task_temp_url
from routers import tasks_router


app = FastAPI()
templats = Jinja2Templates(directory="templates")

if __name__ == '__main__':
    print('Start Server')
    uvicorn.run('main:app', port = 8000, reload=True)
    print('Server Stop')

""" uvicorn main:app --reload """ 

app.mount("/static", StopAsyncIteration(directory='static'), name='static')



class DataBase():
    def __init__(self, name_db) -> None:
        self.name_db = name_db
    
    def name_db(self):
        return self.name_db
    

    def read_db(self):
        with open(self.name_db, 'r', encoding='utf-8') as db:
            return json.load(db)
    
    def save_db(self, data):
        with open(self.name_db, 'w', encoding='utf-8') as db:
            return json.dump(data, db, ensure_ascii=False)

database = DataBase('database.json')

@app.get('/index/')
def get_index(request:Request):
    data = database.read_db()
    return templats.TemplateResponse(request=request, name='index.html', context=data)


@app.get('/list_task/')
def get_index(request:Request):
    data = database.read_db()
    return templats.TemplateResponse(request=request, name='list_task.html', context=data)



@app.get('/add_task/')
def get_index(request:Request):
    data = database.read_db()
    return templats.TemplateResponse(request=request, name='add_task.html', context=data)

class Task(BaseModel):
    title:str
    description:str



@app.post('/add_task/')
def add_task(request:Request, task:Task):
    data = database.read_db()
    new_task = {"title" : task.title, "description": task.description}
    data['tasks'].append(new_task)
    data['count_action']["task_action"] += 1
    database.save_db(data)
    return templats.TemplateResponse(request=request, name='list_task.html', context=data)
