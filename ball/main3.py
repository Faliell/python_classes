import tkinter as tk

# Função para calcular a velocidade, a aceleração e a energia cinética
def calcular():
    # Obtenção dos dados inseridos pelo usuário

    massa = float(massa_entry.get())
    forca = float(forca_entry.get())
    tempo = float(tempo_entry.get())
    coef_atrito = float(coef_atrito_entry.get())
    normal = float(normal_entry.get())

    # Cálculo da força de atrito dinâmico e estático
    fat = coef_atrito * normal
    if abs(forca) < abs(fat):
        fas = forca
    else:
        fas = -1 * fat

    # Cálculo da aceleração, da velocidade e da energia cinética
    aceleracao = (forca + fas) / massa
    velocidade = aceleracao * tempo
    energia_cinetica = 0.5 * massa * (velocidade ** 2)

    # Atualização dos valores nos widgets correspondentes
    aceleracao_label.configure(text=f"Aceleração: {aceleracao:.2f} m/s²")
    velocidade_label.configure(text=f"Velocidade: {velocidade:.2f} m/s")
    energia_cinetica_label.configure(text=f"Energia Cinética: {energia_cinetica:.2f} J")
    fat_label.configure(text=f"Força de Atrito Dinâmico: {fat:.2f} N")
    fas_label.configure(text=f"Força de Atrito Estático: {fas:.2f} N")

    # Desenho da bola
    raio = 20
    x = raio + 10
    y = altura_canvas - raio - 10
    bola = canvas.create_oval(x - raio, y - raio, x + raio, y + raio, fill="red")

    # Movimento da bola
    x_inicial = x
    y_inicial = y
    tempo_total = 0
    while x < largura_canvas - raio:
        # Cálculo da nova posição da bola
        delta_t = 0.1
        x = x_inicial + velocidade * tempo_total + 0.5 * aceleracao * (tempo_total ** 2)
        tempo_total += delta_t

        # Atualização da posição da bola no canvas
        canvas.move(bola, x - x_inicial, y - y_inicial)
        x_inicial = x
        canvas.update()

# Criação da janela
root = tk.Tk()
root.title("Calculadora de Movimento")

# Criação dos widgets para inserção dos dados
massa_label = tk.Label(root, text="Massa (kg): ")
massa_label.grid(row=0, column=0, padx=10, pady=5, sticky="W")
massa_entry = tk.Entry(root)
massa_entry.grid(row=0, column=1, padx=10, pady=5)
forca_label = tk.Label(root, text="Força (N): ")
forca_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
forca_entry = tk.Entry(root)
forca_entry.grid(row=1, column=1, padx=10, pady=5)
tempo_label = tk.Label(root, text="Tempo (s): ")
tempo_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
tempo_entry = tk.Entry(root)
tempo_entry.grid(row=2, column=1, padx=10, pady=5)
coef_atrito_label = tk.Label(root, text="Coeficiente de Atrito (s): ")
coef_atrito_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
coef_atrito_entry = tk.Entry(root)
coef_atrito_entry.grid(row=3, column=1, padx=10, pady=5)
normal_label = tk.Label(root, text="Força Normal (N): ")
normal_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
normal_entry = tk.Entry(root)
normal_entry.grid(row=4, column=1, padx=10, pady=5)

# Criação do botão de cálculo
calcular_button = tk.Button(root, text="Calcular", command=calcular)
calcular_button.grid(row=5, column=1, padx=10, pady=10)

# Criação dos widgets para exibição

aceleracao_label = tk.Label(root, text="Aceleração: ")
aceleracao_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
velocidade_label = tk.Label(root, text="Velocidade: ")
velocidade_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
energia_cinetica_label = tk.Label(root, text="Energia Cinética: ")
energia_cinetica_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")
fat_label = tk.Label(root, text="Força de Atrito Dinâmico: ")
fat_label.grid(row=9, column=0, padx=10, pady=5, sticky="w")
fas_label = tk.Label(root, text="Força de Atrito Estático: ")
fas_label.grid(row=10, column=0, padx=10, pady=5, sticky="w")

# Criação do canvas para desenho da bola
largura_canvas = 600
altura_canvas = 300
canvas = tk.Canvas(root, width=largura_canvas, height=altura_canvas)
canvas.grid(row=1, column=5, rowspan=9, padx=50, pady=50)

# Início do loop principal da aplicação
root.mainloop()