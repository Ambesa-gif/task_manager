from database import add_task, get_tasks, update_task_status, update_task, delete_task

def show_menu():
    print("\n==== Python Task Manager ====")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Update a task")
    print("4. Mark task as complete")
    print("5. Delete a task")
    print("6. Exit")

def view_tasks():
    tasks = get_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        task_id, title, description, status = task
        print(f"ID: {task_id} | Title: {title} | Description: {description} | Status: {status}")

def add_new_task():
    title = input("Enter task title: ")
    description = input("Enter task description (optional): ")
    add_task(title, description)
    print("Task added successfully!")

def update_existing_task():
    task_id = int(input("Enter task ID to update: "))
    new_title = input("Enter new title: ")
    new_description = input("Enter new description: ")
    update_task(task_id, new_title, new_description)
    print("Task updated successfully!")

def mark_task_complete():
    task_id = int(input("Enter task ID to mark as complete: "))
    update_task_status(task_id, "complete")
    print("Task marked as complete!")

def delete_existing_task():
    task_id = int(input("Enter task ID to delete: "))
    delete_task(task_id)
    print("Task deleted successfully!")

def main():
    while True:
        show_menu()
        choice = input("Select an option: ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_new_task()
        elif choice == "3":
            update_existing_task()
        elif choice == "4":
            mark_task_complete()
        elif choice == "5":
            delete_existing_task()
        elif choice == "6":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
