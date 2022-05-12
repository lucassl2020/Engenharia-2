from PyQt5.QtWidgets import QApplication, QMessageBox

import sys

from view.TelaCadastrarCliente import TelaCadastrarCliente
from view.TelaCadastrarFornecedor import TelaCadastrarFornecedor
from view.TelaCadastrarPeca import TelaCadastrarPeca
from view.TelaGerenciarPecas import TelaGerenciarPecas
from view.TelaGerenciarClientes import TelaGerenciarClientes
from view.TelaGerenciarFornecedores import TelaGerenciarFornecedores
from view.TelaRealizarVendas import TelaRealizarVendas
from view.TelaListaPecas import TelaListaPecas
from view.TelaListaClientes import TelaListaClientes
from view.TelaListaFornecedores import TelaListaFornecedores
from view.TelaListaVendas import TelaListaVendas
from view.TelaInicial import TelaInicial

from view.StackTelas import StackTelas

from model.CreateDatabase import create_database
from model.SalvarPeca import SalvarPeca
from model.SalvarCliente import SalvarCliente
from model.SalvarFornecedor import SalvarFornecedor
from model.GerenciarPeca import GerenciarPeca
from model.GerenciarClientes import GerenciarClientes
from model.GerenciarFornecedores import GerenciarFornecedores
from model.RealizarVenda import RealizarVenda
from model.AbrirTelaListaPeca import AbrirTelaListaPeca
from model.AbrirTelaListaClientes import AbrirTelaListaClientes
from model.AbrirTelaCadastrarPecas import AbrirTelaCadastrarPecas
from model.AbrirTelaCadastrarClientes import AbrirTelaCadastrarClientes
from model.AbrirTelaCadastrarFornecedores import AbrirTelaCadastrarFornecedores
from model.AbrirTelaListaFornecedores import AbrirTelaListaFornecedores
from model.AbrirTelaListaVendas import AbrirTelaListaVendas
from model.AbrirTelaGerenciarPecas import AbrirTelaGerenciarPecas
from model.AbrirTelaGerenciarClientes import AbrirTelaGerenciarClientes
from model.AbrirTelaGerenciarFornecedores import AbrirTelaGerenciarFornecedores
from model.AbrirTelaRealizarVendas import AbrirTelaRealizarVendas
from model.AbrirTelaInicial import AbrirTelaInicial


def create_screens():
	telas = []

	telas.append(TelaInicial()) # 0

	telas.append(TelaCadastrarCliente()) # 1

	telas.append(TelaCadastrarFornecedor()) # 2

	telas.append(TelaCadastrarPeca()) # 3

	telas.append(TelaGerenciarPecas()) # 4

	telas.append(TelaGerenciarClientes()) # 5

	telas.append(TelaGerenciarFornecedores()) # 6

	telas.append(TelaRealizarVendas()) # 7

	telas.append(TelaListaPecas()) # 8

	telas.append(TelaListaClientes()) # 9

	telas.append(TelaListaFornecedores()) # 10

	telas.append(TelaListaVendas()) # 11

	return telas


def create_observers(stack_telas):
	abrir_tela_inicial = AbrirTelaInicial(stack_telas)


	stack_telas.screens[0].subject.subscribe(AbrirTelaCadastrarPecas(stack_telas))
	stack_telas.screens[0].subject.subscribe(AbrirTelaCadastrarClientes(stack_telas))
	stack_telas.screens[0].subject.subscribe(AbrirTelaCadastrarFornecedores(stack_telas))
	stack_telas.screens[0].subject.subscribe(AbrirTelaListaPeca(stack_telas))
	stack_telas.screens[0].subject.subscribe(AbrirTelaListaClientes(stack_telas))
	stack_telas.screens[0].subject.subscribe(AbrirTelaListaFornecedores(stack_telas))
	stack_telas.screens[0].subject.subscribe(AbrirTelaListaVendas(stack_telas))
	stack_telas.screens[0].subject.subscribe(AbrirTelaGerenciarPecas(stack_telas))
	stack_telas.screens[0].subject.subscribe(AbrirTelaGerenciarClientes(stack_telas))
	stack_telas.screens[0].subject.subscribe(AbrirTelaGerenciarFornecedores(stack_telas))
	stack_telas.screens[0].subject.subscribe(AbrirTelaRealizarVendas(stack_telas))

	stack_telas.screens[1].subject.subscribe(abrir_tela_inicial)
	stack_telas.screens[2].subject.subscribe(abrir_tela_inicial)
	stack_telas.screens[3].subject.subscribe(abrir_tela_inicial)
	stack_telas.screens[4].subject.subscribe(abrir_tela_inicial)
	stack_telas.screens[5].subject.subscribe(abrir_tela_inicial)
	stack_telas.screens[6].subject.subscribe(abrir_tela_inicial)
	stack_telas.screens[7].subject.subscribe(abrir_tela_inicial)
	stack_telas.screens[8].subject.subscribe(abrir_tela_inicial)
	stack_telas.screens[9].subject.subscribe(abrir_tela_inicial)
	stack_telas.screens[10].subject.subscribe(abrir_tela_inicial)
	stack_telas.screens[11].subject.subscribe(abrir_tela_inicial)

	stack_telas.screens[3].subject.subscribe(SalvarPeca(stack_telas))

	stack_telas.screens[1].subject.subscribe(SalvarCliente(stack_telas))

	stack_telas.screens[2].subject.subscribe(SalvarFornecedor(stack_telas))

	stack_telas.screens[4].subject.subscribe(GerenciarPeca(stack_telas))

	stack_telas.screens[5].subject.subscribe(GerenciarClientes(stack_telas))

	stack_telas.screens[6].subject.subscribe(GerenciarFornecedores(stack_telas))

	stack_telas.screens[7].subject.subscribe(RealizarVenda(stack_telas))


if __name__ == '__main__':
	root = QApplication(sys.argv)


	create_database()
	stack_telas = StackTelas(create_screens())
	create_observers(stack_telas)


	sys.exit(root.exec_())
