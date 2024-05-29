from sqlalchemy import delete, update
from .models import Task
from db.base import BaseService
from db import db

class TaskService(BaseService):
    model = Task

    @classmethod
    def delete_by_id(cls, model_id):
        """Remove by ID"""
        query = delete(cls.model).filter_by(id=model_id)
        result = db.session.execute(query)
        db.session.commit()
        return result.rowcount
    
    @classmethod
    def update_by_id(cls, model_id, **data):
        new_data = dict()
        for column, state in data.items():
            if state:
                new_data[column] = state
        task = update(cls.model).filter_by(id=model_id).values(new_data)
        result = db.session.execute(task)
        db.session.commit()
        return result.rowcount
