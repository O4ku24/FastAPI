import uvicorn
from database import  engine
from fastapi import FastAPI
from models import  UserModel, TaskModel
from routers import router
from urls import task_temp_url

from fastapi.staticfiles import StaticFiles


app = FastAPI(
    title="TodoList",
    version="0.0.1"
)

app.include_router(router)
app.include_router(task_temp_url)
app.mount("/static", StaticFiles(directory='static'), name='static')






if __name__ == '__main__':
    TaskModel.metadata.create_all(engine)
    UserModel.metadata.create_all(engine)
    print('Start Server')
    uvicorn.run('main:app', port = 8000, host='127.0.0.1', reload=True)
    print('Server Stop')