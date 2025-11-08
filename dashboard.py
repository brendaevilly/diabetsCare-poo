import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


valores = {
    "Jejum": 91.3,
    "Pós-prandial": 136.1,
    "Antes de dormir": 120.3
}


dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
jejum = [85, 90, 100, 95, 92, 97, 93]
pos_prandial = [110, 120, 130, 125, 118, 123, 119]
antes_dormir = [115, 118, 125, 119, 116, 120, 117]


root = tk.Tk()
root.title("Dashboard de Glicemia")
root.geometry("800x600")
root.configure(bg="#f5f7fa")


titulo = tk.Label(root, text="Seu Dashboard", font=("Arial", 20, "bold"), fg="#2874f0", bg="#f5f7fa")
titulo.pack(pady=(20,5))

subtitulo = tk.Label(root, text="Acompanhe sua evolução diária da glicemia", font=("Arial", 11), bg="#f5f7fa")
subtitulo.pack(pady=(0,15))


frame_medias = tk.Frame(root, bg="white", relief="solid", bd=1)
frame_medias.pack(pady=10, anchor="center")  # centraliza


label_jejum = tk.Label(frame_medias, text="Jejum", font=("Arial", 10, "bold"), fg="#2874f0", bg="white")
label_jejum.grid(row=0, column=0, padx=40, pady=10)
valor_jejum = tk.Label(frame_medias, text=f"{valores['Jejum']} mg/dL", font=("Arial", 14, "bold"), bg="white")
valor_jejum.grid(row=1, column=0)

label_pos = tk.Label(frame_medias, text="Pós-prandial", font=("Arial", 10, "bold"), fg="#2874f0", bg="white")
label_pos.grid(row=0, column=1, padx=40, pady=10)
valor_pos = tk.Label(frame_medias, text=f"{valores['Pós-prandial']} mg/dL", font=("Arial", 14, "bold"), bg="white")
valor_pos.grid(row=1, column=1)


label_dormir = tk.Label(frame_medias, text="Antes de dormir", font=("Arial", 10, "bold"), fg="#2874f0", bg="white")
label_dormir.grid(row=0, column=2, padx=40, pady=10)
valor_dormir = tk.Label(frame_medias, text=f"{valores['Antes de dormir']} mg/dL", font=("Arial", 14, "bold"), bg="white")
valor_dormir.grid(row=1, column=2)


grafico_label = tk.Label(root, text="Gráfico de Evolução", font=("Arial", 12, "bold"), fg="#2874f0", bg="#f5f7fa")
grafico_label.pack(pady=(20,5))

fig, ax = plt.subplots(figsize=(6,3), dpi=100)
ax.plot(dias, jejum, label="Jejum", color="blue")
ax.plot(dias, pos_prandial, label="Pós-prandial", color="green")
ax.plot(dias, antes_dormir, label="Antes de Dormir", color="red")
ax.set_ylabel("mg/dL")
ax.legend()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(pady=10)

frame_botoes = tk.Frame(root, bg="#f5f7fa")
frame_botoes.pack(pady=20)

btn_voltar = tk.Button(frame_botoes, text="Voltar", font=("Arial", 11, "bold"), bg="lightgray", width=12)
btn_voltar.grid(row=0, column=0, padx=10)

btn_novo = tk.Button(frame_botoes, text="Novo Registro", font=("Arial", 11, "bold"), bg="#2874f0", fg="white", width=15)
btn_novo.grid(row=0, column=1, padx=10)

root.mainloop()
