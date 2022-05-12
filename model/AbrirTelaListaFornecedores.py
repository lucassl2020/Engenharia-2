from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command


class AbrirTelaListaFornecedores(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 19:
            self._stack_telas.screens[10].clear()
            self._stack_telas.open_screen(10)

            conexao, cursor = abrir_banco_de_dados()


            lista_clientes = apply_sql_command(cursor, "SELECT * FROM Fornecedores", retorno="fetchall")

            self._stack_telas.screens[10].tabela.setRowCount(len(lista_clientes)) 
            self._stack_telas.screens[10].tabela.setHorizontalHeaderLabels(["Cnpj", "Nome fantasia", "Razão social", "Telefone", "Endereço", "Inscrição estadual", "Email"])


            fechar_banco_de_dados(conexao)

            indice_linha = 0
            for tupla_valores in lista_clientes:
                self._stack_telas.screens[10].adicionarItemTabela(indice_linha, tupla_valores)

                indice_linha += 1
