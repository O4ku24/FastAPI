from typing import Union
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import json
from pydantic import BaseModel
app = FastAPI()
templats = Jinja2Templates(directory="templates")


""" uvicorn main:app --reload """ 

def database(name_db, mode, data=None):
    if mode == 'r':
        with open(name_db, mode, encoding='utf-8') as db:
            return json.load(db)
    elif mode == 'w':
        with open(name_db, mode, encoding='utf-8') as db:
            return json.dump(data, db)

@app.get('/index/')
def get_index(request:Request):
    data = database('database.json', 'r')
    return templats.TemplateResponse(request=request, name='index.html', context=data)

@app.get('/create/')
def get_index(request:Request):
    data = database('database.json', 'r')
    return templats.TemplateResponse(request=request, name='create.html', context=data)

class Task(BaseModel):
    title:str
    description:str



@app.post('/create/')
def get_index(request:Request, task:Task):
    print(task)
    data = database('database.json', 'r')

    
    new_task = {"title" : task.title, "description": task.description}
    
    
    data['tasks'].append(new_task)
    print(data)
    database('database.json', 'w', data)
