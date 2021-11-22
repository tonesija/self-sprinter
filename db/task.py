from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from db.db import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    desc = Column(String)
    progress = Column(Integer, default=0, nullable=False)

    parent_task = Column(Integer, ForeignKey("tasks.id"))
    subtasks = relationship("Task")

    def update_progress(self):
        pass
