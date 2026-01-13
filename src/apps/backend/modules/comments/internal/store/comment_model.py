from sqlalchemy import Column, Integer, String, ForeignKey
from apps.backend.modules.application.base_model import BaseModel


class Comment(BaseModel):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    content = Column(String, nullable=False)
