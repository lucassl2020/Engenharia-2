from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command


class AbrirTelaListaPeca(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 17:
            self._stack_telas.screens[8].clear()
            self._stack_telas.open_screen(8)

            conexao, cursor = abrir_banco_de_dados()


            lista_pecas = apply_sql_command(cursor, "SELECT * FROM Pecas", retorno="fetchall")

            self._stack_telas.screens[8].tabela.setRowCount(len(lista_pecas)) 
            self._stack_telas.screens[8].tabela.setHorizontalHeaderLabels(["Codigo", "Nome", "Valor de custo", "Valor de venda", "Código do fornecedor"])


            fechar_banco_de_dados(conexao)

            indice_linha = 0
            for tupla_valores in lista_pecas:
                self._stack_telas.screens[8].adicionarItemTabela(indice_linha, tupla_valores)

                indice_linha += 1
