import tkinter as tk
from tkinter import messagebox

# Função para ser chamada quando o botão for clicado
def on_button_click():
    messagebox.showinfo("Título", "Olá! Você clicou no botão.")

# Criação da janela principal
root = tk.Tk()
root.title("Minha Primeira GUI")

# Criação de um rótulo (label)
label = tk.Label(root, text="Olá, Mundo!")
label.pack(pady=10)

# Criação de um botão
button = tk.Button(root, text="Clique em mim", command=on_button_click)
button.pack(pady=10)

# Inicia o loop principal da aplicação
root.mainloop()
