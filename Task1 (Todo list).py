import tkinter as tk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("600x400")
        self.root.configure(bg="#f2f2f2")

        self.task_list = []
        self.editing_index = None
        self.editing_mode = False

        # Title Label
        title_label = tk.Label(self.root, text="To-Do List App", font=("Helvetica", 18, "bold"), bg="#ff5733", fg="white")
        title_label.pack(fill=tk.X, padx=20, pady=10)

        # Input Frame
        input_frame = tk.Frame(self.root, bg="#f2f2f2", highlightbackground="#dcdcdc", highlightthickness=1)  # Add outline to the input frame
        input_frame.pack(padx=20, pady=(0, 10), fill=tk.X)

        task_label = tk.Label(input_frame, text="Task", font=("Helvetica", 12, "bold"), bg="#f2f2f2")
        task_label.pack(side=tk.LEFT, padx=(0, 10))

        self.task_entry = tk.Entry(input_frame, font=("Helvetica", 12), bd=0, highlightbackground="#dcdcdc", highlightthickness=1)  # Add outline to the input box
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.action_button = tk.Button(input_frame, text="Add Task", command=self.toggle_action, font=("Helvetica", 12), bg="#4caf50", fg="white", bd=0)
        self.action_button.pack(side=tk.LEFT, padx=(10, 0))

        # Listbox and Buttons Frame
        listbox_buttons_frame = tk.Frame(self.root, bg="#f2f2f2", highlightbackground="#dcdcdc", highlightthickness=1)  # Add outline to the frame
        listbox_buttons_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        listbox_frame = tk.Frame(listbox_buttons_frame, bg="#f2f2f2")
        listbox_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        list_label = tk.Label(listbox_frame, text="Task List", font=("Helvetica", 12, "bold"), bg="#f2f2f2")
        list_label.pack(pady=(0, 5), anchor="w")

        self.tasks_listbox = tk.Listbox(listbox_frame, font=("Helvetica", 12), selectmode=tk.SINGLE, bd=0, highlightbackground="#dcdcdc", highlightthickness=1)  # Add outline to the listbox
        self.tasks_listbox.pack(fill=tk.BOTH, expand=True)

        button_frame = tk.Frame(listbox_buttons_frame, bg="#f2f2f2")
        button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(10, 0), anchor="n")

        edit_button = tk.Button(button_frame, text="Edit Task", command=self.edit_task, font=("Helvetica", 12), bg="#007bff", fg="white", bd=0, anchor="center", width=10)
        edit_button.pack(fill=tk.X, pady=(100, 10))

        delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task, font=("Helvetica", 12), bg="#e74c3c", fg="white", bd=0, anchor="center", width=10)
        delete_button.pack(fill=tk.X, pady=(10, 10))


    def toggle_action(self):
        if not self.editing_mode:
            self.add_task()
        else:
            self.submit_task()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)

    def submit_task(self):
        task = self.task_entry.get()
        if task:
            if self.editing_index is not None:
                self.task_list[self.editing_index] = task
                self.editing_index = None
                self.editing_mode = False
                self.action_button.config(text="Add Task")
                self.task_entry.delete(0, tk.END)
                self.update_listbox()

    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.task_list:
            self.tasks_listbox.insert(tk.END, task)

    def edit_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            self.editing_index = selected_index
            current_task = self.task_list[selected_index]
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(tk.END, current_task)
            self.editing_mode = True
            self.action_button.config(text="Submit")

    def delete_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            del self.task_list[selected_index]
            self.update_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#f2f2f2")
    app = ToDoListApp(root)
    root.mainloop()


    # ... (Rest of your methods)

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#ffecb3")
    app = ToDoListApp(root)
    root.mainloop()
