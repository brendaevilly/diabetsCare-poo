import tkinter as tk
from tkinter import ttk

class GlycemiaScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#F0F2F5") # Cor de fundo geral da tela

        # Frame para o conteúdo principal (branco, centralizado)
        content_frame = tk.Frame(self, bg="white")
        content_frame.pack(expand=True, fill="both", padx=50, pady=50)

        # --- Header --- #
        header_frame = tk.Frame(content_frame, bg="white")
        header_frame.pack(pady=(20, 10), padx=30, anchor="w", fill="x")

        title_label = tk.Label(header_frame, text="Registre sua glicemia", font=("Roboto", 32, "bold"), fg="#1a73e8", bg="white")
        title_label.pack(anchor="w")

        subtitle_label = tk.Label(header_frame, text="Insira seus dados de hoje", font=("Roboto", 16), fg="#1a73e8", bg="white")
        subtitle_label.pack(anchor="w")

        # --- Sliders Frame --- #
        sliders_frame = tk.Frame(content_frame, bg="white")
        sliders_frame.pack(fill="x", padx=30, pady=20)

        self.slider_data = []

        # --- Sliders --- #
        self._create_slider_row(sliders_frame, "Glicemia em jejum (mg/dL)", 65, 40, 200, "jejum")
        self._create_slider_row(sliders_frame, "Glicemia pós-prandial (após refeição)", 90, 40, 200, "pos_prandial")
        self._create_slider_row(sliders_frame, "Glicemia antes de dormir", 145, 40, 200, "dormir")

        # --- Text Area --- #
        text_frame = tk.Frame(content_frame, bg="white")
        text_frame.pack(fill="x", padx=30, pady=10, anchor="w")

        how_are_you_label = tk.Label(text_frame, text="Como você está?", font=("Arial", 14), fg="#1a73e8", bg="white")
        how_are_you_label.pack(anchor="w", pady=(0, 5))

        self.text_area = tk.Text(text_frame, height=4, font=("Arial", 12), bg="#f0f0f0", relief="solid", bd=0, highlightthickness=1, highlightbackground="#e0e0e0", wrap="word", padx=10, pady=10)
        self.text_area.insert(tk.END, "Escreva aqui...")
        self.text_area.pack(fill="x", expand=True)

        # --- Buttons Frame --- #
        button_frame = tk.Frame(content_frame, bg="white")
        button_frame.pack(pady=20)

        save_button = tk.Button(button_frame, text="Salvar", font=("Arial", 12, "bold"), bg="#1a73e8", fg="white", padx=30, pady=10, relief="flat", bd=0, highlightthickness=0, command=self._save_glycemia_data)
        save_button.pack(side="left", padx=10)

        back_button = tk.Button(button_frame, text="Voltar para Feed", font=("Arial", 12), command=lambda: controller.show_frame("FeedScreen"))
        back_button.pack(side="left", padx=10)

        # --- Abstract Shapes (no main frame, but on the GlycemiaScreen itself) ---
        # These shapes are outside the white content_frame to mimic the original image's layout
        canvas = tk.Canvas(self, width=300, height=200, bg="#F0F2F5", highlightthickness=0)
        canvas.place(relx=1.0, rely=0, anchor="ne", x=-50, y=50) # Ajustado para ficar mais próximo do canto superior direito
        canvas.create_oval(100, -100, 400, 200, fill="#1a73e8", outline="")
        canvas.create_oval(180, -50, 450, 150, fill="#1967d2", outline="")

        self._update_all_status()

    def _create_slider_row(self, parent, label_text, initial_value, min_val, max_val, type_glicemia):
        row_frame = tk.Frame(parent, bg="white")
        row_frame.pack(fill="x", pady=10)

        label = tk.Label(row_frame, text=label_text, font=("Arial", 14), fg="#1a73e8", bg="white")
        label.pack(side="left", anchor="w", expand=True)

        slider_container_frame = tk.Frame(row_frame, bg="white")
        slider_container_frame.pack(side="left", fill="x", expand=True, padx=20)

        value_label = tk.Label(slider_container_frame, text=str(initial_value), font=("Arial", 12), fg="#5f6368", bg="white")
        value_label.pack(anchor="center")

        style = ttk.Style()
        style.configure("TScale", background="white", troughcolor="#d3d3d3")

        slider = ttk.Scale(slider_container_frame, from_=min_val, to=max_val, orient="horizontal", style="TScale", command=lambda val, vl=value_label, tg=type_glicemia: self._update_value(val, vl, tg))
        slider.set(initial_value)
        slider.pack(fill="x", expand=True)

        color_tag = tk.Label(row_frame, text="", bg="gray", fg="white", font=("Arial", 10, "bold"), width=10, pady=5, relief="flat")
        color_tag.pack(side="right", padx=20)

        self.slider_data.append({
            "type": type_glicemia,
            "slider": slider,
            "value_label": value_label,
            "color_tag": color_tag
        })

    def _update_value(self, val, value_label, type_glicemia):
        value = int(float(val))
        value_label.config(text=str(value))
        self._update_status(type_glicemia, value)

    def _update_status(self, type_glicemia, value):
        status_text, status_color = "Normal", "#34a853" # Verde

        if type_glicemia == "jejum":
            if value < 70: status_text, status_color = "Baixa", "#fbbc04" # Amarelo
            elif value > 99: status_text, status_color = "Alta", "#ea4335" # Vermelho
        elif type_glicemia == "pos_prandial":
            if value < 70: status_text, status_color = "Baixa", "#fbbc04"
            elif value > 140: status_text, status_color = "Alta", "#ea4335"
        elif type_glicemia == "dormir":
            if value < 100: status_text, status_color = "Baixa", "#fbbc04"
            elif value > 140: status_text, status_color = "Alta", "#ea4335"

        for data in self.slider_data:
            if data["type"] == type_glicemia:
                data["color_tag"].config(text=status_text, bg=status_color)
                break

    def _update_all_status(self):
        for data in self.slider_data:
            value = int(data["slider"].get())
            self._update_status(data["type"], value)

    def _save_glycemia_data(self):
        data_to_save = {
            "jejum": int(self.slider_data[0]["slider"].get()),
            "pos_prandial": int(self.slider_data[1]["slider"].get()),
            "dormir": int(self.slider_data[2]["slider"].get()),
            "observacoes": self.text_area.get("1.0", "end-1c").strip()
        }
        print("Dados de Glicemia Salvos:", data_to_save)
        self.controller.show_frame("FeedScreen")
