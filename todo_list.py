class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{status} {self.name}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        task = Task(task_name)
        self.tasks.append(task)

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if self.tasks:
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")
        else:
            print("No tasks.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()
    while True:
        print("\nCommand Menu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. View Tasks")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            todo_list.add_task(task_name)
        elif choice == "2":
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.complete_task(task_index)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            task_index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
