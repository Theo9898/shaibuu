class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print(f"Task '{task}' not found in the todo list.")

    def display_tasks(self):
        if self.tasks:
            print("Todo List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Todo List is empty.")

# Example usage:
todo_list = TodoList()
todo_list.add_task("Complete programming assignment")
todo_list.add_task("Read a chapter of a book")
todo_list.add_task("Go for a run")

todo_list.display_tasks()

todo_list.remove_task("Read a chapter of a book")

todo_list.display_tasks()

