from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command


class AbrirTelaCadastrarClientes(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 15:
            self._stack_telas.screens[1].clear()
            self._stack_telas.open_screen(1)
