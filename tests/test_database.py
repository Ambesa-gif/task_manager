import os 
import database


TEST_DB = "test_tasks.db"

def setup_module(module):
    database.create_table(TEST_DB)

def teardown_module(module):
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

def test_add_task():
    database.add_task("Test Task", TEST_DB)
    tasks = database.get_tasks(TEST_DB)
    assert len(tasks) == 1
    assert tasks[0][1] == "Test Task"

def test_complete_task():
    task_id = database.get_tasks(TEST_DB)[0][0]
    database.complete_task(task_id, TEST_DB)
    task = database.get_tasks(TEST_DB)[0]
    assert task[3] == "complete"

def test_delete_task():
    task_id = database.get_tasks(TEST_DB)[0][0]
    database.delete_task(task_id, TEST_DB)
    tasks = database.get_tasks(TEST_DB)
    assert len(tasks) == 0

def test_update_task():
    database.add_task("Old title", TEST_DB)
    task_id = database.get_tasks(TEST_DB)[0][0]

    database.update_task(task_id, "New title", "Updated description", TEST_DB)
    task = database.get_tasks(TEST_DB)[0]

    assert task[1] == "New title"
    assert task[2] == "Updated description"