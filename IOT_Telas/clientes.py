from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re


class Cliente:
    def __init__(self):
        # Lista de exemplo de clientes (pode ser vazia)
        self.clientes = [
            
        ]
    
    def validar_telefone(self, telefone):
        # Remover espaços em branco antes de validar
        telefone = telefone.replace(" ", "")
        
        # Expressão regular para validar números de telefone com DDD (2 dígitos) e número (8 ou 9 dígitos)
        padrao_telefone = re.compile(r'^\d{2}\d{8,9}$')
        
        return bool(padrao_telefone.match(telefone))
    
    def validar_email(self, email):
        # Expressão regular para validar e-mails
        padrao_email = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return bool(padrao_email.match(email))
    
    def pagina_cliente(self, container, voltar_func):
        # Limpa o container e exibe a tabela de clientes
        for widget in container.winfo_children():
            widget.destroy()  # Remove qualquer widget anterior
        
        # Exibir a label de gerenciamento
        self.exibir_label(container)
        
        # Exibir a tabela com todos os clientes inicialmente
        self.exibir_tabela(container)
        
        # Instrução sobre o campo Doc
        Label(container, text="Digite o Doc para busca:", font=("Arial", 12), bg="grey").pack(pady=10)

        # Frame para o campo de Doc e os botões lado a lado
        search_frame = Frame(container, bg="grey")
        search_frame.pack(pady=10)

        # Campo para digitar Doc
        self.doc_entry = Entry(search_frame, font=("Arial", 12), width=15)
        self.doc_entry.pack(side=LEFT, padx=5)  # Ajustando para ficar ao lado do botão

        # Botão de pesquisa
        search_button = Button(search_frame, text="Pesquisar", command=self.pesquisar_cliente, font=("Arial", 12))
        search_button.pack(side=LEFT, padx=5)  # Ajustando para ficar ao lado do campo de Doc

        # Botão Excluir ao lado do botão de pesquisa
        delete_button = Button(search_frame, text="Excluir", command=self.excluir_cliente, font=("Arial", 12), width=10)
        delete_button.pack(side=LEFT, padx=5)  # Ajusta a posição para ficar ao lado do botão de pesquisa

        # Botões de Adicionar, Editar
        self.exibir_botoes(container)
        
        # Botão de voltar ao menu principal
        Button(container, text="Voltar ao Home", width=20, command=voltar_func).pack(pady=20)

    def exibir_label(self, container):
        # Label acima da tabela
        label = Label(container, text="Gerenciamento de Cliente", font=("Arial", 16), bg="grey")
        label.pack(pady=10)  # Espaçamento acima da label

    def exibir_tabela(self, container=None):
        # Remover tabela antiga antes de criar uma nova
        for widget in container.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.destroy()  # Remover a tabela existente

        # Definindo o número de linhas como o número de clientes
        num_linhas = len(self.clientes)

        # Criando a nova tabela (Treeview) com altura ajustada
        self.tabela = ttk.Treeview(container, columns=("Nome", "Sobrenome", "Doc", "Logradouro", "Bairro", "Número", "Cidade", "CEP", "Complemento", "Fixo", "Celular", "Email"), show="headings", height=num_linhas)  # Linhas dinâmicas
        self.tabela.pack(pady=10, padx=20)

        # Definindo as colunas da tabela
        self.tabela.heading("Nome", text="Nome")
        self.tabela.heading("Sobrenome", text="Sobrenome")
        self.tabela.heading("Doc", text="Doc")
        self.tabela.heading("Logradouro", text="Logradouro")
        self.tabela.heading("Bairro", text="Bairro")
        self.tabela.heading("Número", text="Número")
        self.tabela.heading("Cidade", text="Cidade")
        self.tabela.heading("CEP", text="CEP")
        self.tabela.heading("Complemento", text="Complemento")
        self.tabela.heading("Fixo", text="Fixo")
        self.tabela.heading("Celular", text="Celular")
        self.tabela.heading("Email", text="Email")

        # Definindo a largura das colunas
        col_widths = [100, 100, 120, 150, 100, 60, 100, 100, 120, 100, 100, 150]
        for col, width in zip(self.tabela["columns"], col_widths):
            self.tabela.column(col, width=width)  # Ajustando a largura das colunas

        # Adicionando todos os clientes à tabela
        for cliente in self.clientes:
            self.tabela.insert("", "end", values=cliente)

    def pesquisar_cliente(self):
        # Obtendo o Doc digitado
        doc_procurado = self.doc_entry.get()

        # Limpar a tabela antes de adicionar os resultados
        for row in self.tabela.get_children():
            self.tabela.delete(row)  # Remove todas as linhas existentes

        # Verificando se o Doc está na lista de clientes
        encontrado = False
        for cliente in self.clientes:
            if cliente[2] == doc_procurado:  # Comparando com o Doc
                # Se o Doc for encontrado, exibe os dados na tabela
                self.tabela.insert("", "end", values=cliente)
                messagebox.showinfo("Cliente Encontrado", f"Cliente: {cliente[0]} {cliente[1]}")
                encontrado = True
                break

        # Caso o Doc não seja encontrado, exibe uma mensagem de erro
        if not encontrado:
            messagebox.showerror("Erro", "Cliente não encontrado.")
            # Em vez de chamar exibir_tabela, vamos limpar a tabela e restaurar todos os clientes
            self.tabela.delete(*self.tabela.get_children())  # Limpa a tabela existente
            for cliente in self.clientes:  # Adiciona todos os cliente novamente
                self.tabela.insert("", "end", values=cliente)

    def exibir_botoes(self, container):
        # Frame para os botões de Adicionar, Editar e Excluir
        botoes_frame = Frame(container, bg="grey")
        botoes_frame.pack(pady=10)
        
        # Botão Adicionar
        add_button = Button(botoes_frame, text="Adicionar", command=self.adicionar_cliente, font=("Arial", 12), width=10)
        add_button.pack(side=LEFT, padx=10)
        
        # Botão Editar
        edit_button = Button(botoes_frame, text="Editar", command=self.editar_cliente, font=("Arial", 12), width=10)
        edit_button.pack(side=LEFT, padx=10)

    def adicionar_cliente(self):
        # Função para abrir a janela de adicionar cliente
        self.janela_adicionar = Toplevel()
        self.janela_adicionar.title("Adicionar Novo cliente")

        # Criando um Frame para organizar os campos
        form_frame = Frame(self.janela_adicionar)
        form_frame.pack(pady=10)

        # Criando os campos de entrada para o novo cliente
        campos = [
            ("Nome:", "nome_entry"),
            ("Sobrenome:", "sobrenome_entry"),
            ("Doc:", "doc_entry_adicionar"),
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
        
        # Adicionando os campos de forma mais organizada
        self.entries = {}
        for i, (label_text, entry_name) in enumerate(campos):
            Label(form_frame, text=label_text).grid(row=i, column=0, sticky=W, pady=5, padx=5)
            entry = Entry(form_frame, font=("Arial", 12))
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries[entry_name] = entry

        # Botões de salvar e cancelar
        button_frame = Frame(self.janela_adicionar)
        button_frame.pack(pady=10)

        # Botão Salvar
        Button(button_frame, text="Salvar", command=self.salvar_cliente, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
        
        # Botão Cancelar
        Button(button_frame, text="Cancelar", command=self.janela_adicionar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

    def salvar_cliente(self):
        # Salvando as informações do novo cliente
        nome = self.entries["nome_entry"].get()
        sobrenome = self.entries["sobrenome_entry"].get()
        doc = self.entries["doc_entry_adicionar"].get()
        logradouro = self.entries["logradouro_entry"].get()
        bairro = self.entries["bairro_entry"].get()
        numero = self.entries["numero_entry"].get()
        cidade = self.entries["cidade_entry"].get()
        cep = self.entries["cep_entry"].get()
        complemento = self.entries["complemento_entry"].get()
        fixo = self.entries["fixo_entry"].get()
        celular = self.entries["celular_entry"].get()
        email = self.entries["email_entry"].get()

        # Verifica se todos os campos obrigatórios foram preenchidos
        if not nome or not sobrenome or not doc or not logradouro or not bairro or not numero or not cidade or not cep or not celular or not email:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios!")
            return

        if not self.validar_telefone(fixo) or not self.validar_telefone(celular):
            messagebox.showerror("Erro", "Número de telefone inválido! Verifique o formato.")
            return

        if not self.validar_email(email):
            messagebox.showerror("Erro", "E-mail inválido!")
            return

        # Verifica se o Doc já foi registrado
        for cliente in self.clientes:
            if cliente[2] == doc:  # O Doc é o terceiro item da tupla
                messagebox.showerror("Erro", "Doc já registrado!")
                return

        # Se tudo estiver correto, adiciona o novo cliente à lista
        self.clientes.append((nome, sobrenome, doc, logradouro, bairro, numero, cidade, cep, complemento, fixo, celular, email))

        # Atualiza a tabela diretamente
        self.exibir_tabela(self.janela_adicionar)

        # Fecha a janela de adicionar
        self.janela_adicionar.destroy()

        # Exibe uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")

    def editar_cliente(self):
        # Lógica para editar um cliente existente
        doc_procurado = self.doc_entry.get()
        cliente_a_editar = None
        for cliente in self.clientes:
            if cliente[2] == doc_procurado:
                cliente_a_editar = cliente
                break
        
        if cliente_a_editar:
            # Abrir a janela de edição
            self.janela_editar = Toplevel()
            self.janela_editar.title("Editar Cliente")

            # Criando um Frame para organizar os campos
            form_frame = Frame(self.janela_editar)
            form_frame.pack(pady=10)

            # Criando os campos de entrada com os valores existentes do cliente
            campos = [
                ("Nome:", "nome_entry", cliente_a_editar[0]),
                ("Sobrenome:", "sobrenome_entry", cliente_a_editar[1]),
                ("Doc:", "doc_entry_editar", cliente_a_editar[2]),
                ("Logradouro:", "logradouro_entry", cliente_a_editar[3]),
                ("Bairro:", "bairro_entry", cliente_a_editar[4]),
                ("Número:", "numero_entry", cliente_a_editar[5]),
                ("Cidade:", "cidade_entry", cliente_a_editar[6]),
                ("CEP:", "cep_entry", cliente_a_editar[7]),
                ("Complemento:", "complemento_entry", cliente_a_editar[8]),
                ("Fixo:", "fixo_entry", cliente_a_editar[9]),
                ("Celular:", "celular_entry", cliente_a_editar[10]),
                ("Email:", "email_entry", cliente_a_editar[11])
            ]
            
            # Adicionando os campos com valores existentes
            self.entries = {}
            for i, (label_text, entry_name, entry_value) in enumerate(campos):
                Label(form_frame, text=label_text).grid(row=i, column=0, sticky=W, pady=5, padx=5)
                entry = Entry(form_frame, font=("Arial", 12))
                entry.insert(0, entry_value)
                entry.grid(row=i, column=1, pady=5, padx=5)
                self.entries[entry_name] = entry

            # Botões de salvar e cancelar
            button_frame = Frame(self.janela_editar)
            button_frame.pack(pady=10)

            # Botão Salvar
            Button(button_frame, text="Salvar", command=lambda: self.salvar_edicao(cliente_a_editar), font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
            
            # Botão Cancelar
            Button(button_frame, text="Cancelar", command=self.janela_editar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

        else:
            messagebox.showerror("Erro", "Cliente não encontrado!")

    def salvar_edicao(self, cliente_antigo):
        # Atualiza os dados do cliente com as novas informações
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

        if nome and sobrenome and logradouro and bairro and numero and cidade and cep and fixo and celular and email:
            # Atualiza os dados do cliente
            idx = self.clientes.index(cliente_antigo)
            self.clientes[idx] = (nome, sobrenome, cliente_antigo[2], logradouro, bairro, numero, cidade, cep, complemento, fixo, celular, email)

            # Atualiza a tabela diretamente
            self.exibir_tabela(self.janela_editar)

            # Fecha a janela de edição
            self.janela_editar.destroy()

            # Exibe mensagem de sucesso
            messagebox.showinfo("Sucesso", "Cliente editado com sucesso!")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

    def excluir_cliente(self):
        # Função para excluir um cliente baseado no Doc
        doc_procurado = self.doc_entry.get()

        # Verificando se o Doc foi preenchido
        if not doc_procurado:
            messagebox.showerror("Erro", "Digite um Doc para excluir!")
            return

        # Exibe a caixa de confirmação
        confirmacao = messagebox.askyesno("Confirmação", "Você tem certeza de que deseja excluir este cliente?")

        if confirmacao:  # Se o usuário clicar em 'Sim'
            for cliente in self.clientes:
                if cliente[2] == doc_procurado:
                    self.clientes.remove(cliente)
                    self.exibir_tabela(self.janela_adicionar)
                    messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
                    return

            # Caso o Doc não seja encontrado
            messagebox.showerror("Erro", "Cliente não encontrado!")
        else:
            messagebox.showinfo("Cancelado", "A exclusão foi cancelada.")
