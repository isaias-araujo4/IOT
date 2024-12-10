from tkinter import *
from tkinter import messagebox

janela = Tk()

janela.title("home")  # Nome da tela
janela.resizable(False, False)  # Bloqueando a redimensionar a tela
janela.state("zoomed")  # Fazendo a tela abrir em fullscreen
janela['bg'] = "grey"  # Definindo a cor de fundo da tela

# Criando a mensagem e definindo a fonte, cor de fundo e texto
menssagem1 = Label(janela, text="Bem vindo AO IOT!", font="Arial 30", bg="grey", fg="black")
menssagem1.pack(pady=30)  # A mensagem fica no topo, com um espaçamento de 30 pixels

# Criando o frame para agrupar os botões
frame = Frame(janela, bg="grey")
frame.pack(pady=30)  # Espaço entre a mensagem e os botões

# Criando os botões
Button_width = 20
Button_height = 1

funcionario = Button(frame, text="Funcionário", font="Arial 20", bd=5, width=Button_width, height=Button_height)
cliente = Button(frame, text="Cliente", font="Arial 20", bd=5, width=Button_width, height=Button_height)
fornecedor = Button(frame, text="Fornecedor", font="Arial 20", bd=5, width=Button_width, height=Button_height)
produto = Button(frame, text="Produto", font="Arial 20", bd=5, width=Button_width, height=Button_height)
caminhao = Button(frame, text="Caminhão", font="Arial 20", bd=5, width=Button_width, height=Button_height)
manutencao = Button(frame, text="Manutenção", font="Arial 20", bd=5, width=Button_width, height=Button_height)
fluxo_caminhoes = Button(frame, text="Fluxo de Caminhões", font="Arial 20", bd=5, width=Button_width, height=Button_height)

# Empacotando os botões em duas colunas (3 botões em cada coluna)
funcionario.grid(row=0, column=0, padx=10, pady=10)
cliente.grid(row=1, column=0, padx=10, pady=10)
fornecedor.grid(row=2, column=0, padx=10, pady=10)
produto.grid(row=0, column=1, padx=10, pady=10)
caminhao.grid(row=1, column=1, padx=10, pady=10)
manutencao.grid(row=2, column=1, padx=10, pady=10)
fluxo_caminhoes.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

# Centralizando o grid no frame
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

janela.mainloop()
