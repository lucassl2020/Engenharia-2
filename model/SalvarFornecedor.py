from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command


class SalvarFornecedor(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 2:

            cnpj = self._stack_telas.screens[1].cnpj_line.text()
            nome_fantasia = self._stack_telas.screens[1].nome_fantasia_line.text()
            razao_social = self._stack_telas.screens[1].razao_social_line.text()
            telefone = self._stack_telas.screens[1].telefone_line.text()
            endereco = self._stack_telas.screens[1].endereco_line.text()
            inscricao_estadual = self._stack_telas.screens[1].inscricao_estadual_line.text()
            email = self._stack_telas.screens[1].email_line.text()

            conexao, cursor = abrir_banco_de_dados()


            apply_sql_command(cursor, "INSERT INTO Fornecedores (cnpj, nome_fantasia, razao_social, telefone, endereco, inscricao_estadual, email) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (cnpj, nome_fantasia, razao_social, telefone, endereco, inscricao_estadual, email))
            

            fechar_banco_de_dados(conexao)
