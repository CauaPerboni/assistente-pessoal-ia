class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Tarefa adicionada: {task}")

    def list_tasks(self):
        if not self.tasks:
            print("Nenhuma tarefa cadastrada.")
        else:
            for idx, task in enumerate(self.tasks):
                print(f"{idx + 1}. {task}")

    def remove_task(self, task_id):
        if 0 < task_id <= len(self.tasks):
            removed = self.tasks.pop(task_id - 1)
            print(f"Tarefa removida: {removed}")
        else:
            print("ID inválido.")
