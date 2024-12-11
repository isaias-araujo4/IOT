from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Funcionario:
    def __init__(self):
        # Lista de exemplo de funcionários (pode ser vazia)
        self.funcionarios = [
            ("João", "Silva", "12345678901", "Analista"),
            ("Maria", "Oliveira", "98765432100", "Gerente"),
            ("Carlos", "Pereira", "11122334455", "Desenvolvedor")
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
        self.tabela = ttk.Treeview(container, columns=("Nome", "Sobrenome", "CPF", "Cargo"), show="headings", height=4)  # 4 linhas visíveis
        self.tabela.pack(pady=10, padx=20)

        # Definindo as colunas da tabela
        self.tabela.heading("Nome", text="Nome")
        self.tabela.heading("Sobrenome", text="Sobrenome")
        self.tabela.heading("CPF", text="CPF")
        self.tabela.heading("Cargo", text="Cargo")

        # Definindo a largura das colunas
        self.tabela.column("Nome", width=120)  # Largura menor
        self.tabela.column("Sobrenome", width=120)  # Largura menor
        self.tabela.column("CPF", width=120)  # Largura menor
        self.tabela.column("Cargo", width=120)  # Largura menor

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
        # Lógica para adicionar um novo funcionário
        messagebox.showinfo("Adicionar Funcionário", "Adicionar um novo funcionário.")
    
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

