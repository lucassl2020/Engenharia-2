from PyQt5.QtWidgets import QApplication, QWidget

import sys

from view.Widgets import button
from view.StyleButton import style_button

from model.Observer import ISubject


class TelaInicial(QWidget):
    def __init__(self, parent=None):
        super(TelaInicial, self).__init__(parent)

        self.subject = ISubject()

        self._settings()
        self._create_widgets()
        self._set_style()
        self._setConnects()


    def _settings(self):
        self.setFixedSize(1010, 370)
        self.setWindowTitle("Inicio")
 

    def _create_widgets(self):
        self.cadastrar_peca = button(self, "Cadastrar peça", 20, 30, 310, 50)
        self.cadastrar_cliente = button(self, "Cadastrar cliente", 350, 30, 310, 50)
        self.cadastrar_fornecedor = button(self, "Cadastrar fornecedor", 680, 30, 310, 50)
        self.lista_pecas = button(self, "Lista de peças", 20, 120, 310, 50)
        self.lista_clientes = button(self, "Lista de clientes", 350, 120, 310, 50)
        self.lista_fornecedores = button(self, "Lista de fornecedores", 680, 120, 310, 50)
        self.lista_vendas = button(self, "Lista de vendas", 20, 210, 310, 50)
        self.gerenciar_pecas = button(self, "Gerenciar peças", 350, 210, 310, 50)
        self.gerenciar_clientes = button(self, "Gerenciar clientes", 680, 210, 310, 50)
        self.gerenciar_fornecedores = button(self, "Gerenciar fornecedores", 20, 300, 310, 50)
        self.realizar_vendas = button(self, "Realizar venda", 350, 300, 310, 50)
        

    def _set_style(self):
        self.setStyleSheet("background-color: rgb(54, 54, 54);")

        style_button(button=self.cadastrar_peca, cor="cinza_escuro", tam_fonte="14", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.cadastrar_cliente, cor="cinza_escuro", tam_fonte="14", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.cadastrar_fornecedor, cor="cinza_escuro", tam_fonte="14", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.lista_pecas, cor="cinza_escuro", tam_fonte="14", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.lista_clientes, cor="cinza_escuro", tam_fonte="14", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.lista_fornecedores, cor="cinza_escuro", tam_fonte="14", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.lista_vendas, cor="cinza_escuro", tam_fonte="14", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.gerenciar_pecas, cor="cinza_escuro", tam_fonte="14", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.gerenciar_clientes, cor="cinza_escuro", tam_fonte="14", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.gerenciar_fornecedores, cor="cinza_escuro", tam_fonte="14", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.realizar_vendas, cor="cinza_escuro", tam_fonte="14", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")


    def _setConnects(self):
        self.cadastrar_peca.clicked.connect(self.botaoCadastrarPeca)
        self.cadastrar_cliente.clicked.connect(self.botaoCadastrarCliente)
        self.cadastrar_fornecedor.clicked.connect(self.botaoCadastrarFornecedor)
        self.lista_pecas.clicked.connect(self.botaoListaPecas)
        self.lista_clientes.clicked.connect(self.botaoListaClientes)
        self.lista_fornecedores.clicked.connect(self.botaoListaFornecedores)
        self.lista_vendas.clicked.connect(self.botaoListaVendas)
        self.gerenciar_pecas.clicked.connect(self.botaoGerenciarPecas)
        self.gerenciar_clientes.clicked.connect(self.botaoGerenciarClientes)
        self.gerenciar_fornecedores.clicked.connect(self.botaoGerenciarFornecedores)
        self.realizar_vendas.clicked.connect(self.botaoRealizarVenda)
    

    def botaoCadastrarPeca(self):
        event = {"codigo": 14, "descricao": "Botão CADASTRAR PECA da tela INICIAL"}
        self.subject.notify(event)

    def botaoCadastrarCliente(self):
        event = {"codigo": 15, "descricao": "Botão CADASTRAR CLIENTE da tela INICIAL"}
        self.subject.notify(event)

    def botaoCadastrarFornecedor(self):
        event = {"codigo": 16, "descricao": "Botão CADASTRAR FORNECEDOR da tela INICIAL"}
        self.subject.notify(event)

    def botaoListaPecas(self):
        event = {"codigo": 17, "descricao": "Botão LISTA PECAS da tela INICIAL"}
        self.subject.notify(event)

    def botaoListaClientes(self):
        event = {"codigo": 18, "descricao": "Botão LISTA CLIENTES da tela INICIAL"}
        self.subject.notify(event)

    def botaoListaFornecedores(self):
        event = {"codigo": 19, "descricao": "Botão LISTA FORNECEDORES da tela INICIAL"}
        self.subject.notify(event)

    def botaoListaVendas(self):
        event = {"codigo": 20, "descricao": "Botão LISTA VENDAS da tela INICIAL"}
        self.subject.notify(event)

    def botaoGerenciarPecas(self):
        event = {"codigo": 21, "descricao": "Botão GERENCIAR PECAS da tela INICIAL"}
        self.subject.notify(event)

    def botaoGerenciarClientes(self):
        event = {"codigo": 22, "descricao": "Botão GERENCIAR CLIENTES da tela INICIAL"}
        self.subject.notify(event)

    def botaoGerenciarFornecedores(self):
        event = {"codigo": 23, "descricao": "Botão GERENCIAR FORNECEDORES da tela INICIAL"}
        self.subject.notify(event)

    def botaoRealizarVenda(self):
        event = {"codigo": 24, "descricao": "Botão REALIZAR VENDA da tela INICIAL"}
        self.subject.notify(event)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaInicial()
    app.show()
    sys.exit(root.exec_())
