import tkinter as tk

class TelaHome(tk.Frame):
    def __init__(self, parent, abrir_funcionario, abrir_cliente, abrir_fornecedor, abrir_produto, abrir_caminhao, abrir_manutencao, abrir_fluxo):
        super().__init__(parent)

        # Cor de fundo para a tela e widgets
        self.configure(bg='grey')

        self.abrir_funcionario = abrir_funcionario
        self.abrir_cliente = abrir_cliente
        self.abrir_fornecedor = abrir_fornecedor
        self.abrir_produto = abrir_produto
        self.abrir_caminhao = abrir_caminhao
        self.abrir_manutencao = abrir_manutencao
        self.abrir_fluxo = abrir_fluxo

        # Mensagem de boas-vindas no topo
        self.label_bem_vindo = tk.Label(self, text="Bem-vindo ao IOT!", font=("Arial", 16, "bold"), bg='grey', fg='black')
        self.label_bem_vindo.grid(row=0, column=0, columnspan=2, pady=10)

        # Frame para os botões (coluna de 3 botões por vez)
        self.frame_botoes = tk.Frame(self, bg='grey')
        self.frame_botoes.grid(row=1, column=0, columnspan=2, pady=20)

        # Função para criar um botão com estilo customizado
        def criar_botao(texto, comando):
            return tk.Button(self.frame_botoes, text=texto, command=comando, 
                             bd=5, bg='grey', fg='black', width=20, height=1, font=("Arial", 20))

        # Coluna 1
        self.botao_funcionario = criar_botao("Funcionário", self.abrir_funcionario)
        self.botao_funcionario.grid(row=0, column=0, padx=10, pady=10)

        self.botao_cliente = criar_botao("Cliente", self.abrir_cliente)
        self.botao_cliente.grid(row=1, column=0, padx=10, pady=10)

        self.botao_fornecedor = criar_botao("Fornecedor", self.abrir_fornecedor)
        self.botao_fornecedor.grid(row=2, column=0, padx=10, pady=10)

        # Coluna 2
        self.botao_produto = criar_botao("Produto", self.abrir_produto)
        self.botao_produto.grid(row=0, column=1, padx=10, pady=10)

        self.botao_caminhao = criar_botao("Caminhão", self.abrir_caminhao)
        self.botao_caminhao.grid(row=1, column=1, padx=10, pady=10)

        self.botao_manutencao = criar_botao("Manutenção", self.abrir_manutencao)
        self.botao_manutencao.grid(row=2, column=1, padx=10, pady=10)

        # Botão Fluxo de Caminhão
        self.botao_fluxo = criar_botao("Fluxo de Caminhão", self.abrir_fluxo)
        self.botao_fluxo.grid(row=3, column=0, columnspan=2, pady=20)
