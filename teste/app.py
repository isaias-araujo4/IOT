import tkinter as tk
from tela_home import TelaHome
from tela_funcionario import TelaFuncionario
from tela_cliente import TelaCliente
from tela_fornecedor import TelaFornecedor
from tela_produto import TelaProduto
from tela_caminhao import TelaCaminhao
from tela_manutencao import TelaManutencao
from tela_fluxo import TelaFluxo

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IOT")
        self.root['bg'] = "grey"
        self.root.resizable(False, False)
        self.root.state("zoomed")
        
        # Iniciar TelaHome (que é a tela principal)
        self.tela_home = TelaHome(self.root, self.abrir_funcionario, self.abrir_cliente, self.abrir_fornecedor,
                                  self.abrir_produto, self.abrir_caminhao, self.abrir_manutencao, self.abrir_fluxo)
        self.tela_home.pack()

    def abrir_funcionario(self):
        self.tela_home.pack_forget()  # Esconde a TelaHome
        self.tela_funcionario = TelaFuncionario(self.root, self.voltar_home)
        self.tela_funcionario.pack()

    def abrir_cliente(self):
        self.tela_home.pack_forget()  # Esconde a TelaHome
        self.tela_cliente = TelaCliente(self.root, self.voltar_home)
        self.tela_cliente.pack()

    def abrir_fornecedor(self):
        self.tela_home.pack_forget()  # Esconde a TelaHome
        self.tela_fornecedor = TelaFornecedor(self.root, self.voltar_home)
        self.tela_fornecedor.pack()

    def abrir_produto(self):
        self.tela_home.pack_forget()  # Esconde a TelaHome
        self.tela_produto = TelaProduto(self.root, self.voltar_home)
        self.tela_produto.pack()

    def abrir_caminhao(self):
        self.tela_home.pack_forget()  # Esconde a TelaHome
        self.tela_caminhao = TelaCaminhao(self.root, self.voltar_home)
        self.tela_caminhao.pack()

    def abrir_manutencao(self):
        self.tela_home.pack_forget()  # Esconde a TelaHome
        self.tela_manutencao = TelaManutencao(self.root, self.voltar_home)
        self.tela_manutencao.pack()

    def abrir_fluxo(self):
        self.tela_home.pack_forget()  # Esconde a TelaHome
        self.tela_fluxo = TelaFluxo(self.root, self.voltar_home)
        self.tela_fluxo.pack()

    def voltar_home(self):
        # Esconde as outras telas
        if hasattr(self, 'tela_funcionario'):
            self.tela_funcionario.pack_forget()
        if hasattr(self, 'tela_cliente'):
            self.tela_cliente.pack_forget()
        if hasattr(self, 'tela_fornecedor'):
            self.tela_fornecedor.pack_forget()
        if hasattr(self, 'tela_produto'):
            self.tela_produto.pack_forget()
        if hasattr(self, 'tela_caminhao'):
            self.tela_caminhao.pack_forget()
        if hasattr(self, 'tela_manutencao'):
            self.tela_manutencao.pack_forget()
        if hasattr(self, 'tela_fluxo'):
            self.tela_fluxo.pack_forget()
        
        # Exibe a TelaHome novamente
        self.tela_home.pack()

root = tk.Tk()
app = MainApp(root)
root.mainloop()
