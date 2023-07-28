import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from datetime import date
import os

class ConsultorioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Consultório de Fisioterapia")
        self.root.geometry("800x400")

        self.gastos = []
        self.ganhos = []
        self.clientes = []

        self.tab_control = ttk.Notebook(root)
        self.tab_gastos = ttk.Frame(self.tab_control)
        self.tab_ganhos = ttk.Frame(self.tab_control)
        self.tab_clientes = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_gastos, text="Gastos")
        self.tab_control.add(self.tab_ganhos, text="Ganhos")
        self.tab_control.add(self.tab_clientes, text="Clientes")
        self.tab_control.pack(expand=1, fill="both")

        # Aba de Gastos
        self.label_descricao_gastos = tk.Label(self.tab_gastos, text="Descrição do gasto:")
        self.label_descricao_gastos.pack()

        self.entry_descricao_gastos = tk.Entry(self.tab_gastos)
        self.entry_descricao_gastos.pack()

        self.label_valor_gasto = tk.Label(self.tab_gastos, text="Valor do gasto:")
        self.label_valor_gasto.pack()

        self.entry_valor_gasto = tk.Entry(self.tab_gastos)
        self.entry_valor_gasto.pack()

        self.button_registrar_gasto = tk.Button(self.tab_gastos, text="Registrar Gasto", command=self.registrar_gasto)
        self.button_registrar_gasto.pack()

        # Aba de Ganhos
        self.label_nome = tk.Label(self.tab_ganhos, text="Nome:")
        self.label_nome.pack()

        self.entry_nome = tk.Entry(self.tab_ganhos)
        self.entry_nome.pack()

        self.label_cpf = tk.Label(self.tab_ganhos, text="CPF:")
        self.label_cpf.pack()

        self.entry_cpf = tk.Entry(self.tab_ganhos)
        self.entry_cpf.pack()

        self.label_telefone = tk.Label(self.tab_ganhos, text="Telefone:")
        self.label_telefone.pack()

        self.entry_telefone = tk.Entry(self.tab_ganhos)
        self.entry_telefone.pack()

        self.label_procedimento = tk.Label(self.tab_ganhos, text="Procedimento:")
        self.label_procedimento.pack()

        self.entry_procedimento = tk.Entry(self.tab_ganhos)
        self.entry_procedimento.pack()

        self.label_tipo_pagamento = tk.Label(self.tab_ganhos, text="Mensal ou Diária:")
        self.label_tipo_pagamento.pack()

        self.entry_tipo_pagamento = tk.Entry(self.tab_ganhos)
        self.entry_tipo_pagamento.pack()

        self.label_valor_pago = tk.Label(self.tab_ganhos, text="Valor a ser pago:")
        self.label_valor_pago.pack()

        self.entry_valor_pago = tk.Entry(self.tab_ganhos)
        self.entry_valor_pago.pack()

        self.button_registrar_cliente = tk.Button(self.tab_ganhos, text="Registrar Cliente", command=self.registrar_cliente)
        self.button_registrar_cliente.pack()

        # Aba de Clientes
        self.tree = ttk.Treeview(self.tab_clientes, columns=("Nome", "CPF", "Telefone", "Procedimento", "Tipo Pagamento", "Valor Pago"))
        self.tree.heading("#1", text="Nome")
        self.tree.heading("#2", text="CPF")
        self.tree.heading("#3", text="Telefone")
        self.tree.heading("#4", text="Procedimento")
        self.tree.heading("#5", text="Tipo Pagamento")
        self.tree.heading("#6", text="Valor Pago")
        self.tree.pack()

        self.button_atualizar_clientes = tk.Button(self.tab_clientes, text="Atualizar Clientes", command=self.atualizar_clientes)
        self.button_atualizar_clientes.pack()

        self.button_gerar_relatorio = tk.Button(root, text="Gerar Relatório", command=self.gerar_relatorio)
        self.button_gerar_relatorio.pack()

    def registrar_gasto(self):
        try:
            descricao = self.entry_descricao_gastos.get()
            valor = float(self.entry_valor_gasto.get())

            self.gastos.append({"Descrição": descricao, "Valor": valor})

            messagebox.showinfo("Sucesso", "Gasto registrado com sucesso!")

            self.entry_descricao_gastos.delete(0, tk.END)
            self.entry_valor_gasto.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para o gasto.")

    def registrar_cliente(self):
        try:
            nome = self.entry_nome.get()
            cpf = self.entry_cpf.get()
            telefone = self.entry_telefone.get()
            procedimento = self.entry_procedimento.get()
            tipo_pagamento = self.entry_tipo_pagamento.get()
            valor_pago = float(self.entry_valor_pago.get())

            self.clientes.append({
                "Nome": nome,
                "CPF": cpf,
                "Telefone": telefone,
                "Procedimento": procedimento,
                "Tipo Pagamento": tipo_pagamento,
                "Valor Pago": valor_pago
            })

            messagebox.showinfo("Sucesso", "Cliente registrado com sucesso!")

            # Limpar os campos de entrada
            self.entry_nome.delete(0, tk.END)
            self.entry_cpf.delete(0, tk.END)
            self.entry_telefone.delete(0, tk.END)
            self.entry_procedimento.delete(0, tk.END)
            self.entry_tipo_pagamento.delete(0, tk.END)
            self.entry_valor_pago.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para o Valor Pago.")

    def atualizar_clientes(self):
        # Limpar a exibição atual dos clientes
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Adicionar os clientes na tabela
        for cliente in self.clientes:
            self.tree.insert("", "end", values=(
                cliente["Nome"],
                cliente["CPF"],
                cliente["Telefone"],
                cliente["Procedimento"],
                cliente["Tipo Pagamento"],
                cliente["Valor Pago"]
            ))
    def gerar_relatorio(self):
    
        data_atual = date.today().strftime("%d-%m-%Y")
        df_gastos = pd.DataFrame(self.gastos)
        df_gastos["Data"] = data_atual

        df_ganhos = pd.DataFrame(self.ganhos)
        df_ganhos["Data"] = data_atual

        df_clientes = pd.DataFrame(self.clientes)

        file_path = "relatorio_consultorio.xlsx"
        with pd.ExcelWriter(file_path) as writer:
            df_gastos.to_excel(writer, sheet_name="Gastos", index=False)
            df_ganhos.to_excel(writer, sheet_name="Ganhos", index=False)
            df_clientes.to_excel(writer, sheet_name="Clientes", index=False)

        if os.path.exists(file_path):
            messagebox.showinfo("Relatório Gerado", f"Relatório gerado com sucesso!\nCaminho do arquivo: {file_path}")
        else:
            messagebox.showerror("Erro", "Ocorreu um erro ao gerar o relatório. Verifique as permissões de gravação.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConsultorioApp(root)
    root.mainloop()