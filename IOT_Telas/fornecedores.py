from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

class Fornecedor:
    def __init__(self):
        self.fornecedores = []
        self.container = None

    def validar_cnpj(self, cnpj):
        cnpj = re.sub(r'\D', '', cnpj)
        return len(cnpj) == 14 and cnpj.isdigit()

    def validar_telefone(self, telefone):
        telefone = telefone.replace(" ", "")
        padrao_telefone = re.compile(r'^\d{2}\d{8,9}$')
        return bool(padrao_telefone.match(telefone))

    def validar_email(self, email):
        padrao_email = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return bool(padrao_email.match(email))

    def pagina_fornecedor(self, container, voltar_func):
        self.container = container

        for widget in container.winfo_children():
            widget.destroy()
        
        self.exibir_label(container)
        self.exibir_tabela(container)

        Label(container, text="Digite o CNPJ para busca:", font=("Arial", 12), bg="grey").pack(pady=10)
        search_frame = Frame(container, bg="grey")
        search_frame.pack(pady=10)
        self.cnpj_entry = Entry(search_frame, font=("Arial", 12), width=15)
        self.cnpj_entry.pack(side=LEFT, padx=5)
        search_button = Button(search_frame, text="Pesquisar", command=self.pesquisar_fornecedor, font=("Arial", 12))
        search_button.pack(side=LEFT, padx=5)
        delete_button = Button(search_frame, text="Excluir", command=self.excluir_fornecedor, font=("Arial", 12))
        delete_button.pack(side=LEFT, padx=5)
        
        self.exibir_botoes(container)
        Button(container, text="Voltar ao Home", width=20, command=voltar_func).pack(pady=20)

    def exibir_label(self, container):
        label = Label(container, text="Gerenciamento de Fornecedor", font=("Arial", 16), bg="grey")
        label.pack(pady=10)

    def exibir_tabela(self, container=None):
        for widget in container.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.destroy()

        num_linhas = len(self.fornecedores)
        self.tabela = ttk.Treeview(container, columns=("Nome", "Sobrenome", "Razão social" ,"CNPJ", "Logadouro", "Bairro", "Numero", "Roteiro", "Cidade", "Cep", "Complemento", "Telefone", "E-mail"), show="headings", height=num_linhas)
        self.tabela.pack(pady=10, padx=20)

        col_names = ["Nome", "Sobrenome", "Razão social" ,"CNPJ", "Logadouro", "Bairro", "Numero", "Roteiro", "Cidade", "Cep", "Complemento", "Telefone", "E-mail"]
        for col_name in col_names:
            self.tabela.heading(col_name, text=col_name)
        
        col_widths = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        for col, width in zip(self.tabela["columns"], col_widths):
            self.tabela.column(col, width=width)
        
        for fornecedor in self.fornecedores:
            self.tabela.insert("", "end", values=fornecedor)


    def exibir_botoes(self, container):
        botoes_frame = Frame(container, bg="grey")
        botoes_frame.pack(pady=10)
        add_button = Button(botoes_frame, text="Adicionar", command=self.adicionar_fornecedor, font=("Arial", 12), width=10)
        add_button.pack(side=LEFT, padx=10)
        edit_button = Button(botoes_frame, text="Editar", command=self.editar_fornecedor, font=("Arial", 12), width=10)
        edit_button.pack(side=LEFT, padx=10)

    def adicionar_fornecedor(self):
        self.janela_adicionar = Toplevel()
        self.janela_adicionar.title("Adicionar Novo Fornecedor")
        form_frame = Frame(self.janela_adicionar)
        form_frame.pack(pady=10)

        campos = [
            ("Nome:", "nome_entry"),
            ("Sobrenome:", "sobrenome_entry"),
            ("Razão social:", "razao_social_entry"),
            ("CNPJ:", "cnpj_entry"),
            ("Logradouro:", "logradouro_entry"),
            ("Bairro:", "bairro_entry"),
            ("Número:", "numero_entry"),
            ("Cidade:", "cidade_entry"),
            ("CEP:", "cep_entry"),
            ("Complemento (Opcional):", "complemento_entry"),
            ("Fixo (Opcional):", "fixo_entry"),
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
        Button(button_frame, text="Salvar", command=self.salvar_fornecedor, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
        Button(button_frame, text="Cancelar", command=self.janela_adicionar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

    def salvar_fornecedor(self):
        nome = self.entries["nome_entry"].get()
        sobrenome = self.entries["sobrenome_entry"].get()
        razao_social = self.entries["razao_social_entry"].get()
        cnpj = self.entries["cnpj_entry"].get()
        logradouro = self.entries["logradouro_entry"].get()
        bairro = self.entries["bairro_entry"].get()
        numero = self.entries["numero_entry"].get()
        cidade = self.entries["cidade_entry"].get()
        cep = self.entries["cep_entry"].get()
        complemento = self.entries["complemento_entry"].get()
        fixo = self.entries["fixo_entry"].get()
        celular = self.entries["celular_entry"].get()
        email = self.entries["email_entry"].get()

        if not (nome and sobrenome and razao_social and cnpj and logradouro and bairro and numero and cidade and cep and celular and email):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios!")
            return

        if not self.validar_cnpj(cnpj):
                messagebox.showerror("Erro", "CNPJ inválido!")
                return
    
        if not self.validar_telefone(celular):
            messagebox.showerror("Erro", "Número de celular inválido! Verifique o formato.")
            return

        if not self.validar_email(email):
            messagebox.showerror("Erro", "E-mail inválido!")
            return

        for fornecedor in self.fornecedores:
            if fornecedor[3] == cnpj:
                messagebox.showerror("Erro", "CNPJ já registrado!")
                return

        self.fornecedores.append((nome, sobrenome, razao_social ,cnpj, logradouro, bairro, numero, cidade, cep, complemento, fixo, celular, email))
        self.exibir_tabela(self.container)
        self.janela_adicionar.destroy()
        messagebox.showinfo("Sucesso", "Fornecedor adicionado com sucesso!")

        
    def pesquisar_fornecedor(self):
        cnpj_procurado = self.cnpj_entry.get()
        if not cnpj_procurado:
            messagebox.showerror("Erro", "Digite um CNPJ para pesquisar!")
            return

        for row in self.tabela.get_children():
            self.tabela.delete(row)

        encontrado = False
        for fornecedor in self.fornecedores:
            if str(fornecedor[3]) == cnpj_procurado:
                self.tabela.insert("", "end", values=fornecedor)
                messagebox.showinfo("Fornecedor Encontrado", f"Fornecedor: {fornecedor[0]}, {fornecedor[1]}")
                encontrado = True
                break

        if not encontrado:
            messagebox.showerror("Erro", "Fornecedor não encontrado.")
            self.tabela.delete(*self.tabela.get_children())
            for fornecedor in self.fornecedores:
                self.tabela.insert("", "end", values=fornecedor)

    def excluir_fornecedor(self):
        cnpj_procurado = self.cnpj_entry.get()
        if not cnpj_procurado:
            messagebox.showerror("Erro", "Digite um CNPJ para excluir!")
            return
        
        for i, fornecedor in enumerate(self.fornecedores):
            if str(fornecedor[3]) == cnpj_procurado:
                del self.fornecedores[i]
                self.exibir_tabela(self.container)
                messagebox.showinfo("Sucesso", "Fornecedor excluído com sucesso!")
                return

        messagebox.showerror("Erro", "Fornecedor não encontrado!")

    def editar_fornecedor(self):
        cnpj_procurado = self.cnpj_entry.get()
        if not cnpj_procurado:
            messagebox.showerror("Erro", "Digite um CNPJ para editar!")
            return

        fornecedor_encontrado = None
        for fornecedor in self.fornecedores:
            if str(fornecedor[3]) == cnpj_procurado:
                fornecedor_encontrado = fornecedor
                break

        if not fornecedor_encontrado:
            messagebox.showerror("Erro", "Fornecedor não encontrado!")
            return

        self.janela_editar = Toplevel()
        self.janela_editar.title("Editar Fornecedor")
        form_frame = Frame(self.janela_editar)
        form_frame.pack(pady=10)

        campos = [
            ("Nome:", "nome_entry", fornecedor_encontrado[0]),
            ("Sobrenome:", "sobrenome_entry", fornecedor_encontrado[1]),
            ("Razão social:", "razao_social_entry", fornecedor_encontrado[2]),
            ("Logradouro:", "logradouro_entry", fornecedor_encontrado[4]),
            ("Bairro:", "bairro_entry", fornecedor_encontrado[5]),
            ("Número:", "numero_entry", fornecedor_encontrado[6]),
            ("Cidade:", "cidade_entry", fornecedor_encontrado[7]),
            ("CEP:", "cep_entry", fornecedor_encontrado[8]),
            ("Complemento (Opcional):", "complemento_entry", fornecedor_encontrado[9]),
            ("Fixo (Opcional):", "fixo_entry", fornecedor_encontrado[10]),
            ("Celular:", "celular_entry", fornecedor_encontrado[11]),
            ("Email:", "email_entry", fornecedor_encontrado[12])
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
        Button(button_frame, text="Salvar", command=lambda: self.atualizar_fornecedor(fornecedor_encontrado[3]), font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
        Button(button_frame, text="Cancelar", command=self.janela_editar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

    def atualizar_fornecedor(self, cnpj_encontrado):
        nome = self.entries["nome_entry"].get()
        sobrenome = self.entries["sobrenome_entry"].get()
        razao_social = self.entries["razao_social_entry"].get()
        logradouro = self.entries["logradouro_entry"].get()
        bairro = self.entries["bairro_entry"].get()
        numero = self.entries["numero_entry"].get()
        cidade = self.entries["cidade_entry"].get()
        cep = self.entries["cep_entry"].get()
        complemento = self.entries["complemento_entry"].get()
        fixo = self.entries["fixo_entry"].get()
        celular = self.entries["celular_entry"].get()
        email = self.entries["email_entry"].get()

        if not (nome and sobrenome and razao_social and logradouro and bairro and numero and cidade and cep and celular and email):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios!")
            return

        if not self.validar_telefone(celular):
            messagebox.showerror("Erro", "Número de celular inválido! Verifique o formato.")
            return

        if not self.validar_email(email):
            messagebox.showerror("Erro", "E-mail inválido!")
            return
        
        for i, fornecedor in enumerate(self.fornecedores):
            if fornecedor[3] == cnpj_encontrado:
                self.fornecedores[i] = (nome, sobrenome, fornecedor[3], logradouro, bairro, numero, cidade, cep, complemento, fixo, celular, email)
                break

        self.exibir_tabela(self.container)
        self.janela_editar.destroy()
        messagebox.showinfo("Sucesso", "Fornecedor atualizado com sucesso!")