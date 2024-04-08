from database import Model
from sqlalchemy.orm import Mapped, mapped_column

class TaskModel(Model):

    __tablename__ = 'tasks_table'

    user_id: Mapped[int]
    task_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    status: Mapped[bool] = mapped_column(default=False)

    
"""     def __repr__(self) -> str:
        return f"Task title='{self.title}'" """
    

class UserModel(Model):
    __tablename__ = 'users_table'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str]
    user_password: Mapped[str]
    user_tasks = {
        "task_id": [int],
        "title": [str],
        "description": [str],
        "status": [bool],
    }
    
    
