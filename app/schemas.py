from pydantic import BaseModel


class TaskCreateSchema(BaseModel):
    title:str
    description:str

class TaskSchema(BaseModel):
    title: str
    description:str
    status: bool

class TaskUpdateSchema(BaseModel):
    title: str
    description:str
    status: bool

class UserAddSchema(BaseModel):

    login: str
    password: str

class UserCreateSchema(BaseModel):

    login: str
    password: str

class UserUpdateSchema(BaseModel):

    login: str
    password: str

