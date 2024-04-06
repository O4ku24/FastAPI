from fastapi import APIRouter, Request
from schemas import TaskCreateSchema, TaskUpdateSchema
from models import TaskModel
from sqlalchemy.orm import Session
from sqlalchemy import select, insert
from database import engine

tasks_router = APIRouter(prefix='/api/tasks')


""" @tasks_router.post(path='/create/') 
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
 """


@tasks_router.get('/list_task/')
def get_list_task(request:Request):
    session = Session(engine)
    stmt = select(TaskModel)
    object_db = session.execute(stmt)
    tasks:list = object_db.scalars().all()
    session.close()
    return tasks

@tasks_router.post('/create/')
def add_task(request: Request, task: TaskCreateSchema):
    session = Session(engine)
    stmt = insert(TaskModel).values(title = task.title, description = task.description)
    session.execute(stmt)
    session.commit()
    session.close()
    return task

@tasks_router.put('/list_task/')
def update_task(request: Request, task_id: int, task_chenge: TaskUpdateSchema):
    session = Session(engine)
    stmt = select(TaskModel).where(TaskModel.id == task_id)
    object_db = session.execute(stmt)
    task = object_db.scalars().first()
    task.title = task_chenge.title
    task.description = task_chenge.description
    task.status = task_chenge.status
    session.merge(task)
    session.commit()
    session.close()
    return task_chenge

@tasks_router.delete('/delete/')
def delete_task(request: Request, task_id: int):
    session = Session(engine)
    stmt = select(TaskModel).where(TaskModel.id == task_id)
    object_db = session.execute(stmt)
    task = object_db.scalar()
    session.delete(task)
    session.commit()
    session.close()
    return {"Messege" : f"task id:{task_id} delete!"}

