def show_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            if tasks:
                print("Your Tasks:")
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task.strip()}")
            else:
                print("No tasks at the moment.")
    except FileNotFoundError:
        print("No tasks at the moment.")

def add_task(task):
    with open('tasks.txt', 'a') as file:
        file.write(task + "\n")
    print("Task added!")

def remove_task(task_number):
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
        with open('tasks.txt', 'w') as file:
            for index, task in enumerate(tasks):
                if index != (task_number - 1):
                    file.write(task)
        print("Task removed!")
    except FileNotFoundError:
        print("No tasks to remove.")

while True:
    print("\nWelcome to the To-Do List App!")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '3':
        show_tasks()
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    elif choice == '4':
        print("Thank you for using the To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
