import click #to create  a CLI
import json # to save and load the data from json files
import os # to check if file exists or not

TODO_FILE = "todo.json"

# loading tasks from file
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)
    

# saving tasks in files
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


# decorator from Click
@click.group()
def cli():
    """Simple todo list manager""" # DOck string
    pass

@click.command()
@click.argument("task")
def add(task):
    """Ads task into todo list"""
    tasks = load_tasks()
    tasks.append({"task":task, "done":False})
    save_tasks(tasks)
    click.echo(f"Task added successfully: {task}")


@click.command()
def list():
    """List all the task"""
    tasks = load_tasks()
    if not tasks:
        click.echo("no task found")
        return
    for index, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        click.echo(F"{index}. {task["task"]} [{status}]")


@click.command()  # Define a command called 'complete'
@click.argument("task_number", type=int)  # Accepts a task number as an integer
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()  # Load existing tasks
    if 0 < task_number <= len(tasks):  # Ensure task number is valid
        tasks[task_number - 1]["done"] = True  # Mark as done
        save_tasks(tasks)  # Save updated tasks
        click.echo(f"Task {task_number} marked as completed!")  # Print success message
    else:
        click.echo("Invalid task number.")  # Handle invalid numbers


@click.command()  # Define a command called 'remove'
@click.argument("task_number", type=int)  # Accepts a task number as an integer
def remove(task_number):
    """Remove a task from the list"""
    tasks = load_tasks()  # Load existing tasks
    if 0 < task_number <= len(tasks):  # Ensure task number is valid
        removed_task = tasks.pop(task_number - 1)  # Remove the task
        save_tasks(tasks)  # Save updated tasks
        click.echo(f"Removed task: {removed_task['task']}")  # Print removed task
    else:
        click.echo("Invalid task number.")  # Handle invalid numbers


# Add commands to the main CLI group
cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)

# If the script is run directly, start the CLI
if __name__ == "__main__":
    cli()