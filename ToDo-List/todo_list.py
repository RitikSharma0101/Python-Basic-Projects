from time import sleep  # Import sleep function for pause between actions

# Function to display message when no tasks are found
def no_tasks_message():
    print("No tasks found. Start adding some!")

# Function to add tasks
def add_task(number_of_task_add):
    items = []  # List to store added tasks
    for i in range(number_of_task_add):
        item = input(f"Enter task {i+1}: ").strip()  # Take task input
        if not item:  # Skip empty inputs
            print("Empty task skipped.")
            continue
        with open("data.txt", "a") as file:  # Append task to file
            file.write(item + "\n")
        items.append(item)  # Add task to list
    print("Tasks added: " + ", ".join(items))  # Show added tasks

# Function to show all tasks
def show_task():
    try:
        with open("data.txt", "r") as file:  # Read file
            data = [line.strip() for line in file.readlines()]  # Remove extra spaces/newlines
            if not data:  # If no tasks
                no_tasks_message()
                return []
            for idx, task in enumerate(data, start=1):  # Show numbered list
                print(f"{idx}. {task}")
            return data
    except FileNotFoundError:  # If file not found
        no_tasks_message()
        return []

# Function to remove a task by number
def remove_task(task_number, tasks):
    if 0 < task_number <= len(tasks):  # Validate task number
        removed_task = tasks.pop(task_number - 1)  # Remove task from list
        with open("data.txt", "w") as file:  # Overwrite file with updated list
            file.writelines(f"{task}\n" for task in tasks)
        print(f"Removed: {removed_task}")  # Show removed task
    else:
        print("Invalid task number.")

# Function to clear all tasks
def saved_all_clear():
    while True:
        confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
        if confirm == "y":  # Confirm clear
            with open("data.txt", "w") as file:
                file.write("")  # Empty the file
            print("All tasks cleared.")
            break
        elif confirm == "n":  # Cancel clear
            print("Clear cancelled.")
            break
        else:  # Invalid choice
            print("Invalid choice. Please enter 'y' or 'n'.")

# Main program loop
while True:
    # Display menu
    print("""
------ To-Do List ------
[1] Add Task
[2] Show Task
[3] Remove Task
[4] Clear All Tasks
[5] Exit
------------------------""")

    user = input("Enter the number: ").strip()  # Get user choice

    if user == "5" or user.lower() == "e":  # Exit condition
        print("Thank you for using the app!")
        break

    try:
        choice = int(user)  # Convert choice to integer
    except ValueError:
        print("Invalid choice. Please enter a number from 1 to 5.")
        continue

    # Match user choice to action
    match choice:
        case 1:  # Add task
            try:
                number_of_task = int(input("Enter the number of tasks to add: "))
                add_task(number_of_task)
            except ValueError:
                print("Enter only a number!")
        case 2:  # Show tasks
            show_task()
            sleep(1)  # Pause for 1 second
        case 3:  # Remove task
            tasks = show_task()
            if not tasks:
                continue
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number, tasks)
            except ValueError:
                print("Enter only a number!")
        case 4:  # Clear all tasks
            saved_all_clear()
        case _:  # Invalid menu option
            print("Invalid option. Try again.")
