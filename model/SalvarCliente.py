from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command


class SalvarCliente(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 3:
            cpf = self._stack_telas.screens[0].cpf_line.text()
            nome = self._stack_telas.screens[0].nome_line.text()
            endereco = self._stack_telas.screens[0].endereco_line.text()
            data_de_nascimento = self._stack_telas.screens[0].data_nascimento_line.text()
            telefone = self._stack_telas.screens[0].telefone_line.text()

            conexao, cursor = abrir_banco_de_dados()


            apply_sql_command(cursor, "INSERT INTO Clientes (cpf, nome, endereco, data_de_nascimento, telefone) VALUES ('%s', '%s', '%s', '%s', '%s')" % (cpf, nome, endereco, data_de_nascimento, telefone))
            

            fechar_banco_de_dados(conexao)
