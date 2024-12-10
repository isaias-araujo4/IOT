#Projeto IOT
#Turma: G88435/89686 DS
#Aunos: Isaias Araujo, Samuel Sousa e Daniel Jorge

from tkinter import *
from tkinter import messagebox

class Home:
    def __init__(self, root):
        self.root = root
        self.root.title("Home")
        self.root.state("zoomed")
        self.root.resizable(False, False)
        self.root['bg'] = "grey"

        self.funcionarios = {}  # Armazena os funcionários cadastrados
        self.clientes = {}  # Armazena os clientes cadastrados
        self.fornecedores = {}  # Armazena os fornecedores cadastrados

        self.container = Frame(self.root, bg="grey")
        self.container.pack(fill=BOTH, expand=True)
        self.pagina_principal()

    def pagina_principal(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        Label(self.container, text="Bem-vindo ao IOT!", font=("Arial", 20), bg="grey", fg="black").pack(pady=20)
        Button(self.container, text="Funcionário", width=20, command=self.pagina_funcionario).pack(pady=10)
        Button(self.container, text="Cliente", width=20, command=self.pagina_cliente).pack(pady=10)
        Button(self.container, text="Fornecedor", width=20, command=self.pagina_fornecedor).pack(pady=10)
        Button(self.container, text="Sair", width=20, command=self.root.destroy).pack(pady=20)

    def pagina_funcionario(self):
        self.gerar_menu_principal("Funcionário", self.adicionar_funcionario, self.gerenciar_funcionario)

    def pagina_cliente(self):
        self.gerar_menu_principal("Cliente", self.adicionar_cliente, self.gerenciar_cliente)

    def pagina_fornecedor(self):
        self.gerar_menu_principal("Fornecedor", self.adicionar_fornecedor, self.gerenciar_fornecedor)

    def gerar_menu_principal(self, titulo, func_adicionar, func_gerenciar):
        for widget in self.container.winfo_children():
            widget.destroy()

        Label(self.container, text=f"Menu {titulo}", font=("Arial", 16), bg="grey").pack(pady=20)
        Button(self.container, text=f"Adicionar Novo {titulo}", width=25, command=func_adicionar).pack(pady=10)
        Button(self.container, text=f"Pesquisar/Editar {titulo}", width=25, command=func_gerenciar).pack(pady=10)
        Button(self.container, text="Voltar ao home", width=20, command=self.pagina_principal).pack(pady=20)

    def adicionar_funcionario(self):
        self.gerar_pagina_adicionar("Funcionário", "CPF", True, self.salvar_funcionario)

    def adicionar_cliente(self):
        self.gerar_pagina_adicionar("Cliente", "Documento", False, self.salvar_cliente)

    def adicionar_fornecedor(self):
        self.gerar_pagina_adicionar("Fornecedor", "CNPJ", False, self.salvar_fornecedor, incluir_segmento=True)

    def gerar_pagina_adicionar(self, tipo, campo_chave, incluir_cargo, func_salvar, incluir_segmento=False):
        for widget in self.container.winfo_children():
            widget.destroy()

        Label(self.container, text=f"Adicionar {tipo}", font=("Arial", 16), bg="grey").pack(pady=20)
        frame_dados = Frame(self.container, bg="grey")
        frame_dados.pack(pady=10)

        # Dados gerais
        Label(frame_dados, text="Nome:", font=("Arial", 12), bg="grey").grid(row=0, column=0, pady=5, padx=10, sticky=W)
        self.nome_entry = Entry(frame_dados)
        self.nome_entry.grid(row=0, column=1, pady=5, padx=10)

        Label(frame_dados, text="Sobrenome:", font=("Arial", 12), bg="grey").grid(row=0, column=2, pady=5, padx=10, sticky=W)
        self.sobrenome_entry = Entry(frame_dados)
        self.sobrenome_entry.grid(row=0, column=3, pady=5, padx=10)

        Label(frame_dados, text=f"{campo_chave}:", font=("Arial", 12), bg="grey").grid(row=1, column=0, pady=5, padx=10, sticky=W)
        self.chave_entry = Entry(frame_dados)
        self.chave_entry.grid(row=1, column=1, pady=5, padx=10)

        if incluir_cargo:
            Label(frame_dados, text="Cargo:", font=("Arial", 12), bg="grey").grid(row=1, column=2, pady=5, padx=10, sticky=W)
            self.cargo_entry = Entry(frame_dados)
            self.cargo_entry.grid(row=1, column=3, pady=5, padx=10)

        if incluir_segmento:
            Label(frame_dados, text="Segmento:", font=("Arial", 12), bg="grey").grid(row=1, column=2, pady=5, padx=10, sticky=W)
            self.segmento_entry = Entry(frame_dados)
            self.segmento_entry.grid(row=1, column=3, pady=5, padx=10)

        # Contato
        Label(frame_dados, text="Telefone:", font=("Arial", 12), bg="grey").grid(row=2, column=0, pady=5, padx=10, sticky=W)
        self.telefone_entry = Entry(frame_dados)
        self.telefone_entry.grid(row=2, column=1, pady=5, padx=10)

        Label(frame_dados, text="Celular:", font=("Arial", 12), bg="grey").grid(row=2, column=2, pady=5, padx=10, sticky=W)
        self.celular_entry = Entry(frame_dados)
        self.celular_entry.grid(row=2, column=3, pady=5, padx=10)

        Label(frame_dados, text="E-mail:", font=("Arial", 12), bg="grey").grid(row=3, column=0, pady=5, padx=10, sticky=W)
        self.email_entry = Entry(frame_dados)
        self.email_entry.grid(row=3, column=1, pady=5, padx=10)

        # Endereço
        Label(frame_dados, text="Logradouro:", font=("Arial", 12), bg="grey").grid(row=4, column=0, pady=5, padx=10, sticky=W)
        self.logradouro_entry = Entry(frame_dados)
        self.logradouro_entry.grid(row=4, column=1, pady=5, padx=10)

        Label(frame_dados, text="Número:", font=("Arial", 12), bg="grey").grid(row=4, column=2, pady=5, padx=10, sticky=W)
        self.numero_entry = Entry(frame_dados)
        self.numero_entry.grid(row=4, column=3, pady=5, padx=10)

        Label(frame_dados, text="Bairro:", font=("Arial", 12), bg="grey").grid(row=5, column=0, pady=5, padx=10, sticky=W)
        self.bairro_entry = Entry(frame_dados)
        self.bairro_entry.grid(row=5, column=1, pady=5, padx=10)

        Label(frame_dados, text="Cidade:", font=("Arial", 12), bg="grey").grid(row=5, column=2, pady=5, padx=10, sticky=W)
        self.cidade_entry = Entry(frame_dados)
        self.cidade_entry.grid(row=5, column=3, pady=5, padx=10)

        Label(frame_dados, text="CEP:", font=("Arial", 12), bg="grey").grid(row=6, column=0, pady=5, padx=10, sticky=W)
        self.cep_entry = Entry(frame_dados)
        self.cep_entry.grid(row=6, column=1, pady=5, padx=10)

        Label(frame_dados, text="Complemento:", font=("Arial", 12), bg="grey").grid(row=6, column=2, pady=5, padx=10, sticky=W)
        self.complemento_entry = Entry(frame_dados)
        self.complemento_entry.grid(row=6, column=3, pady=5, padx=10)

        Button(self.container, text=f"Salvar {tipo}", width=20, command=func_salvar).pack(pady=20)
        Button(self.container, text="Voltar", width=20, command=self.pagina_principal).pack(pady=10)

    def salvar_funcionario(self):
        self.salvar_dados(self.funcionarios, "CPF", incluir_cargo=True)

    def salvar_cliente(self):
        self.salvar_dados(self.clientes, "Documento")

    def salvar_fornecedor(self):
        self.salvar_dados(self.fornecedores, "CNPJ", incluir_segmento=True)

    def salvar_dados(self, armazenamento, campo_chave, incluir_cargo=False, incluir_segmento=False):
        campos = {
            "Nome": self.nome_entry.get(),
            "Sobrenome": self.sobrenome_entry.get(),
            campo_chave: self.chave_entry.get(),
            "Telefone": self.telefone_entry.get(),
            "Celular": self.celular_entry.get(),
            "E-mail": self.email_entry.get(),
            "Logradouro": self.logradouro_entry.get(),
            "Número": self.numero_entry.get(),
            "Bairro": self.bairro_entry.get(),
            "Cidade": self.cidade_entry.get(),
            "CEP": self.cep_entry.get(),
            "Complemento": self.complemento_entry.get(),
        }

        if incluir_cargo:
            campos["Cargo"] = self.cargo_entry.get()
        if incluir_segmento:
            campos["Segmento"] = self.segmento_entry.get()

        for campo, valor in campos.items():
            if not valor.strip():
                messagebox.showerror("Erro", f"Campo '{campo}' não pode estar vazio!")
                return

        armazenamento[campos[campo_chave]] = campos
        messagebox.showinfo("Sucesso", f"{campo_chave} adicionado com sucesso!")
        self.pagina_principal()

    def gerenciar_funcionario(self):
        self.gerar_pagina_pesquisar("Funcionário", "CPF", self.funcionarios)

    def gerenciar_cliente(self):
        self.gerar_pagina_pesquisar("Cliente", "Documento", self.clientes)

    def gerenciar_fornecedor(self):
        self.gerar_pagina_pesquisar("Fornecedor", "CNPJ", self.fornecedores)

    def gerar_pagina_pesquisar(self, tipo, campo_chave, armazenamento):
        for widget in self.container.winfo_children():
            widget.destroy()

        Label(self.container, text=f"Pesquisar {tipo}", font=("Arial", 16), bg="grey").pack(pady=20)
        Label(self.container, text=f"Digite o {campo_chave}:", font=("Arial", 12), bg="grey").pack(pady=5)
        self.campo_chave_entry = Entry(self.container)
        self.campo_chave_entry.pack(pady=5)

        Button(self.container, text="Pesquisar", width=15, command=lambda: self.pesquisar_dados(armazenamento, tipo, campo_chave)).pack(pady=10)
        Button(self.container, text="Voltar", width=20, command=self.pagina_principal).pack(pady=10)

    def pesquisar_dados(self, armazenamento, tipo, campo_chave):
        chave = self.campo_chave_entry.get()
        dados = armazenamento.get(chave)

        if not dados:
            messagebox.showerror("Erro", f"{tipo} não encontrado!")
            return

        self.editar_dados(armazenamento, chave, dados)

    def editar_dados(self, armazenamento, chave, dados):
        for widget in self.container.winfo_children():
            widget.destroy()

        Label(self.container, text=f"Editando {chave}", font=("Arial", 16), bg="grey").pack(pady=20)
        frame_dados = Frame(self.container, bg="grey")
        frame_dados.pack(pady=10)

        for idx, (campo, valor) in enumerate(dados.items()):
            Label(frame_dados, text=f"{campo}:", font=("Arial", 12), bg="grey").grid(row=idx, column=0, pady=5, padx=10, sticky=W)
            entry = Entry(frame_dados)
            entry.insert(0, valor)
            entry.grid(row=idx, column=1, pady=5, padx=10)
            dados[campo] = entry

        Button(self.container, text="Salvar Alterações", width=20, command=lambda: self.salvar_alteracoes(armazenamento, chave, dados)).pack(pady=20)
        Button(self.container, text="Voltar", width=20, command=self.pagina_principal).pack(pady=10)

    def salvar_alteracoes(self, armazenamento, chave, dados):
        for campo, entry in dados.items():
            valor = entry.get()
            if not valor.strip():
                messagebox.showerror("Erro", f"Campo '{campo}' não pode estar vazio!")
                return
            dados[campo] = valor

        armazenamento[chave] = {campo: entry.get() for campo, entry in dados.items()}
        messagebox.showinfo("Sucesso", "Alterações salvas com sucesso!")
        self.pagina_principal()


if __name__ == "__main__":
    root = Tk()
    app = Home(root)
    root.mainloop()
