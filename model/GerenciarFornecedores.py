from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command


class GerenciarFornecedores(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 10: # BUSCAR
            cnpj = self._stack_telas.screens[5].CNPJ_line.text()
            self._stack_telas.screens[5].clear()

            if(cnpj):
                conexao, cursor = abrir_banco_de_dados()

                lista_fornecedores = apply_sql_command(cursor, "SELECT * FROM Fornecedores WHERE cnpj = '%s'" % (cnpj), "fetchall")

                fechar_banco_de_dados(conexao)
 
                if lista_fornecedores:
                    fornecedor = lista_fornecedores[0]
                    self._stack_telas.screens[5].CNPJ_resultado_line.setText(str(fornecedor[0]))
                    self._stack_telas.screens[5].nome_fantasia_line.setText(str(fornecedor[1]))
                    self._stack_telas.screens[5].razao_social_line.setText(str(fornecedor[2]))
                    self._stack_telas.screens[5].inscricao_estadual_line.setText(str(fornecedor[5]))
                    self._stack_telas.screens[5].endereco_line.setText(str(fornecedor[4]))
                    self._stack_telas.screens[5].telefone_line.setText(str(fornecedor[3]))
                    self._stack_telas.screens[5].email_line.setText(str(fornecedor[6]))


        if event["codigo"] == 11: # SALVAR
            cnpj = self._stack_telas.screens[5].CNPJ_resultado_line.text()
            nome_fantasia_line = self._stack_telas.screens[5].nome_fantasia_line.text()
            razao_social = self._stack_telas.screens[5].razao_social_line.text()
            inscricao_estadual = self._stack_telas.screens[5].inscricao_estadual_line.text()
            endereco = self._stack_telas.screens[5].endereco_line.text()
            telefone = self._stack_telas.screens[5].telefone_line.text()
            email = self._stack_telas.screens[5].email_line.text()                                                                                                                                                                                                                                  
                                                                                                                                                                
            if(cnpj and nome_fantasia_line and razao_social and inscricao_estadual and endereco and telefone and email):
                conexao, cursor = abrir_banco_de_dados()

                lista_fornecedores = apply_sql_command(cursor, "UPDATE Fornecedores SET nome_fantasia = '%s', razao_social = '%s', telefone = '%s', endereco = '%s', inscricao_estadual = '%s', email = '%s' WHERE cnpj = '%s'" % (nome_fantasia_line, razao_social, telefone, endereco, inscricao_estadual, email, cnpj), "fetchall")

                fechar_banco_de_dados(conexao)


        if event["codigo"] == 12: # EXCLUIR
            cnpj =  self._stack_telas.screens[5].CNPJ_resultado_line.text()

            if(cnpj):
                conexao, cursor = abrir_banco_de_dados()

                lista_fornecedores = apply_sql_command(cursor, "DELETE FROM Fornecedores WHERE cnpj = '%s'" % (cnpj), "fetchall")

                fechar_banco_de_dados(conexao)

                self._stack_telas.screens[5].clear()

