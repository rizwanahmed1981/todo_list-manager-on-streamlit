import json
import os
import streamlit as st

TODO_FILE = "todo.json"

# FUNCTIONS

# loading tasks from file todo.json 
def load_tasks():
    try:
        if not os.path.exists(TODO_FILE):
            # Initialize file with empty array
            with open(TODO_FILE, "w") as file:
                json.dump([], file)
            return []
        
        with open(TODO_FILE, "r") as file:
            content = file.read().strip()
            if not content:  # If file is empty
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        # If JSON is invalid, reset the file
        with open(TODO_FILE, "w") as file:
            json.dump([], file)
        return []

# save tasks to todo.json file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# add task 
def add_tasks(task):
    if task.strip() == "":
        st.error("Task cannot be empty!")
        return
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)  # Pass the entire tasks list
    st.success(f"Task successfully added: {task}")

# list all tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        st.info("No tasks found!")
        return
    
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "⏳"
        st.write(f"{i}. {status} {task['task']}")

# complete a task
def complete_task(task_index):
    tasks = load_tasks()
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["done"] = True
        save_tasks(tasks)
        st.success("Task marked as complete!")
    else:
        st.error("Invalid task number!")

# delete a task
def delete_task(task_index):
    tasks = load_tasks()
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        st.success(f"Deleted task: {deleted_task['task']}")
    else:
        st.error("Invalid task number!")