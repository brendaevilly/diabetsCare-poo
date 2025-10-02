import tkinter as tk
from tkinter import ttk

class PostScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#E0F2F7")

        main_frame = tk.Frame(self, bg="#E0F2F7")
        main_frame.pack(expand=True)

        post_card = tk.Frame(main_frame, bg="white", bd=1, relief="solid")
        post_card.pack(padx=20, pady=20)

        self.post_text = tk.Text(post_card, height=10, width=50, font=("Arial", 12), relief="flat")
        self.post_text.pack(padx=10, pady=10)
        self.post_text.insert("1.0", "No que está pensando?")
        self.post_text.config(fg="grey")
        self.post_text.bind("<FocusIn>", self.on_entry_click)
        self.post_text.bind("<FocusOut>", self.on_focusout)

        separator = ttk.Separator(post_card, orient="horizontal")
        separator.pack(fill="x", padx=10, pady=5)

        button_frame = tk.Frame(post_card, bg="white")
        button_frame.pack(pady=10)

        cancel_button = tk.Button(button_frame, text="Cancelar", bg="#e74c3c", fg="white", font=("Arial", 12, "bold"), relief="flat", command=self.cancel)
        cancel_button.pack(side="left", padx=10)

        post_button = tk.Button(button_frame, text="Postar", bg="#2ecc71", fg="white", font=("Arial", 12, "bold"), relief="flat", command=self.post)
        post_button.pack(side="left", padx=10)

    def on_entry_click(self, event):
        if self.post_text.get("1.0", "end-1c") == "No que está pensando?":
           self.post_text.delete("1.0", "end")
           self.post_text.config(fg = "black")

    def on_focusout(self, event):
        if self.post_text.get("1.0", "end-1c") == "":
            self.post_text.insert("1.0", "No que está pensando?")
            self.post_text.config(fg = "grey")

    def post(self):
        content = self.post_text.get("1.0", "end-1c")
        if content and content != "No que está pensando?":
            self.controller.add_post(content)
            self.post_text.delete("1.0", "end")
            self.on_focusout(None) # Reset placeholder
            self.controller.show_frame("FeedScreen")

    def cancel(self):
        self.post_text.delete("1.0", "end")
        self.on_focusout(None) # Reset placeholder
        self.controller.show_frame("FeedScreen")
