import tkinter as tk
from tkinter import ttk

def create_app():
    root = tk.Tk()
    root.title("Registro de Glicemia")
    root.geometry("2000x1500") # Abre a janela em tela cheia
    root.configure(bg="#FFFFFF")

    # --- Header --- #
    header_frame = tk.Frame(root, bg="#FFFFFF")
    header_frame.pack(pady=(40, 20), padx=50, anchor="w")

    title_label = tk.Label(header_frame, text="Registre sua glicemia", font=("Roboto", 60, "bold"), fg="#1a73e8", bg="#FFFFFF")
    title_label.pack(anchor="w")

    subtitle_label = tk.Label(header_frame, text="Insira seus dados de hoje", font=("Roboto", 20), fg="#1a73e8", bg="#FFFFFF")
    subtitle_label.pack(anchor="w")

    # --- Sliders Frame --- #
    sliders_frame = tk.Frame(root, bg="#FFFFFF")
    sliders_frame.pack(fill="x", padx=50, pady=10)

    def create_slider_row(parent, label_text, initial_value, min_val, max_val, color_tag_text, color_tag_bg):
        row_frame = tk.Frame(parent, bg="#FFFFFF")
        row_frame.pack(fill="x", pady=15)

        label = tk.Label(row_frame, text=label_text, font=("Arial", 14), fg="#1a73e8", bg="#FFFFFF")
        label.pack(side="left", anchor="w")

        slider_container_frame = tk.Frame(row_frame, bg="#FFFFFF")
        slider_container_frame.pack(side="left", fill="x", expand=True, padx=20)

        value_label = tk.Label(slider_container_frame, text=str(initial_value), font=("Arial", 12), fg="#5f6368", bg="#FFFFFF")
        value_label.pack(anchor="center")

        # Custom style for the slider
        style = ttk.Style()
        style.configure("TScale", background="#FFFFFF", troughcolor="#d3d3d3", sliderthickness=20)
        style.map("TScale", background=[("active", "#FFFFFF")])

        slider = ttk.Scale(slider_container_frame, from_=min_val, to=max_val, orient="horizontal", length=400, style="TScale")
        slider.set(initial_value)
        slider.pack(fill="x", expand=True)

        def update_value(event):
            value_label.config(text=str(int(slider.get())))
        slider.bind("<B1-Motion>", update_value)
        slider.bind("<ButtonRelease-1>", update_value)

        color_tag = tk.Label(row_frame, text=color_tag_text, bg=color_tag_bg, fg="white", font=("Arial", 10, "bold"), padx=20, pady=5, relief="flat", borderwidth=0)
        color_tag.pack(side="right", padx=20)

        return slider, value_label

    # --- Sliders --- #
    create_slider_row(sliders_frame, "Glicemia em jejum (mg/dL)", 65, 40, 200, "Baixa", "#fbbc04")
    create_slider_row(sliders_frame, "Glicemia pós-prandial (após refeição)", 90, 40, 200, "Normal", "#34a853")
    create_slider_row(sliders_frame, "Glicemia antes de dormir", 145, 40, 200, "Alta", "#ea4335")

    # --- Text Area --- #
    text_frame = tk.Frame(root, bg="#FFFFFF")
    text_frame.pack(fill="x", padx=50, pady=20, anchor="w")

    how_are_you_label = tk.Label(text_frame, text="Como você está?", font=("Arial", 14), fg="#1a73e8", bg="#FFFFFF")
    how_are_you_label.pack(anchor="w", pady=(0, 10))

    text_area = tk.Text(text_frame, height=5, font=("Arial", 12), bg="#f0f0f0", relief="solid", bd=0, highlightthickness=1, highlightbackground="#e0e0e0", wrap="word", padx=10, pady=10)
    text_area.insert(tk.END, "Escreva aqui...")
    text_area.pack(fill="x", expand=True)

    # --- Save Button --- #
    save_button = tk.Button(root, text="Salvar", font=("Arial", 14, "bold"), bg="#1a73e8", fg="white", padx=40, pady=15, relief="flat", bd=0, highlightthickness=0)
    save_button.pack(pady=30)

    # --- Abstract Shapes --- #
    canvas = tk.Canvas(root, width=300, height=200, bg="#FFFFFF", highlightthickness=0)
    canvas.place(relx=1.0, rely=0, anchor="ne")
    canvas.create_oval(100, -100, 400, 200, fill="#1a73e8", outline="")
    canvas.create_oval(180, -50, 450, 150, fill="#1967d2", outline="")

    root.mainloop()

if __name__ == "__main__":
    create_app()
