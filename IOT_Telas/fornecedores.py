from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re


class Fornecedor:
    def __init__(self):
        # Lista de exemplo de fornecedor (pode ser vazia)
        self.fornecedores = [
        ]
    
    def validar_cnpj(self, cnpj):
        # Remove qualquer caractere não numérico
        cnpj = re.sub(r'\D', '', cnpj)

        # Verifica se o CNPJ tem 14 dígitos
        if len(cnpj) != 14 or not cnpj.isdigit():
            return False

        # Implementar a validação do CNPJ (não é simples, pois é necessário verificar os dois últimos dígitos)
        # Aqui, é feita uma validação simplificada de CNPJ
        return True
    
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
    
    def pagina_fornecedor(self, container, voltar_func):
        # Limpa o container e exibe a tabela de fornecedor
        for widget in container.winfo_children():
            widget.destroy()  # Remove qualquer widget anterior
        
        # Exibir a label de gerenciamento
        self.exibir_label(container)
        
        # Exibir a tabela com todos os fornecedores inicialmente
        self.exibir_tabela(container)
        
        # Instrução sobre o campo CNPJ
        Label(container, text="Digite o CNPJ para busca:", font=("Arial", 12), bg="grey").pack(pady=10)

        # Frame para o campo de CNPJ e os botões lado a lado
        search_frame = Frame(container, bg="grey")
        search_frame.pack(pady=10)

        # Campo para digitar CNPJ
        self.cnpj_entry = Entry(search_frame, font=("Arial", 12), width=15)
        self.cnpj_entry.pack(side=LEFT, padx=5)  # Ajustando para ficar ao lado do botão

        # Botão de pesquisa
        search_button = Button(search_frame, text="Pesquisar", command=self.pesquisar_fornecedor, font=("Arial", 12))
        search_button.pack(side=LEFT, padx=5)  # Ajustando para ficar ao lado do campo de CNPJ

        # Botão Excluir ao lado do botão de pesquisa
        delete_button = Button(search_frame, text="Excluir", command=self.excluir_fornecedor, font=("Arial", 12), width=10)
        delete_button.pack(side=LEFT, padx=5)  # Ajusta a posição para ficar ao lado do botão de pesquisa

        # Botões de Adicionar, Editar
        self.exibir_botoes(container)
        
        # Botão de voltar ao menu principal
        Button(container, text="Voltar ao Home", width=20, command=voltar_func).pack(pady=20)

    def exibir_label(self, container):
        # Label acima da tabela
        label = Label(container, text="Gerenciamento de Fornecedor", font=("Arial", 16), bg="grey")
        label.pack(pady=10)  # Espaçamento acima da label

    def exibir_tabela(self, container=None):
        # Remover tabela antiga antes de criar uma nova
        for widget in container.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.destroy()  # Remover a tabela existente

        # Definindo o número de linhas como o número de fornecedores
        num_linhas = len(self.fornecedores)

        # Criando a nova tabela (Treeview) com altura ajustada
        self.tabela = ttk.Treeview(container, columns=("Nome", "Sobrenome", "CNPJ", "Razão social", "Logradouro", "Bairro", "Número", "Cidade", "CEP", "Complemento", "Fixo", "Celular", "Email"), show="headings", height=num_linhas)  # Linhas dinâmicas
        self.tabela.pack(pady=10, padx=20)

        # Definindo as colunas da tabela
        self.tabela.heading("Nome", text="Nome")
        self.tabela.heading("Sobrenome", text="Sobrenome")
        self.tabela.heading("CNPJ", text="CNPJ")
        self.tabela.heading("Razão social", text="Razão social")
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
        col_widths = [100, 100, 120, 120, 150, 100, 60, 100, 100, 120, 100, 100, 150]
        for col, width in zip(self.tabela["columns"], col_widths):
            self.tabela.column(col, width=width)  # Ajustando a largura das colunas

        # Adicionando todos os fornecedoress à tabela
        for fornecedor in self.fornecedores:
            self.tabela.insert("", "end", values=fornecedor)

    def pesquisar_fornecedor(self):
        # Obtendo o CNPJ digitado
        cnpj_procurado = self.cnpj_entry.get()

        # Limpar a tabela antes de adicionar os resultados
        for row in self.tabela.get_children():
            self.tabela.delete(row)  # Remove todas as linhas existentes

        # Verificando se o CNPJ está na lista de funcionários
        encontrado = False
        for fornecedor in self.fornecedores:
            if fornecedor[2] == cnpj_procurado:  # Comparando com o CNPJ
                # Se o CNPJ for encontrado, exibe os dados na tabela
                self.tabela.insert("", "end", values=fornecedor)
                messagebox.showinfo("Fornecedor Encontrado", f"Fornecedor: {fornecedor[0]} {fornecedor[1]}")
                encontrado = True
                break

        # Caso o CNPJ não seja encontrado, exibe uma mensagem de erro
        if not encontrado:
            messagebox.showerror("Erro", "Fornecedor não encontrado.")
            # Em vez de chamar exibir_tabela, vamos limpar a tabela e restaurar todos os fornecedores
            self.tabela.delete(*self.tabela.get_children())  # Limpa a tabela existente
            for fornecedor in self.fornecedores:  # Adiciona todos os fornecedores novamente
                self.tabela.insert("", "end", values=fornecedor)

    def exibir_botoes(self, container):
        # Frame para os botões de Adicionar, Editar e Excluir
        botoes_frame = Frame(container, bg="grey")
        botoes_frame.pack(pady=10)
        
        # Botão Adicionar
        add_button = Button(botoes_frame, text="Adicionar", command=self.adicionar_fornecedor, font=("Arial", 12), width=10)
        add_button.pack(side=LEFT, padx=10)
        
        # Botão Editar
        edit_button = Button(botoes_frame, text="Editar", command=self.editar_fornecedor, font=("Arial", 12), width=10)
        edit_button.pack(side=LEFT, padx=10)

    def adicionar_fornecedor(self):
        # Função para abrir a janela de adicionar fornecedor
        self.janela_adicionar = Toplevel()
        self.janela_adicionar.title("Adicionar Novo Fornecedor")

        # Criando um Frame para organizar os campos
        form_frame = Frame(self.janela_adicionar)
        form_frame.pack(pady=10)

        # Criando os campos de entrada para o novo fornecedor
        campos = [
            ("Nome:", "nome_entry"),
            ("Sobrenome:", "sobrenome_entry"),
            ("CNPJ:", "cnpj_entry_adicionar"),
            ("Razão social:", "razaosocial_entry"),
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
        Button(button_frame, text="Salvar", command=self.salvar_fornecedor, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
        
        # Botão Cancelar
        Button(button_frame, text="Cancelar", command=self.janela_adicionar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

    def salvar_fornecedor(self):
        # Salvando as informações do novo fornecedor
        nome = self.entries["nome_entry"].get()
        sobrenome = self.entries["sobrenome_entry"].get()
        cnpj = self.entries["cnpj_entry_adicionar"].get()
        razao_social = self.entries["razaosocial_entry"].get()
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
        if not nome or not sobrenome or not cnpj or not razao_social or not logradouro or not bairro or not numero or not cidade or not cep or not celular or not email:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios!")
            return
        
          
        if not self.validar_cnpj(cnpj):
            messagebox.showerror("Erro", "CNPJ inválido!")
            return

        if not self.validar_telefone(fixo) or not self.validar_telefone(celular):
            messagebox.showerror("Erro", "Número de telefone inválido! Verifique o formato.")
            return

        if not self.validar_email(email):
            messagebox.showerror("Erro", "E-mail inválido!")
            return

        # Verifica se o CNPJ já foi registrado
        for fornecedor in self.fornecedores:
            if fornecedor[2] == cnpj:  # O CNPJ é o terceiro item da tupla
                messagebox.showerror("Erro", "CNPJ já registrado!")
                return

        # Se tudo estiver correto, adiciona o novo fornecedor à lista
        self.fornecedores.append((nome, sobrenome, cnpj, razao_social, logradouro, bairro, numero, cidade, cep, complemento, fixo, celular, email))

        # Atualiza a tabela diretamente
        self.exibir_tabela(self.janela_adicionar)

        # Fecha a janela de adicionar
        self.janela_adicionar.destroy()

        # Exibe uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "Fornecedor adicionado com sucesso!")

    def editar_fornecedor(self):
        # Lógica para editar um fornecedor existente
        cnpj_procurado = self.cnpj_entry.get()
        fornecedor_a_editar = None
        for fornecedor in self.fornecedores:
            if fornecedor[2] == cnpj_procurado:
                fornecedor_a_editar = fornecedor
                break
        
        if fornecedor_a_editar:
            # Abrir a janela de edição
            self.janela_editar = Toplevel()
            self.janela_editar.title("Editar Fornecedor")

            # Criando um Frame para organizar os campos
            form_frame = Frame(self.janela_editar)
            form_frame.pack(pady=10)

            # Criando os campos de entrada com os valores existentes do fornecedor
            campos = [
                ("Nome:", "nome_entry", fornecedor_a_editar[0]),
                ("Sobrenome:", "sobrenome_entry", fornecedor_a_editar[1]),
                ("CNPJ:", "cnpj_entry_editar", fornecedor_a_editar[2]),
                ("Razão social:", "razaosocial_entry", fornecedor_a_editar[3]),
                ("Logradouro:", "logradouro_entry", fornecedor_a_editar[4]),
                ("Bairro:", "bairro_entry", fornecedor_a_editar[5]),
                ("Número:", "numero_entry", fornecedor_a_editar[6]),
                ("Cidade:", "cidade_entry", fornecedor_a_editar[7]),
                ("CEP:", "cep_entry", fornecedor_a_editar[8]),
                ("Complemento:", "complemento_entry", fornecedor_a_editar[9]),
                ("Fixo:", "fixo_entry", fornecedor_a_editar[10]),
                ("Celular:", "celular_entry", fornecedor_a_editar[11]),
                ("Email:", "email_entry", fornecedor_a_editar[12])
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
            Button(button_frame, text="Salvar", command=lambda: self.salvar_edicao(fornecedor_a_editar), font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
            
            # Botão Cancelar
            Button(button_frame, text="Cancelar", command=self.janela_editar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

        else:
            messagebox.showerror("Erro", "Fornecedor não encontrado!")

    def salvar_edicao(self, fornecedor_antigo):
        # Atualiza os dados do fornecedor com as novas informações
        nome = self.entries["nome_entry"].get()
        sobrenome = self.entries["sobrenome_entry"].get()
        razao_social = self.entries["razaosocial_entry"].get()
        logradouro = self.entries["logradouro_entry"].get()
        bairro = self.entries["bairro_entry"].get()
        numero = self.entries["numero_entry"].get()
        cidade = self.entries["cidade_entry"].get()
        cep = self.entries["cep_entry"].get()
        complemento = self.entries["complemento_entry"].get()
        fixo = self.entries["fixo_entry"].get()
        celular = self.entries["celular_entry"].get()
        email = self.entries["email_entry"].get()

        if nome and sobrenome and razao_social and logradouro and bairro and numero and cidade and cep and fixo and celular and email:
            # Atualiza os dados do fornecedor
            idx = self.fornecedores.index(fornecedor_antigo)
            self.fornecedores[idx] = (nome, sobrenome, fornecedor_antigo[2], razao_social, logradouro, bairro, numero, cidade, cep, complemento, fixo, celular, email)

            # Atualiza a tabela diretamente
            self.exibir_tabela(self.janela_editar)

            # Fecha a janela de edição
            self.janela_editar.destroy()

            # Exibe mensagem de sucesso
            messagebox.showinfo("Sucesso", "Fornecedor editado com sucesso!")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

    def excluir_fornecedor(self):
        # Função para excluir um fornecedor baseado no CNPJ
        cnpj_procurado = self.cnpj_entry.get()

        # Verificando se o CNPJ foi preenchido
        if not cnpj_procurado:
            messagebox.showerror("Erro", "Digite um CNPJ para excluir!")
            return

        # Exibe a caixa de confirmação
        confirmacao = messagebox.askyesno("Confirmação", "Você tem certeza de que deseja excluir este fornecedor?")

        if confirmacao:  # Se o usuário clicar em 'Sim'
            for fornecedor in self.fornecedores:
                if fornecedor[2] == cnpj_procurado:
                    self.fornecedores.remove(fornecedor)
                    self.exibir_tabela(self.janela_adicionar)
                    messagebox.showinfo("Sucesso", "Fornecedor excluído com sucesso!")
                    return

            # Caso o CNPJ não seja encontrado
            messagebox.showerror("Erro", "Fornecedor não encontrado!")
        else:
            messagebox.showinfo("Cancelado", "A exclusão foi cancelada.")
