import tkinter as tk
from tkinter import messagebox

# Function to add a new task to the list
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete the selected task from the list
def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        task_listbox.delete(task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task.")

# Function to clear all tasks from the list
def clear_tasks():
    task_listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")

# Create the GUI components
frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=30)
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks)
clear_button.pack(side=tk.RIGHT, padx=10)

# Run the application
root.mainloop()