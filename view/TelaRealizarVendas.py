from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QListView
from PyQt5 import QtCore

import sys

from view.Widgets import button, label, textEdit, lineEdit, comboBox
from view.StyleButton import style_button

from model.Observer import ISubject


class TelaRealizarVendas(QWidget):
    def __init__(self, parent=None):
        super(TelaRealizarVendas, self).__init__(parent)

        self.subject = ISubject()
        
        self._settings()
        self._create_widgets()
        self._set_style()
        self._setConnects()


    def _settings(self):
        self.setFixedSize(600, 500)
        self.setWindowTitle("Realizar vendas")
 

    def _create_widgets(self):
        self.realizar_venda_label = label(self, "Realizar vendas", 0, 0, 600, 60)
        self.realizar_venda_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.realizar_venda_label.setAlignment(QtCore.Qt.AlignCenter)

        self.cpf_line = lineEdit(self, 170, 100, 261, 41)
        self.cpf_label = label(self, "Cpf do cliente", 0, 80, 600, 20)
        self.cpf_label.setAlignment(QtCore.Qt.AlignCenter)

        self.codigo_peca_line = lineEdit(self, 170, 180, 261, 41)
        self.codigo_peca_label = label(self, "Código da peça", 0, 160, 600, 20)
        self.codigo_peca_label.setAlignment(QtCore.Qt.AlignCenter)

        self.quantidade_line = lineEdit(self, 170, 260, 261, 41)
        self.quantidade_label = label(self, "Quantidade de peças", 0, 240, 600, 20)
        self.quantidade_label.setAlignment(QtCore.Qt.AlignCenter)

        self.confirmar_botao = button(self, "Confirmar", 170, 340, 261, 41)
        self.voltar_botao = button(self, "Voltar", 170, 400, 261, 41)


    def _set_style(self):
        self.setStyleSheet("background-color: rgb(235, 235, 235);")
        
        self.realizar_venda_label.setStyleSheet("font: 16pt;")

        style_button(button=self.confirmar_botao, cor="cinza_escuro", tam_fonte="12", border_radius=(10, 10, 10, 10), rgb_da_letra="(210, 210, 210)")

        self.cpf_label.setStyleSheet("font: 12pt;")
        self.codigo_peca_label.setStyleSheet("font: 12pt;")
        self.quantidade_label.setStyleSheet("font: 12pt;")

        self.cpf_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.codigo_peca_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.quantidade_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")

        style_button(button=self.voltar_botao, cor="cinza", tam_fonte="12", border_radius=(10, 10, 10, 10), rgb_da_letra="(36, 36, 36)")


    def _setConnects(self):
        self.confirmar_botao.clicked.connect(self.botaoConfirmar)
        self.voltar_botao.clicked.connect(self.botaoVoltar)


    def clear(self, *widget_names):
        self.cpf_line.clear()
        self.codigo_peca_line.clear()
        self.quantidade_line.clear()
    

    def botaoConfirmar(self):
        event = {"codigo": 13, "descricao": "Botão CONFIRMAR da tela REALIZAR VENDAS"}
        self.subject.notify(event)

    def botaoVoltar(self):
        event = {"codigo": 31, "descricao": "Botão VOLTAR da tela REALIZAR VENDAS"}
        self.subject.notify(event)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaRealizarVendas()
    app.show()
    sys.exit(root.exec_())
