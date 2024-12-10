import tkinter as tk

class TelaFornecedor(tk.Frame):
    def __init__(self, parent, voltar_home):
        super().__init__(parent)
        
        # Cor de fundo para a tela e widgets
        self.configure(bg='grey')

        self.voltar_home = voltar_home

        # Título da tela
        self.label = tk.Label(self, text="Tela de Fornecedor", font=("Arial", 16, "bold"), bg='grey', fg='black')
        self.label.pack(pady=10)

        # Função para criar um botão com estilo customizado
        def criar_botao(texto, comando):
            return tk.Button(self, text=texto, command=comando, 
                             bd=5, bg='grey', fg='black', width=20, height=1, font=("Arial", 20))

        # Botão para voltar à tela inicial
        self.botao_voltar = criar_botao("Voltar para Home", self.voltar_home)
        self.botao_voltar.pack(pady=10)
