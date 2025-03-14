import streamlit as st
import json
import os
from functions import *

st.title("TODO LIST MANAGER")

# Add task section
task = st.text_input("Add a task here: ")
if st.button("Add Task"):
    add_tasks(task)



# Complete task section
tasks = load_tasks()
if tasks:
    task_numbers = list(range(1, len(tasks) + 1))
    complete_index = st.selectbox("Select task number to mark as complete:", task_numbers)
    if st.button("Complete Task"):
        complete_task(complete_index)
        st.rerun()

    # Delete task section
    delete_index = st.selectbox("Select task number to delete:", task_numbers)
    if st.button("Delete Task"):
        delete_task(delete_index)
        st.rerun()



# Display all tasks
st.subheader("Your Tasks")
list_tasks()