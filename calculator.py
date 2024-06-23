import tkinter as tk
from tkinter import messagebox

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
        else:
            messagebox.showerror("Error", "Invalid operation")
            return

        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

# Set up the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place widgets
tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Number 2:").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Operation:").grid(row=2, column=0, padx=10, pady=10)
operation_var = tk.StringVar(root)
operation_var.set('+')
operation_menu = tk.OptionMenu(root, operation_var, '+', '-', '*', '/')
operation_menu.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, columnspan=2, pady=10)

# Run the application
root.mainloop()