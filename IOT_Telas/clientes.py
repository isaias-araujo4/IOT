from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

class Cliente:
    def __init__(self):
        self.clientes = []
        self.container = None

    def validar_doc(self, doc): 
        return doc.isdigit()

    def validar_telefone(self, telefone):
        telefone = telefone.replace(" ", "")
        padrao_telefone = re.compile(r'^\d{2}\d{8,9}$')
        return bool(padrao_telefone.match(telefone))

    def validar_email(self, email):
        padrao_email = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return bool(padrao_email.match(email))

    def pagina_cliente(self, container, voltar_func):
        self.container = container

        for widget in container.winfo_children():
            widget.destroy()
        
        self.exibir_label(container)
        self.exibir_tabela(container)

        Label(container, text="Digite o CPF para busca:", font=("Arial", 12), bg="grey").pack(pady=10)
        search_frame = Frame(container, bg="grey")
        search_frame.pack(pady=10)
        self.doc_entry = Entry(search_frame, font=("Arial", 12), width=15)
        self.doc_entry.pack(side=LEFT, padx=5)
        search_button = Button(search_frame, text="Pesquisar", command=self.pesquisar_cliente, font=("Arial", 12))
        search_button.pack(side=LEFT, padx=5)
        delete_button = Button(search_frame, text="Excluir", command=self.excluir_cliente, font=("Arial", 12))
        delete_button.pack(side=LEFT, padx=5)
        
        self.exibir_botoes(container)
        Button(container, text="Voltar ao Home", width=20, command=voltar_func).pack(pady=20)

    def exibir_label(self, container):
        label = Label(container, text="Gerenciamento de Cliente", font=("Arial", 16), bg="grey")
        label.pack(pady=10)

    def exibir_tabela(self, container=None):
        for widget in container.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.destroy()

        num_linhas = len(self.clientes)
        self.tabela = ttk.Treeview(container, columns=("Nome", "Sobrenome", "Doc", "Logadouro", "Bairro", "Numero", "Roteiro", "Cidade", "Cep", "Complemento", "Telefone", "E-mail"), show="headings", height=num_linhas)
        self.tabela.pack(pady=10, padx=20)

        col_names = ["Nome", "Sobrenome", "Doc", "Logadouro", "Bairro", "Numero", "Roteiro", "Cidade", "Cep", "Complemento", "Telefone", "E-mail"]
        for col_name in col_names:
            self.tabela.heading(col_name, text=col_name)
        
        col_widths = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        for col, width in zip(self.tabela["columns"], col_widths):
            self.tabela.column(col, width=width)
        
        for cliente in self.clientes:
            self.tabela.insert("", "end", values=cliente)


    def exibir_botoes(self, container):
        botoes_frame = Frame(container, bg="grey")
        botoes_frame.pack(pady=10)
        add_button = Button(botoes_frame, text="Adicionar", command=self.adicionar_cliente, font=("Arial", 12), width=10)
        add_button.pack(side=LEFT, padx=10)
        edit_button = Button(botoes_frame, text="Editar", command=self.editar_cliente, font=("Arial", 12), width=10)
        edit_button.pack(side=LEFT, padx=10)

    def adicionar_cliente(self):
        self.janela_adicionar = Toplevel()
        self.janela_adicionar.title("Adicionar Novo Cliente")
        form_frame = Frame(self.janela_adicionar)
        form_frame.pack(pady=10)

        campos = [
            ("Nome:", "nome_entry"),
            ("Sobrenome:", "sobrenome_entry"),
            ("Doc:", "doc_entry"),
            ("Logradouro:", "logradouro_entry"),
            ("Bairro:", "bairro_entry"),
            ("Número:", "numero_entry"),
            ("Cidade:", "cidade_entry"),
            ("CEP:", "cep_entry"),
            ("Complemento:", "complemento_entry"),
            ("Fixo:", "fixo_entry"),
            ("Celular:", "celular_entry"),
            ("Email:", "email_entry")
        ]

        self.entries = {}
        for i, (label_text, entry_name) in enumerate(campos):
            Label(form_frame, text=label_text).grid(row=i, column=0, sticky=W, pady=5, padx=5)
            entry = Entry(form_frame, font=("Arial", 12))
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries[entry_name] = entry

        button_frame = Frame(self.janela_adicionar)
        button_frame.pack(pady=10)
        Button(button_frame, text="Salvar", command=self.salvar_cliente, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
        Button(button_frame, text="Cancelar", command=self.janela_adicionar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

    def salvar_cliente(self):
        nome = self.entries["nome_entry"].get()
        sobrenome = self.entries["sobrenome_entry"].get()
        doc = self.entries["doc_entry"].get()
        logradouro = self.entries["logradouro_entry"].get()
        bairro = self.entries["bairro_entry"].get()
        numero = self.entries["numero_entry"].get()
        cidade = self.entries["cidade_entry"].get()
        cep = self.entries["cep_entry"].get()
        complemento = self.entries["complemento_entry"].get()
        fixo = self.entries["fixo_entry"].get()
        celular = self.entries["celular_entry"].get()
        email = self.entries["email_entry"].get()

        if not (nome and sobrenome and doc and logradouro and bairro and numero and cidade and cep and celular and email):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios!")
            return

        if not self.validar_doc(doc):  
            messagebox.showerror("Erro", "Doc inválido! O Doc deve conter apenas números.") 
            return 
    
        if not self.validar_telefone(celular):
            messagebox.showerror("Erro", "Número de celular inválido! Verifique o formato.")
            return

        if not self.validar_email(email):
            messagebox.showerror("Erro", "E-mail inválido!")
            return

        for cliente in self.clientes:
            if cliente[2] == doc:
                messagebox.showerror("Erro", "Doc já registrado!")
                return

        self.clientes.append((nome, sobrenome, doc, logradouro, bairro, numero, cidade, cep, complemento, fixo, celular, email))
        self.exibir_tabela(self.container)
        self.janela_adicionar.destroy()
        messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")

        
    def pesquisar_cliente(self):
        doc_procurado = self.doc_entry.get()
        if not doc_procurado:
            messagebox.showerror("Erro", "Digite um Doc para pesquisar!")
            return

        for row in self.tabela.get_children():
            self.tabela.delete(row)

        encontrado = False
        for cliente in self.clientes:
            if str(cliente[2]) == doc_procurado:
                self.tabela.insert("", "end", values=cliente)
                messagebox.showinfo("Cliente Encontrado", f"Cliente: {cliente[0]}, {cliente[1]}")
                encontrado = True
                break

        if not encontrado:
            messagebox.showerror("Erro", "Cliente não encontrado.")
            self.tabela.delete(*self.tabela.get_children())
            for cliente in self.clientes:
                self.tabela.insert("", "end", values=cliente)

    def excluir_cliente(self):
        doc_procurado = self.doc_entry.get()
        if not doc_procurado:
            messagebox.showerror("Erro", "Digite um Doc para excluir!")
            return
        
        for i, Cliente in enumerate(self.clientes):
            if str(Cliente[2]) == doc_procurado:
                del self.clientes[i]
                self.exibir_tabela(self.container)
                messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
                return

        messagebox.showerror("Erro", "Cliente não encontrado!")

    def editar_cliente(self):
        doc_procurado = self.doc_entry.get()
        if not doc_procurado:
            messagebox.showerror("Erro", "Digite um Doc para editar!")
            return

        cliente_encontrado = None
        for cliente in self.clientes:
            if str(cliente[2]) == doc_procurado:
                cliente_encontrado = cliente
                break

        if not cliente_encontrado:
            messagebox.showerror("Erro", "Cliente não encontrado!")
            return

        self.janela_editar = Toplevel()
        self.janela_editar.title("Editar Cliente")
        form_frame = Frame(self.janela_editar)
        form_frame.pack(pady=10)

        campos = [
            ("Nome:", "nome_entry", cliente_encontrado[0]),
            ("Sobrenome:", "sobrenome_entry", cliente_encontrado[1]),
            ("Logradouro:", "logradouro_entry", cliente_encontrado[3]),
            ("Bairro:", "bairro_entry", cliente_encontrado[4]),
            ("Número:", "numero_entry", cliente_encontrado[5]),
            ("Cidade:", "cidade_entry", cliente_encontrado[5]),
            ("CEP:", "cep_entry", cliente_encontrado[7]),
            ("Complemento:", "complemento_entry", cliente_encontrado[8]),
            ("Fixo:", "fixo_entry", cliente_encontrado[9]),
            ("Celular:", "celular_entry", cliente_encontrado[10]),
            ("Email:", "email_entry", cliente_encontrado[11])
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
        Button(button_frame, text="Salvar", command=lambda: self.atualizar_cliente(cliente_encontrado[2]), font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
        Button(button_frame, text="Cancelar", command=self.janela_editar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

    def atualizar_cliente(self, doc_encontrado):
        nome = self.entries["nome_entry"].get()
        sobrenome = self.entries["sobrenome_entry"].get()
        logradouro = self.entries["logradouro_entry"].get()
        bairro = self.entries["bairro_entry"].get()
        numero = self.entries["numero_entry"].get()
        cidade = self.entries["cidade_entry"].get()
        cep = self.entries["cep_entry"].get()
        complemento = self.entries["complemento_entry"].get()
        fixo = self.entries["fixo_entry"].get()
        celular = self.entries["celular_entry"].get()
        email = self.entries["email_entry"].get()

        if not (nome and sobrenome and logradouro and bairro and numero and cidade and cep and celular and email):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios!")
            return

        if not self.validar_telefone(celular):
            messagebox.showerror("Erro", "Número de celular inválido! Verifique o formato.")
            return

        if not self.validar_email(email):
            messagebox.showerror("Erro", "E-mail inválido!")
            return
        
        for i, cliente in enumerate(self.clientes):
            if cliente[2] == doc_encontrado:
                self.clientes[i] = (nome, sobrenome, cliente[2], logradouro, bairro, numero, cidade, cep, complemento, fixo, celular, email)
                break

        self.exibir_tabela(self.container)
        self.janela_editar.destroy()
        messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")

