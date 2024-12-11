from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Funcionario:
    def __init__(self):
        # Lista de exemplo de funcionários (pode ser vazia)
        self.funcionarios = [
            ("João", "Silva", "12345678901", "Analista", "Rua A", "Centro", "123", "São Paulo", "12345-678", "", "3000-0000", "99999-9999", "joao@email.com"),
            ("Maria", "Oliveira", "98765432100", "Gerente", "Rua B", "Jardim", "456", "Rio de Janeiro", "98765-432", "", "4000-0000", "98888-8888", "maria@email.com"),
            ("Carlos", "Pereira", "11122334455", "Desenvolvedor", "Rua C", "Vila", "789", "Belo Horizonte", "11223-445", "", "5000-0000", "97777-7777", "carlos@email.com")
        ]
    
    def pagina_funcionario(self, container, voltar_func):
        # Limpa o container e exibe a tabela de funcionários
        for widget in container.winfo_children():
            widget.destroy()  # Remove qualquer widget anterior
        
        # Exibir a label de gerenciamento
        self.exibir_label(container)
        
        # Exibir a tabela com todos os funcionários inicialmente
        self.exibir_tabela(container)
        
        # Instrução sobre o campo CPF
        Label(container, text="Digite o CPF para busca:", font=("Arial", 12), bg="grey").pack(pady=10)

        # Frame para o campo de CPF e os botões lado a lado
        search_frame = Frame(container, bg="grey")
        search_frame.pack(pady=10)

        # Campo para digitar CPF
        self.cpf_entry = Entry(search_frame, font=("Arial", 12), width=15)
        self.cpf_entry.pack(side=LEFT, padx=5)  # Ajustando para ficar ao lado do botão

        # Botão de pesquisa
        search_button = Button(search_frame, text="Pesquisar", command=self.pesquisar_funcionario, font=("Arial", 12))
        search_button.pack(side=LEFT, padx=5)  # Ajustando para ficar ao lado do campo de CPF

        # Botão Excluir ao lado do botão de pesquisa
        delete_button = Button(search_frame, text="Excluir", command=self.excluir_funcionario, font=("Arial", 12), width=10)
        delete_button.pack(side=LEFT, padx=5)  # Ajusta a posição para ficar ao lado do botão de pesquisa

        # Botões de Adicionar, Editar
        self.exibir_botoes(container)
        
        # Botão de voltar ao menu principal
        Button(container, text="Voltar ao Home", width=20, command=voltar_func).pack(pady=20)

    def exibir_label(self, container):
        # Label acima da tabela
        label = Label(container, text="Gerenciamento de Funcionário", font=("Arial", 16), bg="grey")
        label.pack(pady=10)  # Espaçamento acima da label

    def exibir_tabela(self, container=None):
        # Remover tabela antiga antes de criar uma nova
        for widget in container.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.destroy()  # Remover a tabela existente
        
        # Criando a nova tabela (Treeview)
        self.tabela = ttk.Treeview(container, columns=("Nome", "Sobrenome", "CPF", "Cargo", "Logradouro", "Bairro", "Número", "Cidade", "CEP", "Complemento", "Fixo", "Celular", "Email"), show="headings", height=4)  # 4 linhas visíveis
        self.tabela.pack(pady=10, padx=20)

        # Definindo as colunas da tabela
        self.tabela.heading("Nome", text="Nome")
        self.tabela.heading("Sobrenome", text="Sobrenome")
        self.tabela.heading("CPF", text="CPF")
        self.tabela.heading("Cargo", text="Cargo")
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
        
        # Inicialmente, adiciona todos os funcionários à tabela
        for funcionario in self.funcionarios:
            self.tabela.insert("", "end", values=funcionario)

    def pesquisar_funcionario(self):
        # Obtendo o CPF digitado
        cpf_procurado = self.cpf_entry.get()

        # Limpar a tabela antes de adicionar os resultados
        for row in self.tabela.get_children():
            self.tabela.delete(row)  # Remove todas as linhas existentes

        # Verificando se o CPF está na lista de funcionários
        encontrado = False
        for funcionario in self.funcionarios:
            if funcionario[2] == cpf_procurado:  # Comparando com o CPF
                # Se o CPF for encontrado, exibe os dados na tabela
                self.tabela.insert("", "end", values=funcionario)
                messagebox.showinfo("Funcionário Encontrado", f"Funcionário: {funcionario[0]} {funcionario[1]}")
                encontrado = True
                break

        # Caso o CPF não seja encontrado, exibe uma mensagem de erro
        if not encontrado:
            messagebox.showerror("Erro", "Funcionário não encontrado.")
            # Em vez de chamar exibir_tabela, vamos limpar a tabela e restaurar todos os funcionários
            self.tabela.delete(*self.tabela.get_children())  # Limpa a tabela existente
            for funcionario in self.funcionarios:  # Adiciona todos os funcionários novamente
                self.tabela.insert("", "end", values=funcionario)


    def exibir_botoes(self, container):
        # Frame para os botões de Adicionar, Editar e Excluir
        botoes_frame = Frame(container, bg="grey")
        botoes_frame.pack(pady=10)
        
        # Botão Adicionar
        add_button = Button(botoes_frame, text="Adicionar", command=self.adicionar_funcionario, font=("Arial", 12), width=10)
        add_button.pack(side=LEFT, padx=10)
        
        # Botão Editar
        edit_button = Button(botoes_frame, text="Editar", command=self.editar_funcionario, font=("Arial", 12), width=10)
        edit_button.pack(side=LEFT, padx=10)
    
    def adicionar_funcionario(self):
        # Função para abrir a janela de adicionar funcionário
        self.janela_adicionar = Toplevel()
        self.janela_adicionar.title("Adicionar Novo Funcionário")

        # Definindo o layout da janela como grid
        self.janela_adicionar.geometry("400x600")  # Ajuste o tamanho se necessário
        
        # Criando os campos de entrada para o novo funcionário
        Label(self.janela_adicionar, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.nome_entry = Entry(self.janela_adicionar, font=("Arial", 12))
        self.nome_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(self.janela_adicionar, text="Sobrenome:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.sobrenome_entry = Entry(self.janela_adicionar, font=("Arial", 12))
        self.sobrenome_entry.grid(row=1, column=1, padx=10, pady=5)

        Label(self.janela_adicionar, text="CPF:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.cpf_entry_adicionar = Entry(self.janela_adicionar, font=("Arial", 12))
        self.cpf_entry_adicionar.grid(row=2, column=1, padx=10, pady=5)

        Label(self.janela_adicionar, text="Cargo:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.cargo_entry = Entry(self.janela_adicionar, font=("Arial", 12))
        self.cargo_entry.grid(row=3, column=1, padx=10, pady=5)

        # Novos campos de endereço e contato
        Label(self.janela_adicionar, text="Logradouro:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.logradouro_entry = Entry(self.janela_adicionar, font=("Arial", 12))
        self.logradouro_entry.grid(row=4, column=1, padx=10, pady=5)

        Label(self.janela_adicionar, text="Bairro:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.bairro_entry = Entry(self.janela_adicionar, font=("Arial", 12))
        self.bairro_entry.grid(row=5, column=1, padx=10, pady=5)

        Label(self.janela_adicionar, text="Número:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.numero_entry = Entry(self.janela_adicionar, font=("Arial", 12))
        self.numero_entry.grid(row=6, column=1, padx=10, pady=5)

        Label(self.janela_adicionar, text="Cidade:").grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.cidade_entry = Entry(self.janela_adicionar, font=("Arial", 12))
        self.cidade_entry.grid(row=7, column=1, padx=10, pady=5)

        Label(self.janela_adicionar, text="CEP:").grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.cep_entry = Entry(self.janela_adicionar, font=("Arial", 12))
        self.cep_entry.grid(row=8, column=1, padx=10, pady=5)

        Label(self.janela_adicionar, text="Complemento:").grid(row=9, column=0, padx=10, pady=5, sticky="w")
        self.complemento_entry = Entry(self.janela_adicionar, font=("Arial", 12))
        self.complemento_entry.grid(row=9, column=1, padx=10, pady=5)

        Label(self.janela_adicionar, text="Fixo:").grid(row=10, column=0, padx=10, pady=5, sticky="w")
        self.fixo_entry = Entry(self.janela_adicionar, font=("Arial", 12))
        self.fixo_entry.grid(row=10, column=1, padx=10, pady=5)

        Label(self.janela_adicionar, text="Celular:").grid(row=11, column=0, padx=10, pady=5, sticky="w")
        self.celular_entry = Entry(self.janela_adicionar, font=("Arial", 12))
        self.celular_entry.grid(row=11, column=1, padx=10, pady=5)

        Label(self.janela_adicionar, text="Email:").grid(row=12, column=0, padx=10, pady=5, sticky="w")
        self.email_entry = Entry(self.janela_adicionar, font=("Arial", 12))
        self.email_entry.grid(row=12, column=1, padx=10, pady=5)

        # Botões de Salvar e Cancelar
        frame_botoes = Frame(self.janela_adicionar)
        frame_botoes.grid(row=13, columnspan=2, pady=20)

        # Botão Salvar
        Button(frame_botoes, text="Salvar", command=self.salvar_funcionario, font=("Arial", 12)).pack(side=LEFT, padx=10)
        
        # Botão Cancelar
        Button(frame_botoes, text="Cancelar", command=self.janela_adicionar.destroy, font=("Arial", 12)).pack(side=LEFT, padx=10)





    def salvar_funcionario(self):
        # Salvando as informações do novo funcionário
        nome = self.nome_entry.get()
        sobrenome = self.sobrenome_entry.get()
        cpf = self.cpf_entry_adicionar.get()
        cargo = self.cargo_entry.get()
        logradouro = self.logradouro_entry.get()
        bairro = self.bairro_entry.get()
        numero = self.numero_entry.get()
        cidade = self.cidade_entry.get()
        cep = self.cep_entry.get()
        complemento = self.complemento_entry.get()
        fixo = self.fixo_entry.get()
        celular = self.celular_entry.get()
        email = self.email_entry.get()

        if nome and sobrenome and cpf and cargo and logradouro and bairro and numero and cidade and cep and fixo and celular and email:
            # Adiciona o novo funcionário à lista
            self.funcionarios.append((nome, sobrenome, cpf, cargo, logradouro, bairro, numero, cidade, cep, complemento, fixo, celular, email))

            # Atualiza a tabela
            self.exibir_tabela(self.janela_adicionar)

            # Fecha a janela de adicionar
            self.janela_adicionar.destroy()

            # Exibe uma mensagem de sucesso
            messagebox.showinfo("Sucesso", "Funcionário adicionado com sucesso!")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
    
    def editar_funcionario(self):
        # Lógica para editar um funcionário existente
        messagebox.showinfo("Editar Funcionário", "Editar o funcionário selecionado.")
    
    def excluir_funcionario(self):
        # Obtendo o CPF digitado
        cpf_procurado = self.cpf_entry.get()

        # Procurando o funcionário pelo CPF na lista
        funcionario_a_remover = None
        for funcionario in self.funcionarios:
            if funcionario[2] == cpf_procurado:
                funcionario_a_remover = funcionario
                break

        if funcionario_a_remover:
            # Exibe uma caixa de confirmação antes de excluir
            confirmacao = messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja excluir o funcionário {funcionario_a_remover[0]} {funcionario_a_remover[1]}?")
            
            if confirmacao:  # Se o usuário confirmar a exclusão
                # Remove o funcionário da lista
                self.funcionarios.remove(funcionario_a_remover)

                # Limpar a tabela e exibir todos os funcionários novamente
                for row in self.tabela.get_children():
                    self.tabela.delete(row)  # Remove todas as linhas existentes

                # Adiciona os funcionários restantes na tabela
                for funcionario in self.funcionarios:
                    self.tabela.insert("", "end", values=funcionario)

                # Exibe mensagem de sucesso
                messagebox.showinfo("Sucesso", f"Funcionário {funcionario_a_remover[0]} {funcionario_a_remover[1]} foi excluído.")
            else:
                messagebox.showinfo("Cancelado", "Exclusão cancelada.")
        else:
            messagebox.showerror("Erro", "Funcionário não encontrado.")