from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command

from datetime import date


class RealizarVenda(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 13:
            cpf = self._stack_telas.screens[7].cpf_line.text()
            codigo = self._stack_telas.screens[7].codigo_peca_line.text()
            quantidade = self._stack_telas.screens[7].quantidade_line.text()

            if(cpf and codigo and quantidade):
                conexao, cursor = abrir_banco_de_dados()


                lista_pecas = apply_sql_command(cursor, "SELECT valor_de_venda FROM Pecas WHERE codigo = '%s'" % (codigo), "fetchall")

                if(lista_pecas):
                    valor_de_venda = float(lista_pecas[0][0])

                    valor_total = valor_de_venda * int(quantidade)

                    data = date.today()

                    apply_sql_command(cursor, "INSERT INTO Vendas (quantidade, valor_total, data, cpf_cliente, codigo_peca) VALUES ('%s', '%s', '%s', '%s', '%s')" % (quantidade, str(valor_total), data, cpf, codigo))


                fechar_banco_de_dados(conexao)
