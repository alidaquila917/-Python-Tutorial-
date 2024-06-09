TASKS_FILE = "tasks.txt"

def add_task(task):
    try:
        with open(TASKS_FILE, 'a') as file:
            file.write(task + '\n')
        print("Task added successfully.")
    except IOError as e:
        print("Error adding task:", e)

def remove_completed_tasks():
    try:
        with open(TASKS_FILE, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not line.startswith("[x]"):
                    file.write(line)
            file.truncate()
        print("Completed tasks removed successfully.")
    except IOError as e:
        print("Error removing completed tasks:", e)

def view_task_list():
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = file.readlines()
            if tasks:
                print("Task List:")
                for task in tasks:
                    print(task.strip())
            else:
                print("Task list is empty.")
    except IOError as e:
        print("Error viewing task list:", e)

def save_tasks_to_file(tasks):
    try:
        with open(TASKS_FILE, 'w') as file:
            for task in tasks:
                file.write(task + '\n')
        print("Tasks saved to file.")
    except IOError as e:
        print("Error saving tasks to file:", e)

def load_tasks_from_file():
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except IOError as e:
        print("Error loading tasks from file:", e)
        return []

def main():
    while True:
        print("\n1. Add a task")
        print("2. Remove completed tasks")
        print("3. View current task list")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            remove_completed_tasks()
        elif choice == '3':
            view_task_list()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
