import sqlite3


conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'pending'
)
""")

conn.commit()

def add_task(title, description=""):
    cursor.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (title, description))
    conn.commit()

def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    return cursor.fetchall()

def update_task_status(task_id, status):
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
    conn.commit()

def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

def update_task(task_id, new_title, new_description):
    cursor.execute("UPDATE tasks SET title = ?, description = ? WHERE id = ?", (new_title, new_description, task_id))
    conn.commit()
