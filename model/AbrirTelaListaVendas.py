from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command


class AbrirTelaListaVendas(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 20:
            self._stack_telas.screens[11].clear()
            self._stack_telas.open_screen(11)

            conexao, cursor = abrir_banco_de_dados()


            lista_pecas = apply_sql_command(cursor, "SELECT * FROM Vendas", retorno="fetchall")

            self._stack_telas.screens[11].tabela.setRowCount(len(lista_pecas)) 
            self._stack_telas.screens[11].tabela.setHorizontalHeaderLabels(["Código da venda", "Quantidade", "Valor total", "Data", "Cpf do cliente", "Código da peça"])


            fechar_banco_de_dados(conexao)

            indice_linha = 0
            for tupla_valores in lista_pecas:
                self._stack_telas.screens[11].adicionarItemTabela(indice_linha, tupla_valores)

                indice_linha += 1
