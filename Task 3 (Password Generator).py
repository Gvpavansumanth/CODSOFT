import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    generated_password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(password_length))
    password_display.config(state=tk.NORMAL)
    password_display.delete(1.0, tk.END)
    password_display.insert(tk.END, generated_password)
    password_display.config(state=tk.DISABLED)

def accept_password():
    accepted_password = password_display.get("1.0", tk.END).strip()
    if accepted_password:
        print("Accepted Password:", accepted_password)
        root.destroy()

def reset_password():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    password_display.config(state=tk.NORMAL)
    password_display.delete(1.0, tk.END)
    password_display.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Password Generator")
root.configure(bg="#f2f2f2")

main_frame = tk.Frame(root, bg="#f2f2f2")
main_frame.pack(padx=20, pady=20)

heading_label = tk.Label(main_frame, text="Password Generator App", font=("Helvetica", 16, "bold"), bg="#f2f2f2")
heading_label.grid(row=0, columnspan=2, pady=10)

username_label = tk.Label(main_frame, text=" Enter Username:", bg="#f2f2f2")
username_label.grid(row=1, column=0, sticky="w")

username_entry = tk.Entry(main_frame)
username_entry.grid(row=1, column=1, pady=5)

length_label = tk.Label(main_frame, text="Enter password length:", bg="#f2f2f2")
length_label.grid(row=2, column=0, sticky="w")

length_entry = tk.Entry(main_frame)
length_entry.grid(row=2, column=1, pady=5)

generate_button = tk.Button(main_frame, text="Generate Password", command=generate_password, bg="#4caf50", fg="white", bd=0)
generate_button.grid(row=3, columnspan=2, pady=10)

password_heading_label = tk.Label(main_frame, text="Generated Password:", font=("Helvetica", 12, "bold"), bg="#f2f2f2")
password_heading_label.grid(row=4, columnspan=2, pady=5)

password_display = tk.Text(main_frame, height=1, width=30, state=tk.DISABLED)
password_display.grid(row=5, columnspan=2, pady=5)

accept_button = tk.Button(main_frame, text="Accept", command=accept_password, bg="#007bff", fg="white", bd=0)
accept_button.grid(row=6, column=0, pady=10, padx=5, sticky="e")

reset_button = tk.Button(main_frame, text="Reset", command=reset_password, bg="#e74c3c", fg="white", bd=0)
reset_button.grid(row=6, column=1, pady=10, padx=5, sticky="w")

root.mainloop()
