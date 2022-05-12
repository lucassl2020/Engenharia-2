from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command


class GerenciarClientes(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 7: # BUSCAR
            cpf = self._stack_telas.screens[5].cpf_line.text()
            self._stack_telas.screens[5].clear()

            if(cpf):
                conexao, cursor = abrir_banco_de_dados()

                lista_clientes = apply_sql_command(cursor, "SELECT * FROM Clientes WHERE cpf = '%s'" % (cpf), "fetchall")

                fechar_banco_de_dados(conexao)
                
                if lista_clientes:
                    cliente = lista_clientes[0]
                    self._stack_telas.screens[5].nome_line.setText(str(cliente[1]))
                    self._stack_telas.screens[5].cpf_resultado_line.setText(str(cliente[0]))
                    self._stack_telas.screens[5].endereco_line.setText(str(cliente[2]))
                    self._stack_telas.screens[5].data_nascimento_line.setText(str(cliente[3]))
                    self._stack_telas.screens[5].telefone_line.setText(str(cliente[4]))
                

        if event["codigo"] == 8: # SALVAR
            cpf =  self._stack_telas.screens[5].cpf_resultado_line.text()
            nome = self._stack_telas.screens[5].nome_line.text()
            endereco = self._stack_telas.screens[5].endereco_line.text()
            data_nascimento = self._stack_telas.screens[5].data_nascimento_line.text()
            telefone = self._stack_telas.screens[5].telefone_line.text()
         
            if(cpf and nome and endereco and data_nascimento and telefone):
                conexao, cursor = abrir_banco_de_dados()

                lista_clientes = apply_sql_command(cursor, "UPDATE Clientes SET nome = '%s', endereco = '%s', data_de_nascimento = '%s', telefone = '%s' WHERE cpf = '%s'" % (nome, endereco, data_nascimento, telefone, cpf), "fetchall")

                fechar_banco_de_dados(conexao)
            

        if event["codigo"] == 9: # EXCLUIR
            cpf =  self._stack_telas.screens[5].cpf_resultado_line.text()

            if(cpf):
                conexao, cursor = abrir_banco_de_dados()

                lista_clientes = apply_sql_command(cursor, "DELETE FROM Clientes WHERE cpf = '%s'" % (cpf), "fetchall")

                fechar_banco_de_dados(conexao)

                self._stack_telas.screens[5].clear()
