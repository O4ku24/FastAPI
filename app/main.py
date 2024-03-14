from typing import Union
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()
templats = Jinja2Templates(directory="templates")


""" uvicorn main:app --reload """

@app.get('/')
def task_list(request: Request):
    context = {}
    with open('database.json', 'r', encoding='utf-8') as db:
        db:dict = json.load(db)
        context = db
        print(context)
    return templats.TemplateResponse(request=request, name='index.html', context=context)


@app.get('/users/')
def get_user(request:Request):
    with open('database.json', 'r', encoding='utf-8') as db:
        db:dict = json.load(db)
        context = db
    return templats.TemplateResponse(request=request, name='users.html', context=context)

@app.get('/create/')
def create_task(request:Request):
    return templats.TemplateResponse(request=request, name='create.html')    


@app.post('/create/')
def create_task(request:Request, task:str = Form(...)):
    print(task)
    return templats.TemplateResponse(request=request, name='create.html')   