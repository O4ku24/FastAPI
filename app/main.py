import uvicorn
from database import Model, engine
from fastapi import FastAPI
from models import TaskModel
from routers import tasks_router
from urls import task_temp_url
from routers import tasks_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="TodoList",
    version="0.0.1"
)

app.include_router(tasks_router)
app.include_router(task_temp_url)
app.mount("/static", StaticFiles(directory='static'), name='static')






if __name__ == '__main__':
    TaskModel.metadata.create_all(engine)

    print('Start Server')
    uvicorn.run('main:app', port = 8000, host='127.0.0.1', reload=True)
    print('Server Stop')