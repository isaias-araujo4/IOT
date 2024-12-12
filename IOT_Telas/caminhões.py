from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

class Caminhao:
    def __init__(self):
        self.caminhoes = []
        self.container = None

    def validar_placa(self, placa):
        padrao_placa = re.compile(r'^[A-Z]{3}\d[A-Z]\d{2}$')
        return bool(padrao_placa.match(placa.upper()))


    def validar_renavam(self, renavam):
        renavam = re.sub(r'\D', '', renavam)
        return len(renavam) == 11 and renavam.isdigit()

    def validar_chassi(self, chassi):
        padrao_chassi = re.compile(r'^[A-Z0-9]{17}$')
        return bool(padrao_chassi.match(chassi.upper()))

    def pagina_caminhao(self, container, voltar_func):
        self.container = container

        for widget in container.winfo_children():
            widget.destroy()
        
        self.exibir_label(container)
        self.exibir_tabela(container)

        Label(container, text="Digite a Placa para busca:", font=("Arial", 12), bg="grey").pack(pady=10)
        search_frame = Frame(container, bg="grey")
        search_frame.pack(pady=10)
        self.placa_entry = Entry(search_frame, font=("Arial", 12), width=15)
        self.placa_entry.pack(side=LEFT, padx=5)
        search_button = Button(search_frame, text="Pesquisar", command=self.pesquisar_caminhao, font=("Arial", 12))
        search_button.pack(side=LEFT, padx=5)
        delete_button = Button(search_frame, text="Excluir", command=self.excluir_caminhao, font=("Arial", 12))
        delete_button.pack(side=LEFT, padx=5)
        
        self.exibir_botoes(container)
        Button(container, text="Voltar ao Home", width=20, command=voltar_func).pack(pady=20)

    def exibir_label(self, container):
        label = Label(container, text="Gerenciamento de Caminhão", font=("Arial", 16), bg="grey")
        label.pack(pady=10)

    def exibir_tabela(self, container=None):
        for widget in container.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.destroy()

        num_linhas = len(self.caminhoes)
        self.tabela = ttk.Treeview(container, columns=("Modelo", "Marca", "Cor", "Placa", "RENAVAM", "Chassi", "Capacidade"), show="headings", height=num_linhas)
        self.tabela.pack(pady=10, padx=20)

        col_names = ["Modelo", "Marca", "Cor", "Placa", "RENAVAM", "Chassi", "Capacidade"]
        for col_name in col_names:
            self.tabela.heading(col_name, text=col_name)
        
        col_widths = [100, 100, 100, 100, 100, 100, 100]
        for col, width in zip(self.tabela["columns"], col_widths):
            self.tabela.column(col, width=width)
        
        for caminhao in self.caminhoes:
            self.tabela.insert("", "end", values=caminhao)

    def exibir_botoes(self, container):
        botoes_frame = Frame(container, bg="grey")
        botoes_frame.pack(pady=10)
        add_button = Button(botoes_frame, text="Adicionar", command=self.adicionar_caminhao, font=("Arial", 12), width=10)
        add_button.pack(side=LEFT, padx=10)
        edit_button = Button(botoes_frame, text="Editar", command=self.editar_caminhao, font=("Arial", 12), width=10)
        edit_button.pack(side=LEFT, padx=10)

    def adicionar_caminhao(self):
        self.janela_adicionar = Toplevel()
        self.janela_adicionar.title("Adicionar Novo Caminhão")
        form_frame = Frame(self.janela_adicionar)
        form_frame.pack(pady=10)

        campos = [
            ("Modelo:", "modelo_entry"),
            ("Marca:", "marca_entry"),
            ("Cor:", "cor_entry"),
            ("Placa:", "placa_entry"),
            ("RENAVAM:", "renavam_entry"),
            ("Chassi:", "chassi_entry"),
            ("Capacidade:", "capacidade_entry")
        ]

        self.entries = {}
        for i, (label_text, entry_name) in enumerate(campos):
            Label(form_frame, text=label_text).grid(row=i, column=0, sticky=W, pady=5, padx=5)
            entry = Entry(form_frame, font=("Arial", 12))
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries[entry_name] = entry

        button_frame = Frame(self.janela_adicionar)
        button_frame.pack(pady=10)
        Button(button_frame, text="Salvar", command=self.salvar_caminhao, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
        Button(button_frame, text="Cancelar", command=self.janela_adicionar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

    def salvar_caminhao(self):
        modelo = self.entries["modelo_entry"].get()
        marca = self.entries["marca_entry"].get()
        cor = self.entries["cor_entry"].get()
        placa = self.entries["placa_entry"].get().upper()
        renavam = self.entries["renavam_entry"].get()
        chassi = self.entries["chassi_entry"].get().upper()
        capacidade = self.entries["capacidade_entry"].get()

        if not (modelo and marca and cor and placa and renavam and chassi and capacidade):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios!")
            return

        if not self.validar_placa(placa):
            messagebox.showerror("Erro", "Placa inválida! Verifique o formato.")
            return

        if not self.validar_renavam(renavam):
            messagebox.showerror("Erro", "RENAVAM inválido!")
            return

        if not self.validar_chassi(chassi):
            messagebox.showerror("Erro", "Chassi inválido! Verifique o formato.")
            return

        for caminhao in self.caminhoes:
            if caminhao[3] == placa:
                messagebox.showerror("Erro", "Placa já registrada!")
                return

        self.caminhoes.append((modelo, marca, cor, placa, renavam, chassi, capacidade))
        self.exibir_tabela(self.container)
        self.janela_adicionar.destroy()
        messagebox.showinfo("Sucesso", "Caminhão adicionado com sucesso!")

    def pesquisar_caminhao(self):
        placa_procurada = self.placa_entry.get().upper()
        if not placa_procurada:
            messagebox.showerror("Erro", "Digite uma Placa para pesquisar!")
            return

        for row in self.tabela.get_children():
            self.tabela.delete(row)

        encontrado = False
        for caminhao in self.caminhoes:
            if caminhao[3] == placa_procurada:
                self.tabela.insert("", "end", values=caminhao)
                messagebox.showinfo("Caminhão Encontrado", f"Caminhão: {caminhao[0]}, {caminhao[1]}")
                encontrado = True
                break

        if not encontrado:
            messagebox.showerror("Erro", "Caminhão não encontrado.")
            self.tabela.delete(*self.tabela.get_children())
            for caminhao in self.caminhoes:
                self.tabela.insert("", "end", values=caminhao)

    def excluir_caminhao(self):
        placa_procurada = self.placa_entry.get().upper()
        if not placa_procurada:
            messagebox.showerror("Erro", "Digite uma Placa para excluir!")
            return

        for i, caminhao in enumerate(self.caminhoes):
            if caminhao[3] == placa_procurada:
                del self.caminhoes[i]
                self.exibir_tabela(self.container)
                messagebox.showinfo("Sucesso", "Caminhão excluído com sucesso!")
                return

        messagebox.showerror("Erro", "Caminhão não encontrado!")
    
    def editar_caminhao(self):
        placa_procurada = self.placa_entry.get().upper()
        if not placa_procurada:
            messagebox.showerror("Erro", "Digite uma Placa para editar!")
            return

        caminhao_encontrado = None
        for caminhao in self.caminhoes:
            if caminhao[3] == placa_procurada:
                caminhao_encontrado = caminhao
                break

        if not caminhao_encontrado:
            messagebox.showerror("Erro", "Caminhão não encontrado!")
            return

        self.janela_editar = Toplevel()
        self.janela_editar.title("Editar Caminhão")
        form_frame = Frame(self.janela_editar)
        form_frame.pack(pady=10)

        campos = [
            ("Modelo:", "modelo_entry", caminhao_encontrado[0]),
            ("Marca:", "marca_entry", caminhao_encontrado[1]),
            ("Cor:", "cor_entry", caminhao_encontrado[2]),
            ("RENAVAM:", "renavam_entry", caminhao_encontrado[4]),
            ("Chassi:", "chassi_entry", caminhao_encontrado[5]),
            ("Capacidade:", "capacidade_entry", caminhao_encontrado[6])
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
        Button(button_frame, text="Salvar", command=lambda: self.atualizar_caminhao(caminhao_encontrado[3]), font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
        Button(button_frame, text="Cancelar", command=self.janela_editar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

    def atualizar_caminhao(self, placa_encontrada):
        modelo = self.entries["modelo_entry"].get()
        marca = self.entries["marca_entry"].get()
        cor = self.entries["cor_entry"].get()
        renavam = self.entries["renavam_entry"].get()
        chassi = self.entries["chassi_entry"].get().upper()
        capacidade = self.entries["capacidade_entry"].get()

        if not (modelo and marca and cor and renavam and chassi and capacidade):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios!")
            return

        if not self.validar_renavam(renavam):
            messagebox.showerror("Erro", "RENAVAM inválido!")
            return

        if not self.validar_chassi(chassi):
            messagebox.showerror("Erro", "Chassi inválido! Verifique o formato.")
            return
        
        for i, caminhao in enumerate(self.caminhoes):
            if caminhao[3] == placa_encontrada:
                self.caminhoes[i] = (modelo, marca, cor, caminhao[3], renavam, chassi, capacidade)
                break

        self.exibir_tabela(self.container)
        self.janela_editar.destroy()
        messagebox.showinfo("Sucesso", "Caminhão atualizado com sucesso!")
