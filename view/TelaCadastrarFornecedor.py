from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QListView
from PyQt5 import QtCore

import sys

from view.Widgets import button, label, textEdit, lineEdit, comboBox
from view.StyleButton import style_button

from model.Observer import ISubject


class TelaCadastrarFornecedor(QWidget):
    def __init__(self, parent=None):
        super(TelaCadastrarFornecedor, self).__init__(parent)

        self.subject = ISubject()
        
        self._settings()
        self._create_widgets()
        self._set_style()
        self._setConnects()


    def _settings(self):
        self.setFixedSize(800, 740)
        self.setWindowTitle("Cadastrar fornecedor")
 

    def _create_widgets(self):
        self.formulario_label = label(self, "Formulario para Fornecedor", 240, 0, 561, 60)
        self.formulario_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.formulario_label.setAlignment(QtCore.Qt.AlignCenter)

        self.nome_fantasia_line = lineEdit(self, 390, 100, 261, 41)
        self.nome_fantasia_label = label(self, "Nome Fantasia", 240, 80, 561, 20)
        self.nome_fantasia_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.razao_social_line = lineEdit(self, 390, 180, 261, 41)
        self.razao_social_label = label(self, "Razão social", 240, 160, 561, 20)
        self.razao_social_label.setAlignment(QtCore.Qt.AlignCenter)

        self.cnpj_line = lineEdit(self, 390, 260, 261, 41)
        self.cnpj_label = label(self, "CNPJ", 240, 240, 561, 20)
        self.cnpj_label.setAlignment(QtCore.Qt.AlignCenter)

        self.inscricao_estadual_line = lineEdit(self, 390, 340, 261, 41)
        self.inscricao_estadual_label = label(self, "Inscrição Estadual", 240, 320, 561, 20)
        self.inscricao_estadual_label.setAlignment(QtCore.Qt.AlignCenter)

        self.endereco_line = lineEdit(self, 390, 420, 261, 41)
        self.endereco_label = label(self, "Endereço", 240, 400, 561, 20)
        self.endereco_label.setAlignment(QtCore.Qt.AlignCenter)

        self.telefone_line = lineEdit(self, 390, 500, 261, 41)
        self.telefone_label = label(self, "Telefone", 240, 480, 561, 20)
        self.telefone_label.setAlignment(QtCore.Qt.AlignCenter)

        self.email_line = lineEdit(self, 390, 580, 261, 41)
        self.email_label = label(self, "Email", 240, 560, 561, 20)
        self.email_label.setAlignment(QtCore.Qt.AlignCenter)

        self.cadastrar_botao = button(self, "Cadastrar", 390, 660, 261, 41)

        self.listView = QListView(self)
        self.listView.setGeometry(QtCore.QRect(0, 0, 241, 741))


    def _set_style(self):
        self.setStyleSheet("background-color: rgb(235, 235, 235);")

        self.listView.setStyleSheet("background-color: rgb(32, 29, 29);")
        
        self.formulario_label.setStyleSheet("font: 16pt;")
        self.nome_fantasia_label.setStyleSheet("font: 12pt;")
        self.razao_social_label.setStyleSheet("font: 12pt;")
        self.cnpj_label.setStyleSheet("font: 12pt;")
        self.inscricao_estadual_label.setStyleSheet("font: 12pt;")
        self.endereco_label.setStyleSheet("font: 12pt;")
        self.telefone_label.setStyleSheet("font: 12pt;")
        self.email_label.setStyleSheet("font: 12pt;")

        self.nome_fantasia_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.razao_social_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.cnpj_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.inscricao_estadual_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.endereco_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.telefone_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.email_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")

        style_button(button=self.cadastrar_botao, cor="cinza_escuro", tam_fonte="12", border_radius=(10, 10, 10, 10), rgb_da_letra="(210, 210, 210)")


    def _setConnects(self):
        self.cadastrar_botao.clicked.connect(self.botaoCadastrar)


    def clear(self, *widget_names):
        self.nome_fantasia_line.clear()
        self.razao_social_line.clear()
        self.cnpj_line.clear()
        self.inscricao_estadual_line.clear()
        self.endereco_line.clear()
        self.telefone_line.clear()
        self.email_line.clear()


    def botaoCadastrar(self):
        event = {"codigo": 2, "descricao": "Botão CADASTRAR da tela CADASTRAR FUNCIONÁRIO"}
        self.subject.notify(event)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaCadastrarFornecedor()
    app.show()
    sys.exit(root.exec_())
