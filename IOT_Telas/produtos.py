from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
from datetime import datetime

class Produto:
    def __init__(self):
        self.produtos = []
        self.container = None

    def validar_validade(self, validade):
        try:
            datetime.strptime(validade, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def validar_quantidade(self, quantidade):
        try:
            float(quantidade)
            return True
        except ValueError:
            return False

    def pagina_produto(self, container, voltar_func):
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
        search_button = Button(search_frame, text="Pesquisar", command=self.pesquisar_produto, font=("Arial", 12))
        search_button.pack(side=LEFT, padx=5)
        delete_button = Button(search_frame, text="Excluir", command=self.excluir_produto, font=("Arial", 12))
        delete_button.pack(side=LEFT, padx=5)

        self.exibir_botoes(container)
        Button(container, text="Voltar ao Home", width=20, command=voltar_func).pack(pady=20)

    def exibir_label(self, container):
        label = Label(container, text="Gerenciamento de Produto", font=("Arial", 16), bg="grey")
        label.pack(pady=10)

    def exibir_tabela(self, container=None):
        for widget in container.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.destroy()

        num_linhas = len(self.produtos)
        self.tabela = ttk.Treeview(container, columns=("ID", "Nome", "Validade", "Segmento", "Lote", "Armazenamento", "Quantidade"), show="headings", height=num_linhas)
        self.tabela.pack(pady=10, padx=20)

        col_names = ["ID", "Nome", "Validade", "Segmento", "Lote", "Armazenamento", "Quantidade"]
        for col_name in col_names:
            self.tabela.heading(col_name, text=col_name)
        
        col_widths = [50, 150, 100, 100, 100, 100, 100]
        for col, width in zip(self.tabela["columns"], col_widths):
            self.tabela.column(col, width=width)
        
        for produto in self.produtos:
            self.tabela.insert("", "end", values=produto)

    def exibir_botoes(self, container):
        botoes_frame = Frame(container, bg="grey")
        botoes_frame.pack(pady=10)
        add_button = Button(botoes_frame, text="Adicionar", command=self.adicionar_produto, font=("Arial", 12), width=10)
        add_button.pack(side=LEFT, padx=10)
        edit_button = Button(botoes_frame, text="Editar", command=self.editar_produto, font=("Arial", 12), width=10)
        edit_button.pack(side=LEFT, padx=10)

    def adicionar_produto(self):
        self.janela_adicionar = Toplevel()
        self.janela_adicionar.title("Adicionar Novo Produto")
        form_frame = Frame(self.janela_adicionar)
        form_frame.pack(pady=10)

        campos = [
            ("Nome:", "nome_entry"),
            ("Validade:", "validade_entry"),
            ("Segmento:", "segmento_entry"),
            ("Lote:", "lote_entry"),
            ("Armazenamento:", "armazenamento_entry"),
            ("Quantidade:", "quantidade_entry")
        ]

        self.entries = {}
        for i, (label_text, entry_name) in enumerate(campos):
            Label(form_frame, text=label_text).grid(row=i, column=0, sticky=W, pady=5, padx=5)
            entry = Entry(form_frame, font=("Arial", 12))
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries[entry_name] = entry

        button_frame = Frame(self.janela_adicionar)
        button_frame.pack(pady=10)
        Button(button_frame, text="Salvar", command=self.salvar_produto, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
        Button(button_frame, text="Cancelar", command=self.janela_adicionar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

    def salvar_produto(self):
        nome = self.entries["nome_entry"].get()
        validade = self.entries["validade_entry"].get()
        segmento = self.entries["segmento_entry"].get()
        lote = self.entries["lote_entry"].get()
        armazenamento = self.entries["armazenamento_entry"].get()
        quantidade = self.entries["quantidade_entry"].get()

        if not nome and validade and segmento and lote and armazenamento and quantidade:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios!")
            return

        if not self.validar_validade(validade):
            messagebox.showerror("Erro", "Data de validade inválida! Use o formato DD/MM/AAAA.")
            return

        if not self.validar_quantidade(quantidade):
            messagebox.showerror("Erro", "Quantidade inválida! Deve ser um número.")
            return

        id_produto = len(self.produtos) + 1
        self.produtos.append((id_produto, nome, validade, segmento, lote, armazenamento, float(quantidade)))
        self.exibir_tabela(self.container)
        self.janela_adicionar.destroy()
        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")

    def pesquisar_produto(self):
        id_procurado = self.id_entry.get()
        if not id_procurado:
            messagebox.showerror("Erro", "Digite um ID para pesquisar!")
            return

        for row in self.tabela.get_children():
            self.tabela.delete(row)

        encontrado = False
        for produto in self.produtos:
            if str(produto[0]) == id_procurado:
                self.tabela.insert("", "end", values=produto)
                messagebox.showinfo("Produto Encontrado", f"Produto: {produto[1]}")
                encontrado = True
                break

        if not encontrado:
            messagebox.showerror("Erro", "Produto não encontrado.")
            self.tabela.delete(*self.tabela.get_children())
            for produto in self.produtos:
                self.tabela.insert("", "end", values=produto)

    def excluir_produto(self):
        id_procurado = self.id_entry.get()
        if not id_procurado:
            messagebox.showerror("Erro", "Digite um ID para excluir!")
            return

        for i, produto in enumerate(self.produtos):
            if str(produto[0]) == id_procurado:
                del self.produtos[i]
                self.exibir_tabela(self.container)
                messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
                return

        messagebox.showerror("Erro", "Produto não encontrado!")

    def editar_produto(self):
        id_procurado = self.id_entry.get()
        if not id_procurado:
            messagebox.showerror("Erro", "Digite um ID para editar!")
            return

        produto_encontrado = None
        for produto in self.produtos:
            if str(produto[0]) == id_procurado:
                produto_encontrado = produto
                break

        if not produto_encontrado:
            messagebox.showerror("Erro", "Produto não encontrado!")
            return

        self.janela_editar = Toplevel()
        self.janela_editar.title("Editar Produto")
        form_frame = Frame(self.janela_editar)
        form_frame.pack(pady=10)

        campos = [
            ("Nome:", "nome_entry", produto_encontrado[1]),
            ("Validade:", "validade_entry", produto_encontrado[2]),
            ("Segmento:", "segmento_entry", produto_encontrado[3]),
            ("Lote:", "lote_entry", produto_encontrado[4]),
            ("Armazenamento:", "armazenamento_entry", produto_encontrado[5]),
            ("Quantidade:", "quantidade_entry", produto_encontrado[6])
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
        Button(button_frame, text="Salvar", command=lambda: self.atualizar_produto(produto_encontrado[0]), font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
        Button(button_frame, text="Cancelar", command=self.janela_editar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

    def atualizar_produto(self, id_produto):
        nome = self.entries["nome_entry"].get()
        validade = self.entries["validade_entry"].get()
        segmento = self.entries["segmento_entry"].get()
        lote = self.entries["lote_entry"].get()
        armazenamento = self.entries["armazenamento_entry"].get()
        quantidade = self.entries["quantidade_entry"].get()

        if not (validade and segmento and lote and armazenamento and quantidade):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios!")
            return

        if not self.validar_validade(validade):
            messagebox.showerror("Erro", "Data de validade inválida! Use o formato DD/MM/AAAA.")
            return

        if not self.validar_quantidade(quantidade):
            messagebox.showerror("Erro", "Quantidade inválida! Deve ser um número.")
            return

        for i, produto in enumerate(self.produtos):
            if produto[0] == id_produto:
                self.produtos[i] = (id_produto, nome, validade, segmento, lote, armazenamento, float(quantidade))
                break

        self.exibir_tabela(self.container)
        self.janela_editar.destroy()
        messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
