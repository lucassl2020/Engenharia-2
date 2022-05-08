from PyQt5.QtWidgets import QApplication, QMessageBox

import sys

from view.TelaCadastrarCliente import TelaCadastrarCliente
from view.TelaCadastrarFornecedor import TelaCadastrarFornecedor
from view.TelaCadastrarPeca import TelaCadastrarPeca
from view.TelaGerenciarPecas import TelaGerenciarPecas
from view.TelaGerenciarClientes import TelaGerenciarClientes
from view.TelaGerenciarFornecedores import TelaGerenciarFornecedores
from view.StackTelas import StackTelas

from model.CreateDatabase import create_database
from model.SalvarPeca import SalvarPeca
from model.SalvarCliente import SalvarCliente
from model.SalvarFornecedor import SalvarFornecedor
from model.GerenciarPeca import GerenciarPeca
from model.GerenciarClientes import GerenciarClientes
from model.GerenciarFornecedores import GerenciarFornecedores



def create_screens():
	telas = []

	telas.append(TelaCadastrarCliente()) # 0

	telas.append(TelaCadastrarFornecedor()) # 1

	telas.append(TelaCadastrarPeca()) # 2

	telas.append(TelaGerenciarPecas()) # 3

	telas.append(TelaGerenciarClientes()) # 4

	telas.append(TelaGerenciarFornecedores()) # 5

	return telas


def create_observers(stack_telas):
	stack_telas.screens[2].subject.subscribe(SalvarPeca(stack_telas))

	stack_telas.screens[0].subject.subscribe(SalvarCliente(stack_telas))

	stack_telas.screens[1].subject.subscribe(SalvarFornecedor(stack_telas))

	stack_telas.screens[3].subject.subscribe(GerenciarPeca(stack_telas))

	stack_telas.screens[4].subject.subscribe(GerenciarClientes(stack_telas))

	stack_telas.screens[5].subject.subscribe(GerenciarFornecedores(stack_telas))


if __name__ == '__main__':
	root = QApplication(sys.argv)


	create_database()
	stack_telas = StackTelas(create_screens())
	create_observers(stack_telas)

	stack_telas.open_screen(5)


	sys.exit(root.exec_())
