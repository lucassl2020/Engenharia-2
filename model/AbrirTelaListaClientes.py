from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command


class AbrirTelaListaClientes(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 18:
            self._stack_telas.screens[9].clear()
            self._stack_telas.open_screen(9)

            conexao, cursor = abrir_banco_de_dados()


            lista_clientes = apply_sql_command(cursor, "SELECT * FROM Clientes", retorno="fetchall")

            self._stack_telas.screens[9].tabela.setRowCount(len(lista_clientes)) 
            self._stack_telas.screens[9].tabela.setHorizontalHeaderLabels(["Cpf", "Nome", "Endereço", "Data de nascimento", "Telefone"])


            fechar_banco_de_dados(conexao)

            indice_linha = 0
            for tupla_valores in lista_clientes:
                self._stack_telas.screens[9].adicionarItemTabela(indice_linha, tupla_valores)

                indice_linha += 1
