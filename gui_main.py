import tkinter as tk
from tkinter import messagebox
from main import load_tasks, save_tasks

def refresh_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

def add_task():
    new_task = task_entry.get()
    if new_task.strip():
        tasks.append(new_task)
        save_tasks(tasks)
        refresh_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        refresh_task_list()
        messagebox.showinfo("Task Removed", f"Removed: {removed_task}")
    else:
        messagebox.showwarning("Selection Error", "No task selected!")

# Load tasks from the file
tasks = load_tasks()

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Task list display
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Entry field for new tasks
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Populate the task list initially
refresh_task_list()

# Run the application
root.mainloop()
