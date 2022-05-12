from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command


class AbrirTelaInicial(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] in (25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35):
            self._stack_telas.open_screen(0)
