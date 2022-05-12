from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QListView
from PyQt5 import QtCore

import sys

from view.Widgets import button, label, textEdit, lineEdit, comboBox
from view.StyleButton import style_button

from model.Observer import ISubject


class TelaCadastrarPeca(QWidget):
    def __init__(self, parent=None):
        super(TelaCadastrarPeca, self).__init__(parent)

        self.subject = ISubject()
        
        self._settings()
        self._create_widgets()
        self._set_style()
        self._setConnects()


    def _settings(self):
        self.setFixedSize(600, 740)
        self.setWindowTitle("Cadastrar peças")
 

    def _create_widgets(self):
        self.formulario_label = label(self, "Formulario para Peças Automotivas", 0, 0, 600, 60)
        self.formulario_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.formulario_label.setAlignment(QtCore.Qt.AlignCenter)

        self.nome_line = lineEdit(self, 170, 100, 261, 41)
        self.nome_label = label(self, "Nome", 0, 80, 600, 20)
        self.nome_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.codigo_line = lineEdit(self, 170, 180, 261, 41)
        self.codigo_label = label(self, "Codigo", 0, 160, 600, 20)
        self.codigo_label.setAlignment(QtCore.Qt.AlignCenter)

        self.valor_custo_line = lineEdit(self, 170, 260, 261, 41)
        self.valor_custo_label = label(self, "Valor de custo", 0, 240, 600, 20)
        self.valor_custo_label.setAlignment(QtCore.Qt.AlignCenter)

        self.valor_venda_line = lineEdit(self, 170, 340, 261, 41)
        self.valor_venda_label = label(self, "Valor de venda", 0, 320, 600, 20)
        self.valor_venda_label.setAlignment(QtCore.Qt.AlignCenter)

        self.codigo_fornecedor_line = lineEdit(self, 170, 420, 261, 41)
        self.codigo_fornecedor_label = label(self, "Codigo do fornecedor", 0, 400, 600, 20)
        self.codigo_fornecedor_label.setAlignment(QtCore.Qt.AlignCenter)

        self.cadastrar_botao = button(self, "Cadastrar", 170, 500, 261, 41)
        self.voltar_botao = button(self, "Voltar", 170, 560, 261, 41)


    def _set_style(self):
        self.setStyleSheet("background-color: rgb(235, 235, 235);")
        
        self.formulario_label.setStyleSheet("font: 16pt;")
        self.nome_label.setStyleSheet("font: 12pt;")
        self.codigo_label.setStyleSheet("font: 12pt;")
        self.valor_custo_label.setStyleSheet("font: 12pt;")
        self.valor_venda_label.setStyleSheet("font: 12pt;")
        self.codigo_fornecedor_label.setStyleSheet("font: 12pt;")

        self.nome_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.codigo_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.valor_custo_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.valor_venda_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.codigo_fornecedor_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")

        style_button(button=self.cadastrar_botao, cor="cinza_escuro", tam_fonte="12", border_radius=(10, 10, 10, 10), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.voltar_botao, cor="cinza", tam_fonte="12", border_radius=(10, 10, 10, 10), rgb_da_letra="(36, 36, 36)")


    def _setConnects(self):
        self.cadastrar_botao.clicked.connect(self.botaoCadastrar)
        self.voltar_botao.clicked.connect(self.botaoVoltar)


    def clear(self, *widget_names):
        self.nome_line.clear()
        self.codigo_line.clear()
        self.valor_custo_line.clear()
        self.valor_venda_line.clear()
        self.codigo_fornecedor_line.clear()

    
    def botaoCadastrar(self):
        event = {"codigo": 1, "descricao": "Botão CADASTRAR da tela CADASTRAR PEÇAS"}
        self.subject.notify(event)

    def botaoVoltar(self):
        event = {"codigo": 27, "descricao": "Botão VOLTAR da tela CADASTRAR PEÇAS"}
        self.subject.notify(event)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaCadastrarPeca()
    app.show()
    sys.exit(root.exec_())
