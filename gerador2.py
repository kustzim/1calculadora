import random
import string
import csv
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title("Senhas yey")
root.geometry("400x400")

notebook = ttk.Notebook(root)

frame1 = tk.Frame(notebook)
frame2 = tk.Frame(notebook)

notebook.add(frame1, text="Nueva senha")
notebook.add(frame2, text="Senhas salvas")

notebook.pack()

label = tk.Label(root, text="Olá, é aqui que você passará a guardar suas senhas.")
label.pack()


def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

def quantidade_caracteres():
    quatidade_caracteres = caracteres_entry.get()
    descricao = descricao_entry.get()
    if quatidade_caracteres.isdigit():
        quatidade_caracteres = int(quatidade_caracteres)
        senha = gerar_senha(quatidade_caracteres)
        with open("senhas.csv", "a", newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([senha, descricao])
        exibir_senhas()
    else:
        resultado_label = tk.Label(frame1, text="Por favor, digite um número válido")
        resultado_label.pack()


caracteres_label = tk.Label(frame1, text="Quantidade de caracteres:")
caracteres_label.pack()

descricao_label = tk.Label(root, text="Descrição:")
descricao_label.pack()
descricao_entry = tk.Entry(root)
descricao_entry.pack()

caracteres_entry = tk.Entry(frame1)
caracteres_entry.pack()

gerar_senha_botao = tk.Button(frame1, text="Gerar Senha", command=quantidade_caracteres)
gerar_senha_botao.pack()

def exibir_senhas():
    with open("senhas.csv", "r") as arquivo:
        leitor = csv.reader(arquivo)
        for widget in frame2.winfo_children():
            widget.destroy()
        for linha in leitor:
            senha = linha[0]
            descricao = linha[1]
            senha_label = tk.Label(frame2, text=descricao + " - " + senha)
            senha_label.pack()

exibir_senhas_botao = tk.Button(frame2, text="Exibir Senhas", command=exibir_senhas)
exibir_senhas_botao.pack()

root.mainloop()
