import sqlite3

import database


def connect(db_name="task.db"):
    return sqlite3.connect(db_name)

def create_table(db_name="table.db"):
    conn = connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'incomplete'
    )
    """)

    conn.commit()
    conn.close()

def add_task(title, db_name="tasks.db"):
    conn = connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()

def get_tasks(db_name="tasks.db"):
    conn = connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks


def update_task_status(task_id, status, db_name="tasks.db"):
    conn = connect(db_name)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET status = ? WHERE id = ?",
        (status, task_id)
    )
    conn.commit()
    conn.close()


def delete_task(task_id, db_name="tasks.db"):
    conn = connect(db_name)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def update_task(task_id, new_title, new_description, db_name="tasks.db"):
    conn = connect(db_name)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET title = ?, description = ? WHERE id = ?",
        (new_title, new_description, task_id)
    )
    conn.commit()
    conn.close()

def complete_task(task_id, db_name="tasks.db"):
    update_task_status(task_id, "complete", db_name)

