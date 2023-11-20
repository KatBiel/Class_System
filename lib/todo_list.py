class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, todo):
        self.tasks.append(todo)

    def incomplete(self):
        incomplete_tasks = []
        for task in self.tasks:
            if task.complete == False:
                incomplete_tasks.append(task)
        return incomplete_tasks
    # return [task for task in self.tasks if not task.complete]

    def complete(self):
        complete_tasks = []
        for task in self.tasks:
            if task.complete == True:
                complete_tasks.append(task)
        return complete_tasks
    # return [task for task in self.tasks if task.complete]


    def give_up(self):
        for task in self.tasks:
            task.mark_complete()
