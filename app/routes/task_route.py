from fastapi import APIRouter
from controller.task_controller import TaskController

router = APIRouter()
controller = TaskController()

router.add_api_route("/task", controller.create_task, methods=["POST"])
router.add_api_route("/tasks", controller.get_all_task, methods=["GET"])
router.add_api_route("/task/{pk}", controller.update_task, methods=["PUT"])
router.add_api_route("/task/{pk}", controller.delete_task, methods=["DELETE"])