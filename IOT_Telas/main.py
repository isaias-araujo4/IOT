#projeto: IOT
#Turma: G88435/89686 DS
#Alunos: Isaias Araujo, Samuel Sousa, Daniel Jorge

from tkinter import *
from tkinter import messagebox
from funcionarios import Funcionario
from clientes import Cliente
from fornecedores import Fornecedor
from caminhões import Caminhao
from produtos import Produto
from manutenções import Manutencao  # Adicione esta linha
from fluxos import Fluxo  

class Home:
    def __init__(self, root):
        self.root = root
        self.root.title("Home")
        self.root.state("zoomed")
        self.root.resizable(False, False)
        self.root['bg'] = "grey"

        self.funcionarios = Funcionario()
        self.clientes = Cliente()
        self.fornecedores = Fornecedor()
        self.caminhoes = Caminhao()
        self.produtos = Produto()
        self.manutencoes = Manutencao(self.produtos.produtos, self.funcionarios.funcionarios, self.caminhoes.caminhoes)  # Adicione esta linha
        self.fluxo = Fluxo(self.funcionarios.funcionarios, self.clientes.clientes, self.caminhoes.caminhoes)

        self.container = Frame(self.root, bg="grey")
        self.container.pack(fill=BOTH, expand=True)

        # Botão para fechar o programa, posicionado no canto superior esquerdo
        self.close_button = Button(self.root, text="X", command=self.fechar_programa, bg="red", fg="white", font=("Arial", 12, "bold"))
        self.close_button.place(x=10, y=10)  # Ajuste da posição no canto superior esquerdo da janela principal

        self.pagina_principal()

    def pagina_principal(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        Label(self.container, text="Bem-vindo ao IOT!", font=("Arial", 20), bg="grey", fg="black").pack(pady=20)
        Button(self.container, text="Funcionário", width=20, command=self.pagina_funcionario).pack(pady=10)
        Button(self.container, text="Cliente", width=20, command=self.pagina_cliente).pack(pady=10)
        Button(self.container, text="Fornecedor", width=20, command=self.pagina_fornecedor).pack(pady=10)
        Button(self.container, text="Caminhão", width=20, command=self.pagina_caminhao).pack(pady=10)
        Button(self.container, text="Produto", width=20, command=self.pagina_produto).pack(pady=10)
        Button(self.container, text="Manutenção", width=20, command=self.pagina_manutencao).pack(pady=10)  # Adicione esta linha
        Button(self.container, text="Fluxo", width=20, command=self.pagina_fluxo).pack(pady=10)

    def fechar_programa(self):
        self.root.quit()

    def pagina_funcionario(self):
        self.funcionarios.pagina_funcionario(self.container, self.pagina_principal)

    def pagina_cliente(self):
        self.clientes.pagina_cliente(self.container, self.pagina_principal)

    def pagina_fornecedor(self):
        self.fornecedores.pagina_fornecedor(self.container, self.pagina_principal)
        
    def pagina_caminhao(self):
        self.caminhoes.pagina_caminhao(self.container, self.pagina_principal)

    def pagina_produto(self):
        self.produtos.pagina_produto(self.container, self.pagina_principal)

    def pagina_manutencao(self):  # Adicione este método
        self.manutencoes.pagina_manutencao(self.container, self.pagina_principal)

    def pagina_fluxo(self):
        self.fluxo.pagina_fluxo(self.container, self.pagina_principal)

if __name__ == "__main__":
    root = Tk()
    app = Home(root)
    root.mainloop()
