from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command


class GerenciarPeca(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 4: # BUSCAR
            codigo = self._stack_telas.screens[3].codigo_line.text()
            self._stack_telas.screens[3].clear()

            if(codigo):
                conexao, cursor = abrir_banco_de_dados()

                lista_pecas = apply_sql_command(cursor, "SELECT * FROM Pecas WHERE codigo = '%s'" % (codigo), "fetchall")

                fechar_banco_de_dados(conexao)
                
                if lista_pecas:
                    peca = lista_pecas[0]
                    self._stack_telas.screens[3].nome_line.setText(str(peca[1]))
                    self._stack_telas.screens[3].codigo_resultado_line.setText(str(peca[0]))
                    self._stack_telas.screens[3].valor_custo_line.setText(str(peca[2]))
                    self._stack_telas.screens[3].valor_venda_line.setText(str(peca[3]))
                    self._stack_telas.screens[3].codigo_fornecedor_line.setText(str(peca[4]))
                

        if event["codigo"] == 5: # SALVAR
            codigo =  self._stack_telas.screens[3].codigo_resultado_line.text()
            nome = self._stack_telas.screens[3].nome_line.text()
            valor_custo = self._stack_telas.screens[3].valor_custo_line.text()
            valor_venda = self._stack_telas.screens[3].valor_venda_line.text()
            codigo_fornecedor = self._stack_telas.screens[3].codigo_fornecedor_line.text()
            

            if(codigo and nome and valor_custo and valor_venda and codigo_fornecedor):
                conexao, cursor = abrir_banco_de_dados()

                lista_pecas = apply_sql_command(cursor, "UPDATE Pecas SET nome = '%s', valor_de_custo = '%s', valor_de_venda = '%s', codigo_fornecedor = '%s' WHERE codigo = '%s'" % (nome, valor_custo, valor_venda, codigo_fornecedor, codigo), "fetchall")

                fechar_banco_de_dados(conexao)
            

        if event["codigo"] == 6: # EXCLUIR
            codigo = self._stack_telas.screens[3].codigo_resultado_line.text()

            if(codigo):
                conexao, cursor = abrir_banco_de_dados()

                lista_pecas = apply_sql_command(cursor, "DELETE FROM Pecas WHERE codigo = '%s'" % (codigo), "fetchall")

                fechar_banco_de_dados(conexao)

                self._stack_telas.screens[3].clear()
