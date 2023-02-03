import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")

a_entry = tk.Entry(janela)
a_entry.pack()
b_entry = tk.Entry(janela)
b_entry.pack()

valor_operacao = tk.IntVar()
valor_operacao.set(1)

def adicao():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
    except ValueError:
        resultado_label.config(text="Entrada inválida. Por favor, insira números válidos.")
        return

    resultado = a + b
    resultado_label.config(text="Resultado: {:.2f}".format(resultado))

def subtracao():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
    except ValueError:
        resultado_label.config(text="Entrada inválida. Por favor, insira números válidos.")
        return

    resultado = a - b
    resultado_label.config(text="Resultado: {:.2f}".format(resultado))

def multiplicacao():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
    except ValueError:
        resultado_label.config(text="Entrada inválida. Por favor, insira números válidos.")
        return

    resultado = a * b
    resultado_label.config(text="Resultado: {:.2f}".format(resultado))

def divisao():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
    except ValueError:
        resultado_label.config(text="Entrada inválida. Por favor, insira números válidos.")
        return

    if b == 0:
        resultado_label.config(text="Divisão por zero não permitida.")
        return

    resultado = a / b
    resultado_label.config(text="Resultado: {:.2f}".format(resultado))

operacao_1 = tk.Radiobutton(janela, text="Adição", value=1, variable=valor_operacao, command=adicao)
operacao_1.pack()
operacao_2 = tk.Radiobutton(janela, text="Subtração", value=2, variable=valor_operacao, command=subtracao)
operacao_2.pack()
operacao_3 = tk.Radiobutton(janela, text="Multiplicação", value=3, variable=valor_operacao, command=multiplicacao)
operacao_3.pack()
operacao_4 = tk.Radiobutton(janela, text="Divisão", value=4, variable=valor_operacao, command=divisao)
operacao_4.pack()

calcular_botao = tk.Button(janela, text="Calcular", command=eval("operacao_{}".format(valor_operacao.get())))
calcular_botao.pack()

resultado_label = tk.Label(janela, text="Aguarde, metendo os calc")
resultado_label.pack()

janela.mainloop()
