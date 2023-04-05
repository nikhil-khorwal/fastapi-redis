from models.task_model import Task


class TaskController:
    async def create_task(self, task:Task):
        return task.save()

    async def get_all_task(self):
        return [self.format_task(pk) for pk in Task.all_pks()]

    async def update_task(self, pk:str, task:Task):
        _task = Task.get(pk)
        _task.name = task.name
        _task.description = task.description
        return _task.save()

    async def delete_task(self, pk:str):
        return Task.delete(pk=pk)

    def format_task(self, pk:str):
        task = Task.get(pk)
        return {
            "id": task.pk,
            "name": task.name,
            "description": task.description
        }