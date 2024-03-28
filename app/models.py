from database import Model
from sqlalchemy.orm import Mapped, mapped_column

class TaskModel(Model):

    __tablename__ = 'tasks_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    status: Mapped[bool] = mapped_column(default=False)

    
    def __repr__(self) -> str:
        return f"Task title='{self.title}'"
    
class UserModel(Model):
    __tablename__ = 'user_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    password: Mapped[str]



