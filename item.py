class Task:
    def __init__(self, description, priority='normal'):
        self.description = description
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.description} [{self.priority}] - {status}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority='normal'):
        task = Task(description, priority)
        self.tasks.append(task)
        print(f"Task added: {task}")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
            print(f"Task marked as completed: {self.tasks[task_index]}")
        else:
            print("Invalid task index.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"{index}: {task}")

def main():
    todo_list = TodoList()
    while True:
        print("\nTODO LIST APP")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Show Tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter priority (high/normal/low): ").lower()
            if priority not in ['high', 'normal', 'low']:
                priority = 'normal'
            todo_list.add_task(description, priority)
        elif choice == '2':
            todo_list.show_tasks()
            task_index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_task_completed(task_index)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()