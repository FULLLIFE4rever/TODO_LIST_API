from flask import Blueprint, jsonify, request
from pydantic import TypeAdapter, ValidationError
from pymysql.err import DataError
from flask_pydantic import validate
from todo.exeptions import TaskValidationError

from .services import TaskService
from .schemas import STaskInfo, STaskUpdate, STasksInfo, STaskCreate

tasks_route = Blueprint("tasks", __name__, url_prefix="/tasks")


@tasks_route.errorhandler(TaskValidationError)
def invalid_api_usage(error):
    return jsonify(error.to_dict()), error.status_code


@tasks_route.route("", methods=["GET"])
def get_tasks():
    tasks = TaskService.find_all()
    return jsonify(STasksInfo(tasks=tasks).model_dump())


@tasks_route.route("", methods=["POST"])
@validate()
def add_task(body: STaskCreate):
    task = TaskService.add(**dict(body))
    return jsonify(TypeAdapter(STaskInfo).validate_python(task, from_attributes=True).model_dump())


@tasks_route.route('/<int:model_id>', methods=["DELETE"])
def delete_task_by_id(model_id: int):
    result = TaskService.delete_by_id(model_id=model_id)
    response = jsonify({"message": "Deleted"}), 204
    if not result:
        response = jsonify({"message": "Not found"}), 404
    return response


@tasks_route.route('/<int:model_id>', methods=["GET"])
def get_task_by_id(model_id: int):
    task = TaskService.find_by_id(model_id=model_id)
    response = jsonify({"message": "Not found"}), 404
    if task:
        response = jsonify(TypeAdapter(STaskInfo).validate_python(task, from_attributes=True).model_dump()), 200
    return response

@tasks_route.route('/<int:model_id>', methods=["PUT"])
@validate()
def update_task_by_id(body: STaskUpdate, model_id: int):
    result = TaskService.update_by_id(model_id=model_id, **dict(body))
    response = jsonify({"message": "Not found"}), 404
    if result:
        task = TaskService.find_by_id(model_id=model_id)
        response = jsonify(TypeAdapter(STaskInfo).validate_python(task, from_attributes=True).model_dump()), 200
    return response