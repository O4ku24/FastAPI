from database import Model
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, func
import enum
import datetime



class TaskModel(Model):

    __tablename__ = 'tasks_table'

    user_id: Mapped[int] = mapped_column(ForeignKey("users_table.user_id", ondelete="CASCADE"))
    task_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    status: Mapped[bool] = mapped_column(default=False)
    create_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


class RangUser(enum.Enum):
    admin = "admin"
    redactor = "redactor"
    user = "user"

class UserModel(Model):
    __tablename__ = 'users_table'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str]
    user_password: Mapped[str]
    rang_user: Mapped[RangUser]



class TaskUser(Model):
    pass
    
    
