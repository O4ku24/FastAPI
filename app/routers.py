from fastapi import APIRouter, Request
from schemas import TaskCreateSchema
from models import TaskModel
from sqlalchemy.orm import Session
from sqlalchemy import select
from database import engine

tasks_router = APIRouter(prefix='/api/v1/tasks')


@tasks_router.post(path='/create/') 
def create_task_point(request:Request, task: TaskCreateSchema):
    new_task = TaskModel(
        title = task.title,
        description = task.description,
    )

    session = Session(engine)
    session.add(new_task)
    session.commit()
    session.close()
    return {"task": task}

@tasks_router.get('/list_task/')
def list_tasks_point(request:Request):
    session = Session(engine)
    stmt = select(TaskModel)
    tasks:list = session.scalars(stmt).all()
    return tasks

@tasks_router.get('/')