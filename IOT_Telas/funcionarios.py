from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

class Funcionario:
    def __init__(self):
        self.funcionarios = []
        self.container = None

    def validar_cpf(self, cpf):
        cpf = re.sub(r'\D', '', cpf)
        return len(cpf) == 11 and cpf.isdigit()

    def validar_telefone(self, telefone):
        telefone = telefone.replace(" ", "")
        padrao_telefone = re.compile(r'^\d{2}\d{8,9}$')
        return bool(padrao_telefone.match(telefone))

    def validar_email(self, email):
        padrao_email = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return bool(padrao_email.match(email))

    def pagina_funcionario(self, container, voltar_func):
        self.container = container

        for widget in container.winfo_children():
            widget.destroy()
        
        self.exibir_label(container)
        self.exibir_tabela(container)

        Label(container, text="Digite o CPF para busca:", font=("Arial", 12), bg="grey").pack(pady=10)
        search_frame = Frame(container, bg="grey")
        search_frame.pack(pady=10)
        self.cpf_entry = Entry(search_frame, font=("Arial", 12), width=15)
        self.cpf_entry.pack(side=LEFT, padx=5)
        search_button = Button(search_frame, text="Pesquisar", command=self.pesquisar_funcionario, font=("Arial", 12))
        search_button.pack(side=LEFT, padx=5)
        delete_button = Button(search_frame, text="Excluir", command=self.excluir_funcionario, font=("Arial", 12))
        delete_button.pack(side=LEFT, padx=5)
        
        self.exibir_botoes(container)
        Button(container, text="Voltar ao Home", width=20, command=voltar_func).pack(pady=20)

    def exibir_label(self, container):
        label = Label(container, text="Gerenciamento de Funcionário", font=("Arial", 16), bg="grey")
        label.pack(pady=10)

    def exibir_tabela(self, container=None):
        for widget in container.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.destroy()

        num_linhas = len(self.funcionarios)
        self.tabela = ttk.Treeview(container, columns=("Nome", "Sobrenome", "CPF", "Cargo", "Logadouro", "Bairro", "Numero", "Roteiro", "Cidade", "Cep", "Complemento", "Telefone", "E-mail"), show="headings", height=num_linhas)
        self.tabela.pack(pady=10, padx=20)

        col_names = ["Nome", "Sobrenome", "CPF", "Cargo", "Logadouro", "Bairro", "Numero", "Roteiro", "Cidade", "Cep", "Complemento", "Telefone", "E-mail"]
        for col_name in col_names:
            self.tabela.heading(col_name, text=col_name)
        
        col_widths = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        for col, width in zip(self.tabela["columns"], col_widths):
            self.tabela.column(col, width=width)
        
        for funcionario in self.funcionarios:
            self.tabela.insert("", "end", values=funcionario)


    def exibir_botoes(self, container):
        botoes_frame = Frame(container, bg="grey")
        botoes_frame.pack(pady=10)
        add_button = Button(botoes_frame, text="Adicionar", command=self.adicionar_funcionario, font=("Arial", 12), width=10)
        add_button.pack(side=LEFT, padx=10)
        edit_button = Button(botoes_frame, text="Editar", command=self.editar_funcionario, font=("Arial", 12), width=10)
        edit_button.pack(side=LEFT, padx=10)

    def adicionar_funcionario(self):
        self.janela_adicionar = Toplevel()
        self.janela_adicionar.title("Adicionar Novo Funcionário")
        form_frame = Frame(self.janela_adicionar)
        form_frame.pack(pady=10)

        campos = [
            ("Nome:", "nome_entry"),
            ("Sobrenome:", "sobrenome_entry"),
            ("CPF:", "cpf_entry"),
            ("Cargo:", "cargo_entry"),
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
        Button(button_frame, text="Salvar", command=self.salvar_funcionario, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
        Button(button_frame, text="Cancelar", command=self.janela_adicionar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

    def salvar_funcionario(self):
        nome = self.entries["nome_entry"].get()
        sobrenome = self.entries["sobrenome_entry"].get()
        cpf = self.entries["cpf_entry"].get()
        cargo = self.entries["cargo_entry"].get()
        logradouro = self.entries["logradouro_entry"].get()
        bairro = self.entries["bairro_entry"].get()
        numero = self.entries["numero_entry"].get()
        cidade = self.entries["cidade_entry"].get()
        cep = self.entries["cep_entry"].get()
        complemento = self.entries["complemento_entry"].get()
        fixo = self.entries["fixo_entry"].get()
        celular = self.entries["celular_entry"].get()
        email = self.entries["email_entry"].get()

        if not (nome and sobrenome and cpf and cargo and logradouro and bairro and numero and cidade and cep and celular and email):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios!")
            return

        if not self.validar_cpf(cpf):
                messagebox.showerror("Erro", "CPF inválido!")
                return
    
        if not self.validar_telefone(celular):
            messagebox.showerror("Erro", "Número de celular inválido! Verifique o formato.")
            return

        if not self.validar_email(email):
            messagebox.showerror("Erro", "E-mail inválido!")
            return

        for funcionario in self.funcionarios:
            if funcionario[2] == cpf:
                messagebox.showerror("Erro", "CPF já registrado!")
                return

        self.funcionarios.append((nome, sobrenome, cpf, cargo, logradouro, bairro, numero, cidade, cep, complemento, fixo, celular, email))
        self.exibir_tabela(self.container)
        self.janela_adicionar.destroy()
        messagebox.showinfo("Sucesso", "Funcionário adicionado com sucesso!")

        
    def pesquisar_funcionario(self):
        cpf_procurado = self.cpf_entry.get()
        if not cpf_procurado:
            messagebox.showerror("Erro", "Digite um CPF para pesquisar!")
            return

        for row in self.tabela.get_children():
            self.tabela.delete(row)

        encontrado = False
        for funcionario in self.funcionarios:
            if str(funcionario[2]) == cpf_procurado:
                self.tabela.insert("", "end", values=funcionario)
                messagebox.showinfo("Funcionário Encontrado", f"Funcionário: {funcionario[0]}, {funcionario[1]}")
                encontrado = True
                break

        if not encontrado:
            messagebox.showerror("Erro", "Funcionário não encontrado.")
            self.tabela.delete(*self.tabela.get_children())
            for funcionario in self.funcionarios:
                self.tabela.insert("", "end", values=funcionario)

    def excluir_funcionario(self):
        cpf_procurado = self.cpf_entry.get()
        if not cpf_procurado:
            messagebox.showerror("Erro", "Digite um CPF para excluir!")
            return
        
        for i, Funcionario in enumerate(self.funcionarios):
            if str(Funcionario[2]) == cpf_procurado:
                del self.funcionarios[i]
                self.exibir_tabela(self.container)
                messagebox.showinfo("Sucesso", "Funcionário excluído com sucesso!")
                return

        messagebox.showerror("Erro", "Funcionário não encontrado!")

    def editar_funcionario(self):
        cpf_procurado = self.cpf_entry.get()
        if not cpf_procurado:
            messagebox.showerror("Erro", "Digite um CPF para editar!")
            return

        funcionario_encontrado = None
        for funcionario in self.funcionarios:
            if str(funcionario[2]) == cpf_procurado:
                funcionario_encontrado = funcionario
                break

        if not funcionario_encontrado:
            messagebox.showerror("Erro", "Funcionário não encontrado!")
            return

        self.janela_editar = Toplevel()
        self.janela_editar.title("Editar Funcionário")
        form_frame = Frame(self.janela_editar)
        form_frame.pack(pady=10)

        campos = [
            ("Nome:", "nome_entry", funcionario_encontrado[0]),
            ("Sobrenome:", "sobrenome_entry", funcionario_encontrado[1]),
            ("Cargo:", "cargo_entry", funcionario_encontrado[3]),
            ("Logradouro:", "logradouro_entry", funcionario_encontrado[4]),
            ("Bairro:", "bairro_entry", funcionario_encontrado[5]),
            ("Número:", "numero_entry", funcionario_encontrado[6]),
            ("Cidade:", "cidade_entry", funcionario_encontrado[7]),
            ("CEP:", "cep_entry", funcionario_encontrado[8]),
            ("Complemento (Opcional):", "complemento_entry", funcionario_encontrado[9]),
            ("Fixo (Opcional):", "fixo_entry", funcionario_encontrado[10]),
            ("Celular:", "celular_entry", funcionario_encontrado[11]),
            ("Email:", "email_entry", funcionario_encontrado[12])
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
        Button(button_frame, text="Salvar", command=lambda: self.atualizar_funcionario(funcionario_encontrado[2]), font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
        Button(button_frame, text="Cancelar", command=self.janela_editar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

    def atualizar_funcionario(self, cpf_encontrado):
        nome = self.entries["nome_entry"].get()
        sobrenome = self.entries["sobrenome_entry"].get()
        cargo = self.entries["cargo_entry"].get()
        logradouro = self.entries["logradouro_entry"].get()
        bairro = self.entries["bairro_entry"].get()
        numero = self.entries["numero_entry"].get()
        cidade = self.entries["cidade_entry"].get()
        cep = self.entries["cep_entry"].get()
        complemento = self.entries["complemento_entry"].get()
        fixo = self.entries["fixo_entry"].get()
        celular = self.entries["celular_entry"].get()
        email = self.entries["email_entry"].get()

        if not (nome and sobrenome and cargo and logradouro and bairro and numero and cidade and cep and celular and email):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios!")
            return

        if not self.validar_telefone(celular):
            messagebox.showerror("Erro", "Número de celular inválido! Verifique o formato.")
            return

        if not self.validar_email(email):
            messagebox.showerror("Erro", "E-mail inválido!")
            return
        
        for i, funcionario in enumerate(self.funcionarios):
            if funcionario[2] == cpf_encontrado:
                self.funcionarios[i] = (nome, sobrenome, funcionario[2], cargo, logradouro, bairro, numero, cidade, cep, complemento, fixo, celular, email)
                break

        self.exibir_tabela(self.container)
        self.janela_editar.destroy()
        messagebox.showinfo("Sucesso", "Funcionário atualizado com sucesso!")

