from typing import Union
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()
templats = Jinja2Templates(directory="app/templates")


""" uvicorn main:app --reload """

@app.get('/')
def index(request: Request):
    return templats.TemplateResponse("index.html", {"request":request})
    


@app.get('/home/')
def temp(request: Request):

    return {'IP':request.client[0],
            'Port':request.client[1],
            }

@app.get('/regestrator/')
def reg(request: Request):
    return templats.TemplateResponse("reg.html", {"request":request})




