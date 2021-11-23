from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import ForeignKey
from db.db import Base, SessionLocal, get_db


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    desc = Column(String)
    progress = Column(Integer, default=0, nullable=False)
    creation_time = Column(DateTime, default=func.now(), nullable=False)
    completion_time = Column(DateTime)

    parent_task = Column(Integer, ForeignKey("tasks.id"))
    subtasks = relationship("Task")

    def update_progress(self):
        pass

    def delete(self, db):
        db.delete(self)
        db.commit()

    @classmethod
    def create_and_save_new_task(cls, db: SessionLocal):
        new_task = Task(title="")
        db.add(new_task)
        db.commit()
        return new_task
