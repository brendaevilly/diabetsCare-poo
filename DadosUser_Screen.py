import tkinter as tk
from tkinter import ttk

class UserScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Nome do Usuário")
        self.geometry("1400x1500")
        self.configure(bg="#142124")

        self._create_main_frame()
        self._create_header()
        self._create_content()

    def _create_main_frame(self):
        self.main_frame = tk.Frame(self, bg="#FFFFFF", bd=0, relief="flat")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center", width=1400, height=750)

    def _create_header(self):
        self.header_frame = tk.Frame(self.main_frame, bg="#1A73EB", height=150)
        self.header_frame.pack(fill="x", side="top")

        self.canvas = tk.Canvas(self.header_frame, width=300, height=200, bg="#1A73EB", highlightthickness=0)
        self.canvas.place(relx=1.0, rely=0, anchor="ne")
        self.canvas.create_oval(100, -100, 400, 200, fill="#FFFFFF", outline="")
        self.canvas.create_oval(180, -50, 450, 150, fill="#1A73EB", outline="")

    def _create_content(self):
        self.content_frame = tk.Frame(self.main_frame, bg="#FFFFFF")
        self.content_frame.pack(fill="both", expand=True, padx=40, pady=30)

        self.user_label = tk.Label(self.content_frame, text="Nome do usuário", font=("Arial", 25, "bold"), bg="#FFFFFF", fg="#1A73EB")
        self.user_label.pack(anchor="w", pady=(0, 5))

        self.user_entry = tk.Entry(self.content_frame, font=("Arial", 14), bg="#F5F5F5", bd=0, relief="flat", highlightthickness=0)
        self.user_entry.insert(0, "Bio")
        self.user_entry.pack(anchor="w", pady=(0, 10), ipady=70, ipadx=140)

        self.data_frame = tk.Frame(self.content_frame, bg="#FFFFFF")
        self.data_frame.pack(fill="x", pady=(14, 30))

        self._create_data_block(self.data_frame, "Em jejum", "65", "#FFC107")
        self._create_data_block(self.data_frame, "Pós-prandial", "90", "#4CAF50")
        self._create_data_block(self.data_frame, "Hora de dormir", "145", "#DC3545")

        self.dashboard_button = tk.Button(self.content_frame, text="Consultar dashboard", font=("Arial", 14, "bold"), bg="#1A73EB", fg="#FFFFFF", relief="flat", bd=0, padx=14, pady=10)
        self.dashboard_button.pack(pady=(14, 0))

    def _create_data_block(self, parent, title, value, color):
        block_frame = tk.Frame(parent, bg="#FFFFFF")
        block_frame.pack(side="left", expand=True, fill="x")

        tk.Label(block_frame, text=title, font=("Arial", 20, "bold"), bg="#FFFFFF", fg="#1A73EB").pack()
        tk.Label(block_frame, text=value, font=("Arial", 24, "bold"), bg="#FFFFFF", fg=color).pack()


if __name__ == "__main__":
    app = UserScreen()
    app.mainloop()
