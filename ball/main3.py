import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo de entrada de número")

# Define uma variável de controle para a entrada
entrada_valor = tk.StringVar()

# Cria um rótulo para exibir o valor da entrada
rotulo_valor = tk.Label(janela, text="")
rotulo_valor.pack()

# Cria uma entrada de número
entrada_numero = tk.Entry(janela, textvariable=entrada_valor)
entrada_numero.pack()

# Define uma função para atualizar o valor exibido no rótulo
def atualizar_valor():
    valor = entrada_valor.get()
    rotulo_valor.config(text=valor)

# Cria um botão para atualizar o valor
botao_atualizar = tk.Button(janela, text="Atualizar", command=atualizar_valor)
botao_atualizar.pack()

janela.mainloop()