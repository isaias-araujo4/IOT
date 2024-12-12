from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class Fluxo:
    def __init__(self, funcionarios, clientes, caminhoes):
        self.fluxos = []
        self.funcionarios = funcionarios
        self.clientes = clientes
        self.caminhoes = caminhoes
        self.id_contador = 1
        self.container = None
    
    def gerar_id(self):
        novo_id = self.id_contador
        self.id_contador += 1
        return novo_id

    def pagina_fluxo(self, container, voltar_func):
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
        search_button = Button(search_frame, text="Pesquisar", command=self.pesquisar_fluxo, font=("Arial", 12))
        search_button.pack(side=LEFT, padx=5)
        delete_button = Button(search_frame, text="Excluir", command=self.excluir_fluxo, font=("Arial", 12))
        delete_button.pack(side=LEFT, padx=5)
        
        self.exibir_botoes(container)
        Button(container, text="Voltar ao Home", width=20, command=voltar_func).pack(pady=20)

    def exibir_label(self, container):
        label = Label(container, text="Gerenciamento de Fluxo", font=("Arial", 16), bg="grey")
        label.pack(pady=10)

    def exibir_tabela(self, container=None):
        for widget in container.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.destroy()

        num_linhas = len(self.fluxos)
        self.tabela = ttk.Treeview(container, columns=("ID", "Carga", "Data Saída", "Hora Saída", "Data Retorno", "Hora Retorno", "Destino Final", "Roteiro", "KM Saída", "KM Retorno", "Funcionário", "Cliente", "Caminhão"), show="headings", height=num_linhas)
        self.tabela.pack(pady=10, padx=20)

        col_names = ["ID", "Carga", "Data Saída", "Hora Saída", "Data Retorno", "Hora Retorno", "Destino Final", "Roteiro", "KM Saída", "KM Retorno", "Funcionário", "Cliente", "Caminhão"]
        for col_name in col_names:
            self.tabela.heading(col_name, text=col_name)
        
        col_widths = [50, 100, 100, 100, 100, 100, 120, 120, 100, 100, 100, 100, 100]
        for col, width in zip(self.tabela["columns"], col_widths):
            self.tabela.column(col, width=width)
        
        for fluxo in self.fluxos:
            self.tabela.insert("", "end", values=fluxo)


    def exibir_botoes(self, container):
        botoes_frame = Frame(container, bg="grey")
        botoes_frame.pack(pady=10)
        add_button = Button(botoes_frame, text="Adicionar", command=self.adicionar_fluxo, font=("Arial", 12), width=10)
        add_button.pack(side=LEFT, padx=10)
        edit_button = Button(botoes_frame, text="Editar", command=self.editar_fluxo, font=("Arial", 12), width=10)
        edit_button.pack(side=LEFT, padx=10)

    def adicionar_fluxo(self):
        self.janela_adicionar = Toplevel()
        self.janela_adicionar.title("Adicionar Novo Fluxo")
        form_frame = Frame(self.janela_adicionar)
        form_frame.pack(pady=10)

        campos = [
            ("Carga:", "carga_entry"),
            ("Data Saída:", "data_saida_entry"),
            ("Hora Saída:", "hora_saida_entry"),
            ("Data Retorno:", "data_retorno_entry"),
            ("Hora Retorno:", "hora_retorno_entry"),
            ("Destino Final:", "destino_final_entry"),
            ("Roteiro:", "roteiro_entry"),
            ("KM Saída:", "km_saida_entry"),
            ("KM Retorno:", "km_retorno_entry"),
            ("Funcionário (Nome Sobrenome):", "funcionario_entry"),
            ("Cliente (Nome Sobrenome):", "cliente_entry"),
            ("Caminhão (Modelo Marca):", "caminhao_entry")
        ]

        self.entries = {}
        for i, (label_text, entry_name) in enumerate(campos):
            Label(form_frame, text=label_text).grid(row=i, column=0, sticky=W, pady=5, padx=5)
            entry = Entry(form_frame, font=("Arial", 12))
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries[entry_name] = entry

        button_frame = Frame(self.janela_adicionar)
        button_frame.pack(pady=10)
        Button(button_frame, text="Salvar", command=self.salvar_fluxo, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
        Button(button_frame, text="Cancelar", command=self.janela_adicionar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

    def salvar_fluxo(self):
        id_fluxo = self.gerar_id()
        carga = self.entries["carga_entry"].get()
        data_saida = self.entries["data_saida_entry"].get()
        hora_saida = self.entries["hora_saida_entry"].get()
        data_retorno = self.entries["data_retorno_entry"].get()
        hora_retorno = self.entries["hora_retorno_entry"].get()
        destino_final = self.entries["destino_final_entry"].get()
        roteiro = self.entries["roteiro_entry"].get()
        km_saida = self.entries["km_saida_entry"].get()
        km_retorno = self.entries["km_retorno_entry"].get()
        funcionario = self.entries["funcionario_entry"].get()
        cliente = self.entries["cliente_entry"].get()
        caminhao = self.entries["caminhao_entry"].get()

        if not carga or not data_saida or not hora_saida or not data_retorno or not hora_retorno or not destino_final or not roteiro or not km_saida or not km_retorno or not funcionario or not cliente or not caminhao:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios!")
            return

        try:
            km_saida = float(km_saida)
            km_retorno = float(km_retorno)
            datetime.strptime(data_saida, "%d/%m/%Y")
            datetime.strptime(hora_saida, "%H:%M")
            datetime.strptime(data_retorno, "%d/%m/%Y")
            datetime.strptime(hora_retorno, "%H:%M")
        except ValueError as e:
            messagebox.showerror("Erro", f"Erro no formato de um dos campos: {e}")
            return

        funcionario_existente = any(f"{f[0]} {f[1]}" == funcionario for f in self.funcionarios)
        if not funcionario_existente:
            messagebox.showerror("Erro", "Funcionário não encontrado!")
            return

        cliente_existente = any(f"{c[0]} {c[1]}" == cliente for c in self.clientes)
        if not cliente_existente:
            messagebox.showerror("Erro", "Cliente não encontrado!")
            return

        caminhao_existente = any(f"{c[0]} {c[1]}" == caminhao for c in self.caminhoes)
        if not caminhao_existente:
            messagebox.showerror("Erro", "Caminhão não encontrado!")
            return

        self.fluxos.append((id_fluxo, carga, data_saida, hora_saida, data_retorno, hora_retorno, destino_final, roteiro, km_saida, km_retorno, funcionario, cliente, caminhao))
        self.exibir_tabela(self.container)
        self.janela_adicionar.destroy()
        messagebox.showinfo("Sucesso", "Fluxo adicionado com sucesso!")
        
    def pesquisar_fluxo(self):
        id_procurado = self.id_entry.get()
        for row in self.tabela.get_children():
            self.tabela.delete(row)

        encontrado = False
        for fluxo in self.fluxos:
            if str(fluxo[0]) == id_procurado:
                self.tabela.insert("", "end", values=fluxo)
                messagebox.showinfo("Fluxo Encontrado", f"Fluxo: {fluxo[1]}")
                encontrado = True
                break

        if not encontrado:
            messagebox.showerror("Erro", "Fluxo não encontrado.")
            self.tabela.delete(*self.tabela.get_children())
            for fluxo in self.fluxos:
                self.tabela.insert("", "end", values=fluxo)

    def excluir_fluxo(self):
        id_procurado = self.id_entry.get()
        if not id_procurado:
            messagebox.showerror("Erro", "Digite um ID para excluir!")
            return
        
        for i, fluxo in enumerate(self.fluxos):
            if str(fluxo[0]) == id_procurado:
                del self.fluxos[i]
                self.exibir_tabela(self.container)
                messagebox.showinfo("Sucesso", "Fluxo excluído com sucesso!")
                return

        messagebox.showerror("Erro", "Fluxo não encontrado!")

    def editar_fluxo(self):
        id_procurado = self.id_entry.get()
        if not id_procurado:
            messagebox.showerror("Erro", "Digite um ID para editar!")
            return

        fluxo_encontrado = None
        for fluxo in self.fluxos:
            if str(fluxo[0]) == id_procurado:
                fluxo_encontrado = fluxo
                break

        if not fluxo_encontrado:
            messagebox.showerror("Erro", "Fluxo não encontrado!")
            return

        self.janela_editar = Toplevel()
        self.janela_editar.title("Editar Fluxo")
        form_frame = Frame(self.janela_editar)
        form_frame.pack(pady=10)

        campos = [
            ("Carga:", "carga_entry", fluxo_encontrado[1]),
            ("Data Saída:", "data_saida_entry", fluxo_encontrado[2]),
            ("Hora Saída:", "hora_saida_entry", fluxo_encontrado[3]),
            ("Data Retorno:", "data_retorno_entry", fluxo_encontrado[4]),
            ("Hora Retorno:", "hora_retorno_entry", fluxo_encontrado[5]),
            ("Destino Final:", "destino_final_entry", fluxo_encontrado[6]),
            ("Roteiro:", "roteiro_entry", fluxo_encontrado[7]),
            ("KM Saída:", "km_saida_entry", fluxo_encontrado[8]),
            ("KM Retorno:", "km_retorno_entry", fluxo_encontrado[9]),
            ("Funcionário (Nome Sobrenome):", "funcionario_entry", fluxo_encontrado[10]),
            ("Cliente (Nome Sobrenome):", "cliente_entry", fluxo_encontrado[11]),
            ("Caminhão (Modelo Marca):", "caminhao_entry", fluxo_encontrado[12])
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
        Button(button_frame, text="Salvar", command=lambda: self.atualizar_fluxo(fluxo_encontrado[0]), font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
        Button(button_frame, text="Cancelar", command=self.janela_editar.destroy, font=("Arial", 12), width=10).pack(side=LEFT, padx=10)

    def atualizar_fluxo(self, id_fluxo):
        carga = self.entries["carga_entry"].get()
        data_saida = self.entries["data_saida_entry"].get()
        hora_saida = self.entries["hora_saida_entry"].get()
        data_retorno = self.entries["data_retorno_entry"].get()
        hora_retorno = self.entries["hora_retorno_entry"].get()
        destino_final = self.entries["destino_final_entry"].get()
        roteiro = self.entries["roteiro_entry"].get()
        km_saida = self.entries["km_saida_entry"].get()
        km_retorno = self.entries["km_retorno_entry"].get()
        funcionario = self.entries["funcionario_entry"].get()
        cliente = self.entries["cliente_entry"].get()
        caminhao = self.entries["caminhao_entry"].get()

        if not carga or not data_saida  or not hora_saida  or not data_retorno or not hora_retorno  or not destino_final  or not roteiro  or not km_saida  or not km_retorno  or not funcionario  or not cliente  or not caminhao:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios!")
            return

        try:
            km_saida = float(km_saida)
            km_retorno = float(km_retorno)
            datetime.strptime(data_saida, "%d/%m/%Y")
            datetime.strptime(hora_saida, "%H:%M")
            datetime.strptime(data_retorno, "%d/%m/%Y")
            datetime.strptime(hora_retorno, "%H:%M")
        except ValueError as e:
            messagebox.showerror("Erro", f"Erro no formato de um dos campos: {e}")
            return

        funcionario_existente = any(f"{f[0]} {f[1]}" == funcionario for f in self.funcionarios)
        if not funcionario_existente:
            messagebox.showerror("Erro", "Funcionário não encontrado!")
            return

        cliente_existente = any(f"{c[0]} {c[1]}" == cliente for c in self.clientes)
        if not cliente_existente:
            messagebox.showerror("Erro", "Cliente não encontrado!")
            return

        caminhao_existente = any(f"{c[0]} {c[1]}" == caminhao for c in self.caminhoes)
        if not caminhao_existente:
            messagebox.showerror("Erro", "Caminhão não encontrado!")
            return

        for i, fluxo in enumerate(self.fluxos):
            if fluxo[0] == id_fluxo:
                self.fluxos[i] = (id_fluxo, carga, data_saida, hora_saida, data_retorno, hora_retorno, destino_final, roteiro, km_saida, km_retorno, funcionario, cliente, caminhao)
                break

        self.exibir_tabela(self.container)
        self.janela_editar.destroy()
        messagebox.showinfo("Sucesso", "Fluxo atualizado com sucesso!")
