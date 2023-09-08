import tkinter as tk
import math

# Function to update the display
def update_display(value):
    current_text = display_var.get()
    new_text = current_text + value
    display_var.set(new_text)

# Function to perform calculations
def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

# Function to clear the display
def clear():
    display_var.set("")

# Function to perform backspace
def backspace():
    current_text = display_var.get()
    new_text = current_text[:-1]
    display_var.set(new_text)

# Function to calculate square root
def square_root():
    try:
        result = math.sqrt(float(display_var.get()))
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

# Function to calculate factorial
def factorial():
    try:
        n = int(display_var.get())
        result = math.factorial(n)
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Set the background color to black
root.configure(bg="black")

# Set the initial size of the calculator window
root.geometry("400x500")  # You can adjust the width and height as needed

# Create a variable to hold the display text
display_var = tk.StringVar()
display_var.set("")

# Create the display widget with a white background and set it to span all columns
display = tk.Entry(root, textvariable=display_var, font=('Arial', 20), justify='right', bg='white')
display.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=20, pady=20)  # Add padx and pady for margin

# Define the buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('<-', 5, 1), ('√', 5, 2), ('!', 5, 3)
]

# Create and place the buttons
for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, font=('Arial', 15), command=clear)
    elif text == '<-':
        button = tk.Button(root, text=text, font=('Arial', 15), command=backspace)
    elif text == '√':
        button = tk.Button(root, text=text, font=('Arial', 15), command=square_root)
    elif text == '=':
        button = tk.Button(root, text=text, font=('Arial', 15), command=calculate)
    elif text == '!':
        button = tk.Button(root, text=text, font=('Arial', 15), command=factorial)
    else:
        button = tk.Button(root, text=text, font=('Arial', 15), command=lambda t=text: update_display(t))
    
    button.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')

# Configure grid proportions
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the GUI event loop
root.mainloop()
