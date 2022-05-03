from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command


class GerenciarPeca(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 4: #BUSCAR
            codigo = self._stack_telas.screens[2].codigo_line.text()
            nome = self._stack_telas.screens[2].nome_line.text()
            valor_de_custo = self._stack_telas.screens[2].valor_custo_line.text()
            valor_de_venda = self._stack_telas.screens[2].valor_venda_line.text()
            codigo_fornecedor = self._stack_telas.screens[2].codigo_fornecedor_line.text()

            conexao, cursor = abrir_banco_de_dados()

            if(codigo and nome and valor_de_custo and valor_de_venda and codigo_fornecedor):
                apply_sql_command(cursor, "INSERT INTO Pecas (codigo, nome, valor_de_custo, valor_de_venda, codigo_fornecedor) VALUES ('%s', '%s', '%s', '%s', '%s')" % (codigo, nome, valor_de_custo, valor_de_venda, codigo_fornecedor))
            

            fechar_banco_de_dados(conexao)

        if event["codigo"] == 5: #BUSCAR


        if event["codigo"] == 6: #BUSCAR
