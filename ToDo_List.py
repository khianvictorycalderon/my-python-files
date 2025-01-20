# Initialize a dictionary to store tasks and their statuses
tasks = {}

print()
print("Run these commands to perform specific tasks:")
print("- Create <task name>\n- Remove <task name>\n- Status <task name>\n- Change <task name>, <new status>\n- Exit")
print()
print("Create = Adds new task to the list.")
print("Remove = Delete a task in the list.")
print("Status = View the current status of the task.")
print("Change = Change the status of the task (separate task name and status with a comma).")
print("Exit = Stops the loop.")

while True:
    print()
    ui = input().strip()
    command_parts = ui.split(" ", 1)
    command = command_parts[0].lower()
    task_input = command_parts[1].strip() if len(command_parts) > 1 else None

    if command == "create":
        if not task_input:
            print("Error: Please provide a task name after 'Create'.")
        elif task_input in tasks:
            print(f"Error: Task '{task_input}' already exists.")
        else:
            tasks[task_input] = "Just Created"
            print(f"Task '{task_input}' created with status 'Just Created'.")

    elif command == "remove":
        if not task_input:
            print("Error: Please provide a task name after 'Remove'.")
        elif task_input not in tasks:
            print(f"Error: Task '{task_input}' does not exist.")
        else:
            del tasks[task_input]
            print(f"Task '{task_input}' removed.")

    elif command == "status":
        if not task_input:
            print("Error: Please provide a task name after 'Status'.")
        elif task_input not in tasks:
            print(f"Error: Task '{task_input}' does not exist.")
        else:
            print(f"Status of task '{task_input}': {tasks[task_input]}")

    elif command == "change":
        if not task_input or "," not in task_input:
            print("Error: Please provide a task name and new status separated by a comma after 'Change'.")
        else:
            task_name, new_status = map(str.strip, task_input.split(",", 1))
            if task_name not in tasks:
                print(f"Error: Task '{task_name}' does not exist.")
            else:
                tasks[task_name] = new_status
                print(f"Status of task '{task_name}' changed to '{new_status}'.")

    elif command == "exit":
        print("\nThank you for using the program!")
        break

    else:
        print("Error: Invalid command. Please try again.")
