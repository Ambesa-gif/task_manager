from database import add_task, get_tasks, update_task_status, delete_task

# Add a task
add_task("Finish Python task manager", "Start building the project step by step")

# Fetch and print tasks
tasks = get_tasks()
print(tasks)

# Mark task complete
update_task_status(1, "complete")

# Fetch again
tasks = get_tasks()
print(tasks)

# Delete task
delete_task(1)
tasks = get_tasks()
print(tasks)
