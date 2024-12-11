from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re



class Caminhao:
    def __init__(self):
        # Lista de exemplo de caminhões (pode ser vazia)
        self.caminhoes = []
    
    def validar_renavam(self, renavam):
        # Remove qualquer caractere não numérico
        renavam = re.sub(r'\D', '', renavam)

        # Verifica se o renavam tem 11 dígitos
        if len(renavam) != 11 or not renavam.isdigit():
            return False
        return True
    
    def validar_chassi(self, chassi):
        # Verifica se o chassi tem 17 caracteres e é alfanumérico
        if len(chassi) != 17 or not chassi.isalnum():
            return False
        return True

    def validar_placa(self, placa):
        # Converte a placa para letras maiúsculas
        placa = placa.upper()
        
        # Expressão regular para validar a placa no padrão ABC1A23 (sem hífen)
        padrao = r'^[A-Z]{3}\d[A-Z]\d{2}$'
        
        # Verifica se a placa corresponde ao padrão
        if re.match(padrao, placa):
            return True
        return False  
    
    def pagina_caminhao(self, container, voltar_func):
        # Limpa o container e exibe a tabela de caminhão
        for widget in container.winfo_children():
            widget.destroy()  # Remove qualquer widget anterior
        
        # Exibir a label de gerenciamento
        self.exibir_label(container)
        
        # Exibir a tabela com todos os caminhões inicialmente
        self.exibir_tabela(container)
        
        # Instrução sobre o campo placa
        Label(container, text="Digite a placa para busca:", font=("Arial", 12), bg="grey").pack(pady=10)

        # Frame para o campo da placa e os botões lado a lado
        search_frame = Frame(container, bg="grey")
        search_frame.pack(pady=10)

        # Campo para digitar a placa
        self.placa_entry = Entry(search_frame, font=("Arial", 12), width=15)
        self.placa_entry.pack(side=LEFT, padx=5)  # Ajustando para ficar ao lado do botão

        # Botão de pesquisa
        search_button = Button(search_frame, text="Pesquisar", command=self.pesquisar_caminhao, font=("Arial", 12))
        search_button.pack(side=LEFT, padx=5)  # Ajustando para ficar ao lado do campo da placa

        # Botão Excluir ao lado do botão de pesquisa
        delete_button = Button(search_frame, text="Excluir", command=self.excluir_caminhao, font=("Arial", 12), width=10)
        delete_button.pack(side=LEFT, padx=5)  # Ajusta a posição para ficar ao lado do botão de pesquisa

        # Botões de Adicionar, Editar
        self.exibir_botoes(container)
        
        # Botão de voltar ao menu principal
        Button(container, text="Voltar ao Home", width=20, command=voltar_func).pack(pady=20)

    def exibir_label(self, container):
        # Label acima da tabela
        label = Label(container, text="Gerenciamento de Caminhão", font=("Arial", 16), bg="grey")
        label.pack(pady=10)  # Espaçamento acima da label

    def exibir_tabela(self, container=None):
        # Remover tabela antiga antes de criar uma nova
        for widget in container.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.destroy()  # Remover a tabela existente

        # Definindo o número de linhas como o número de caminhões
        num_linhas = len(self.caminhoes)

        # Criando a nova tabela (Treeview) com altura ajustada
        self.tabela = ttk.Treeview(container, columns=("Modelo", "Marca", "Cor", "Placa", "Renavam", "Chassi", "Capacidade"), show="headings", height=num_linhas)  # Linhas dinâmicas
        self.tabela.pack(pady=10, padx=20)

        # Definindo as colunas da tabela
        self.tabela.heading("Modelo", text="Modelo")
        self.tabela.heading("Marca", text="marca")
        self.tabela.heading("Cor", text="Cor")
        self.tabela.heading("Placa", text="Placa")
        self.tabela.heading("Renavam", text="Renavam")
        self.tabela.heading("Chassi", text="Chassi")
        self.tabela.heading("Capacidade", text="Capacidade")

        # Definindo a largura das colunas
        col_widths = [100, 100, 100, 100, 100, 100, 100]
        for col, width in zip(self.tabela["columns"], col_widths):
            self.tabela.column(col, width=width)  # Ajustando a largura das colunas

        # Adicionando todos os caminhões à tabela
        for caminhao in self.caminhoes:
            # Convertendo a placa para maiúsculas
            caminhao_com_placa_maiuscula = list(caminhao)
            caminhao_com_placa_maiuscula[3] = caminhao[3].upper()  # Convertendo a placa para maiúsculas

            # Adicionando a linha com a placa em maiúsculas
            self.tabela.insert("", "end", values=caminhao_com_placa_maiuscula)


    def pesquisar_caminhao(self):
        # Obtendo a placa digitado
        placa_procurado = self.placa_entry.get().upper()  # Converte para maiúsculas

        # Limpar a tabela antes de adicionar os resultados
        for row in self.tabela.get_children():
            self.tabela.delete(row)  # Remove todas as linhas existentes

        # Verificando se a placa está na lista de funcionários
        encontrado = False
        for caminhao in self.caminhoes:
            if caminhao[3] == placa_procurado:  # Comparando com a placa
                # Se a placa for encontrado, exibe os dados na tabela
                self.tabela.insert("", "end", values=caminhao)
                messagebox.showinfo("Caminhão Encontrado", f"caminhão: {caminhao[0]} {caminhao[1]}")
                encontrado = True
                break

        # Caso a placa não seja encontrado, exibe uma mensagem de erro
        if not encontrado:
            messagebox.showerror("Erro", "Caminhão não encontrado.")
            # Em vez de chamar exibir_tabela, vamos limpar a tabela e restaurar todos os caminhões
            self.tabela.delete(*self.tabela.get_children())  # Limpa a tabela existente
            for caminhao in self.caminhoes:  # Adiciona todos os caminhões novamente
                self.tabela.insert("", "end", values=caminhao)

    def exibir_botoes(self, container):
        # Frame para os botões de Adicionar, Editar e Excluir
        botoes_frame = Frame(container, bg="grey")
        botoes_frame.pack(pady=10)
        
        # Botão Adicionar
        add_button = Button(botoes_frame, text="Adicionar", command=self.adicionar_caminhao, font=("Arial", 12), width=10)
        add_button.pack(side=LEFT, padx=10)
        
        # Botão Editar
        edit_button = Button(botoes_frame, text="Editar", command=self.editar_caminhao, font=("Arial", 12), width=10)
        edit_button.pack(side=LEFT, padx=10)

    def adicionar_caminhao(self):
        # Função para abrir a janela de adicionar caminhão
        self.janela_adicionar = Toplevel()
        self.janela_adicionar.title("Adicionar Novo caminhão")

        # Criando um Frame para organizar os campos
        form_frame = Frame(self.janela_adicionar)
        form_frame.pack(pady=10)

        # Criando os campos de entrada para o novo caminhão
        campos = [
            ("Modelo:", "modelo_entry"),
            ("Marca:", "marca_entry"),
            ("Cor:", "cor_entry"),
            ("Placa:", "placa_entry"),
            ("Renavam:", "renavam_entry"),
            ("Chassi:", "chassi_entry"),
            ("Capacidade:", "capacidade_entry"),
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
        Button(button_frame, text="Salvar", command=self.salvar_caminhao, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
        
        # Botão Cancelar
        Button(button_frame, text="Cancelar", command=self.janela_adicionar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

    def salvar_caminhao(self):
        # Salvando as informações do novo caminhão
        modelo = self.entries["modelo_entry"].get()
        marca = self.entries["marca_entry"].get()
        cor = self.entries["cor_entry"].get()
        placa = self.entries["placa_entry"].get().upper()  # Converte para maiúsculas
        renavam = self.entries["renavam_entry"].get()
        chassi = self.entries["chassi_entry"].get()
        capacidade = self.entries["capacidade_entry"].get()
        

        # Verifica se todos os campos obrigatórios foram preenchidos
        if not modelo or not marca or not cor or not placa or not renavam or not chassi or not capacidade:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios!")
            return
        
          
        if not self.validar_placa(placa):
            messagebox.showerror("Erro", "Placa inválido!")
            return

        if not self.validar_renavam(renavam):
            messagebox.showerror("Erro", "Renavam inválido!")
            return

        if not self.validar_chassi(chassi):
            messagebox.showerror("Erro", "Chassi inválido!")
            return

        # Verifica se a placa já foi registrado
        for caminhao in self.caminhoes:
            if caminhao[3] == placa:  # a placa é o terceiro item da tupla
                messagebox.showerror("Erro", "Placa já registrado!")
                return

        # Se tudo estiver correto, adiciona o novo caminhão à lista
        self.caminhoes.append((modelo, marca, cor, placa, renavam, chassi, capacidade))

        # Atualiza a tabela diretamente
        self.exibir_tabela(self.janela_adicionar)

        # Fecha a janela de adicionar
        self.janela_adicionar.destroy()

        # Exibe uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "Caminhão adicionado com sucesso!")

    def editar_caminhao(self):
        # Lógica para editar um caminhão existente
        placa_procurado = self.placa_entry.get().upper()
        
        caminhao_a_editar = None
        for caminhao in self.caminhoes:
            if caminhao[3] == placa_procurado:
                caminhao_a_editar = caminhao
                break
        
        if caminhao_a_editar:
            # Abrir a janela de edição
            self.janela_editar = Toplevel()
            self.janela_editar.title("Editar Caminhão")

            # Criando um Frame para organizar os campos
            form_frame = Frame(self.janela_editar)
            form_frame.pack(pady=10)

            # Criando os campos de entrada com os valores existentes do caminhão
            campos = [
                ("Modelo:", "modelo_entry", caminhao_a_editar[0]),
                ("Marca:", "marca_entry", caminhao_a_editar[1]),
                ("Cor:", "cor_entry", caminhao_a_editar[2]),
                ("Placa:", "placa_entry", caminhao_a_editar[3]),
                ("Renavam:", "renavam_entry", caminhao_a_editar[4]),
                ("Chassi:", "chassi_entry", caminhao_a_editar[5]),
                ("Capacidade:", "capacidade_entry", caminhao_a_editar[6]),
            ]
            
            # Adicionando os campos com valores existentes
            self.entries = {}
            for i, (label_text, entry_name, entry_value) in enumerate(campos):
                Label(form_frame, text=label_text).grid(row=i, column=0, sticky=W, pady=5, padx=5)
                entry = Entry(form_frame, font=("Arial", 12))
                entry.insert(0, entry_value.upper())  # Converte para maiúsculas ao exibir
                entry.grid(row=i, column=1, pady=5, padx=5)
                self.entries[entry_name] = entry

            # Botões de salvar e cancelar
            button_frame = Frame(self.janela_editar)
            button_frame.pack(pady=10)

            # Botão Salvar
            Button(button_frame, text="Salvar", command=lambda: self.salvar_edicao(caminhao_a_editar), font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
            
            # Botão Cancelar
            Button(button_frame, text="Cancelar", command=self.janela_editar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

        else:
            messagebox.showerror("Erro", "Caminhão não encontrado!")

    def salvar_edicao(self, caminhao_antigo):
        # Atualiza os dados do caminhão com as novas informações
        modelo = self.entries["modelo_entry"].get()
        marca = self.entries["marca_entry"].get()
        cor = self.entries["cor_entry"].get()
        renavam = self.entries["renavam_entry"].get()
        chassi = self.entries["chassi_entry"].get()
        capacidade = self.entries["capacidade_entry"].get()

        if modelo and marca and cor and renavam and chassi and capacidade:
            # Atualiza os dados do caminhão
            idx = self.caminhoes.index(caminhao_antigo)
            self.caminhoes[idx] = (modelo, marca, cor, caminhao_antigo[3], renavam, chassi, capacidade)

            # Atualiza a tabela diretamente
            self.exibir_tabela(self.janela_editar)

            # Fecha a janela de edição
            self.janela_editar.destroy()

            # Exibe mensagem de sucesso
            messagebox.showinfo("Sucesso", "Caminhão editado com sucesso!")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

    def excluir_caminhao(self):
        # Função para excluir um caminhão baseado na placa
        placa_procurado = self.placa_entry.get().upper()

        # Verificando se a placa foi preenchido
        if not placa_procurado:
            messagebox.showerror("Erro", "Digite uma placa para excluir!")
            return

        # Exibe a caixa de confirmação
        confirmacao = messagebox.askyesno("Confirmação", "Você tem certeza de que deseja excluir este caminhão?")

        if confirmacao:  # Se o usuário clicar em 'Sim'
            for caminhao in self.caminhoes:
                if caminhao[3] == placa_procurado:
                    self.caminhoes.remove(caminhao)
                    self.exibir_tabela(self.janela_adicionar)
                    messagebox.showinfo("Sucesso", "Caminhão excluído com sucesso!")
                    return

            # Caso a placa não seja encontrado
            messagebox.showerror("Erro", "Caminhão não encontrado!")
        else:
            messagebox.showinfo("Cancelado", "A exclusão foi cancelada.")
