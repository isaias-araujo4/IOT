from tkinter import *
from tkinter import messagebox

class Fornecedor:
    def __init__(self):
        self.fornecedores = {}

    def pagina_fornecedor(self, container, voltar_func):
        self.gerar_menu_principal(container, "Fornecedor", self.adicionar_fornecedor, self.gerenciar_fornecedor, voltar_func)

    def gerar_menu_principal(self, container, titulo, func_adicionar, func_gerenciar, voltar_func):
        for widget in container.winfo_children():
            widget.destroy()

        Label(container, text=f"Menu {titulo}", font=("Arial", 16), bg="grey").pack(pady=20)
        Button(container, text=f"Adicionar Novo {titulo}", width=25, command=func_adicionar).pack(pady=10)
        Button(container, text=f"Pesquisar/Editar {titulo}", width=25, command=func_gerenciar).pack(pady=10)
        Button(container, text="Voltar ao home", width=20, command=voltar_func).pack(pady=20)

    def adicionar_fornecedor(self):
        # Implementar a lógica de adicionar um fornecedor
        pass

    def gerenciar_fornecedor(self):
        # Implementar a lógica de gerenciar fornecedores
        pass
