from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class Manutencao:
    def __init__(self, produtos, funcionarios, caminhoes):
        self.manutencoes = []
        self.produtos = produtos
        self.funcionarios = funcionarios
        self.caminhoes = caminhoes
        self.container = None

    def validar_produto(self, nome_produto):
        for produto in self.produtos:
            if produto[1] == nome_produto:
                return True
        return False

    def validar_funcionario(self, nome_funcionario, sobrenome_funcionario):
        for funcionario in self.funcionarios:
            if funcionario[0] == nome_funcionario and funcionario[1] == sobrenome_funcionario:
                return True
        return False

    def validar_caminhao(self, marca, modelo):
        for caminhao in self.caminhoes:
            if caminhao[1] == marca and caminhao[0] == modelo:
                return True
        return False

    def pagina_manutencao(self, container, voltar_func):
        self.container = container

        for widget in container.winfo_children():
            widget.destroy()

        self.exibir_label(container)
        self.exibir_tabela(container)

        Label(container, text="Digite o ID para busca:", font=("Arial", 12), bg="grey").pack(pady=10)
        search_frame = Frame(container, bg="grey")
        search_frame.pack(pady=10)
        self.id_entry = Entry(search_frame, font=("Arial", 12), width=15)
        self.id_entry.pack(side=LEFT, padx=5)
        search_button = Button(search_frame, text="Pesquisar", command=self.pesquisar_manutencao, font=("Arial", 12))
        search_button.pack(side=LEFT, padx=5)
        delete_button = Button(search_frame, text="Excluir", command=self.excluir_manutencao, font=("Arial", 12))
        delete_button.pack(side=LEFT, padx=5)

        self.exibir_botoes(container)
        Button(container, text="Voltar ao Home", width=20, command=voltar_func).pack(pady=20)

    def exibir_label(self, container):
        label = Label(container, text="Gerenciamento de Manutenção", font=("Arial", 16), bg="grey")
        label.pack(pady=10)

    def exibir_tabela(self, container=None):
        for widget in container.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.destroy()

        num_linhas = len(self.manutencoes)
        self.tabela = ttk.Treeview(container, columns=("ID", "Data", "Serviço", "Produto", "Funcionário", "Caminhão"), show="headings", height=num_linhas)
        self.tabela.pack(pady=10, padx=20)

        col_names = ["ID", "Data", "Serviço", "Produto", "Funcionário", "Caminhão"]
        for col_name in col_names:
            self.tabela.heading(col_name, text=col_name)
        
        col_widths = [50, 100, 150, 150, 150, 150]
        for col, width in zip(self.tabela["columns"], col_widths):
            self.tabela.column(col, width=width)
        
        for manutencao in self.manutencoes:
            self.tabela.insert("", "end", values=manutencao)

    def exibir_botoes(self, container):
        botoes_frame = Frame(container, bg="grey")
        botoes_frame.pack(pady=10)
        add_button = Button(botoes_frame, text="Adicionar", command=self.adicionar_manutencao, font=("Arial", 12), width=10)
        add_button.pack(side=LEFT, padx=10)
        edit_button = Button(botoes_frame, text="Editar", command=self.editar_manutencao, font=("Arial", 12), width=10)
        edit_button.pack(side=LEFT, padx=10)

    def adicionar_manutencao(self):
        self.janela_adicionar = Toplevel()
        self.janela_adicionar.title("Adicionar Nova Manutenção")
        form_frame = Frame(self.janela_adicionar)
        form_frame.pack(pady=10)

        campos = [
            ("Data:", "data_entry"),
            ("Serviço:", "servico_entry"),
            ("Produto:", "produto_entry"),
            ("Nome do Funcionário:", "nome_funcionario_entry"),
            ("Sobrenome do Funcionário:", "sobrenome_funcionario_entry"),
            ("Marca do Caminhão:", "marca_caminhao_entry"),
            ("Modelo do Caminhão:", "modelo_caminhao_entry")
        ]

        self.entries = {}
        for i, (label_text, entry_name) in enumerate(campos):
            Label(form_frame, text=label_text).grid(row=i, column=0, sticky=W, pady=5, padx=5)
            entry = Entry(form_frame, font=("Arial", 12))
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries[entry_name] = entry

        button_frame = Frame(self.janela_adicionar)
        button_frame.pack(pady=10)
        Button(button_frame, text="Salvar", command=self.salvar_manutencao, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
        Button(button_frame, text="Cancelar", command=self.janela_adicionar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

    def salvar_manutencao(self):
        data = self.entries["data_entry"].get()
        servico = self.entries["servico_entry"].get()
        produto = self.entries["produto_entry"].get()
        nome_funcionario = self.entries["nome_funcionario_entry"].get()
        sobrenome_funcionario = self.entries["sobrenome_funcionario_entry"].get()
        marca_caminhao = self.entries["marca_caminhao_entry"].get()
        modelo_caminhao = self.entries["modelo_caminhao_entry"].get()

        if not (data and servico and produto and nome_funcionario and sobrenome_funcionario and marca_caminhao and modelo_caminhao):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios!")
            return

        if not self.validar_produto(produto):
            messagebox.showerror("Erro", "Produto não encontrado!")
            return

        if not self.validar_funcionario(nome_funcionario, sobrenome_funcionario):
            messagebox.showerror("Erro", "Funcionário não encontrado!")
            return

        if not self.validar_caminhao(marca_caminhao, modelo_caminhao):
            messagebox.showerror("Erro", "Caminhão não encontrado!")
            return

        id_manutencao = len(self.manutencoes) + 1
        self.manutencoes.append((id_manutencao, data, servico, produto, f"{nome_funcionario} {sobrenome_funcionario}", f"{marca_caminhao} {modelo_caminhao}"))
        self.exibir_tabela(self.container)
        self.janela_adicionar.destroy()
        messagebox.showinfo("Sucesso", "Manutenção adicionada com sucesso!")

    def pesquisar_manutencao(self):
        id_procurado = self.id_entry.get()
        if not id_procurado:
            messagebox.showerror("Erro", "Digite um ID para pesquisar!")
            return

        for row in self.tabela.get_children():
            self.tabela.delete(row)

        encontrado = False
        for manutencao in self.manutencoes:
            if str(manutencao[0]) == id_procurado:
                self.tabela.insert("", "end", values=manutencao)
                messagebox.showinfo("Manutenção Encontrada", f"Serviço: {manutencao[2]}")
                encontrado = True
                break

        if not encontrado:
            messagebox.showerror("Erro", "Manutenção não encontrada.")
            self.tabela.delete(*self.tabela.get_children())
            for manutencao in self.manutencoes:
                self.tabela.insert("", "end", values=manutencao)

    def excluir_manutencao(self):
        id_procurado = self.id_entry.get()
        if not id_procurado:
            messagebox.showerror("Erro", "Digite um ID para excluir!")
            return

        for i, manutencao in enumerate(self.manutencoes):
            if str(manutencao[0]) == id_procurado:
                del self.manutencoes[i]
                self.exibir_tabela(self.container)
                messagebox.showinfo("Sucesso", "Manutenção excluída com sucesso!")
                return

        messagebox.showerror("Erro", "Manutenção não encontrada!")

    def editar_manutencao(self):
        id_procurado = self.id_entry.get()
        if not id_procurado:
            messagebox.showerror("Erro", "Digite um ID para editar!")
            return

        manutencao_encontrada = None
        for manutencao in self.manutencoes:
            if str(manutencao[0]) == id_procurado:
                manutencao_encontrada = manutencao
                break

        if not manutencao_encontrada:
            messagebox.showerror("Erro", "Manutenção não encontrada!")
            return

        self.janela_editar = Toplevel()
        self.janela_editar.title("Editar Manutenção")
        form_frame = Frame(self.janela_editar)
        form_frame.pack(pady=10)

        campos = [
            ("Data:", "data_entry", manutencao_encontrada[1]),
            ("Serviço:", "servico_entry", manutencao_encontrada[2]),
            ("Produto:", "produto_entry", manutencao_encontrada[3]),
            ("Nome do Funcionário:", "nome_funcionario_entry", manutencao_encontrada[4].split()[0]),
            ("Sobrenome do Funcionário:", "sobrenome_funcionario_entry", manutencao_encontrada[4].split()[1]),
            ("Marca do Caminhão:", "marca_caminhao_entry", manutencao_encontrada[5].split()[0]),
            ("Modelo do Caminhão:", "modelo_caminhao_entry", manutencao_encontrada[5].split()[1])
        ]

        self.entries = {}
        for i, (label_text, entry_name, value) in enumerate(campos):
            Label(form_frame, text=label_text).grid(row=i, column=0, sticky=W, pady=5, padx=5)
            entry = Entry(form_frame, font=("Arial", 12))
            entry.grid(row=i, column=1, pady=5, padx=5)
            entry.insert(0, value)
            self.entries[entry_name] = entry

        button_frame = Frame(self.janela_editar)
        button_frame.pack(pady=10)
        Button(button_frame, text="Salvar", command=lambda: self.atualizar_manutencao(manutencao_encontrada[0]), font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
        Button(button_frame, text="Cancelar", command=self.janela_editar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

    def atualizar_manutencao(self, id_manutencao):
        data = self.entries["data_entry"].get()
        servico = self.entries["servico_entry"].get()
        produto = self.entries["produto_entry"].get()
        nome_funcionario = self.entries["nome_funcionario_entry"].get()
        sobrenome_funcionario = self.entries["sobrenome_funcionario_entry"].get()
        marca_caminhao = self.entries["marca_caminhao_entry"].get()
        modelo_caminhao = self.entries["modelo_caminhao_entry"].get()

        if not (data and servico and produto and nome_funcionario and sobrenome_funcionario and marca_caminhao and modelo_caminhao):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios!")
            return

        if not self.validar_produto(produto):
            messagebox.showerror("Erro", "Produto não encontrado!")
            return

        if not self.validar_funcionario(nome_funcionario, sobrenome_funcionario):
            messagebox.showerror("Erro", "Funcionário não encontrado!")
            return

        if not self.validar_caminhao(marca_caminhao, modelo_caminhao):
            messagebox.showerror("Erro", "Caminhão não encontrado!")
            return

        for i, manutencao in enumerate(self.manutencoes):
            if manutencao[0] == id_manutencao:
                self.manutencoes[i] = (id_manutencao, data, servico, produto, f"{nome_funcionario} {sobrenome_funcionario}", f"{marca_caminhao} {modelo_caminhao}")
                break

        self.exibir_tabela(self.container)
        self.janela_editar.destroy()
        messagebox.showinfo("Sucesso", "Manutenção atualizada com sucesso!")
