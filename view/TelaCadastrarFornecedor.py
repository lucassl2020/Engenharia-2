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
        self.setFixedSize(600, 800)
        self.setWindowTitle("Cadastrar fornecedor")
 

    def _create_widgets(self):
        self.formulario_label = label(self, "Formulario para Fornecedor", 0, 0, 600, 60)
        self.formulario_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.formulario_label.setAlignment(QtCore.Qt.AlignCenter)

        self.nome_fantasia_line = lineEdit(self, 170, 100, 261, 41)
        self.nome_fantasia_label = label(self, "Nome Fantasia", 0, 80, 600, 20)
        self.nome_fantasia_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.razao_social_line = lineEdit(self, 170, 180, 261, 41)
        self.razao_social_label = label(self, "Razão social", 0, 160, 600, 20)
        self.razao_social_label.setAlignment(QtCore.Qt.AlignCenter)

        self.cnpj_line = lineEdit(self, 170, 260, 261, 41)
        self.cnpj_label = label(self, "CNPJ", 0, 240, 600, 20)
        self.cnpj_label.setAlignment(QtCore.Qt.AlignCenter)

        self.inscricao_estadual_line = lineEdit(self, 170, 340, 261, 41)
        self.inscricao_estadual_label = label(self, "Inscrição Estadual", 0, 320, 600, 20)
        self.inscricao_estadual_label.setAlignment(QtCore.Qt.AlignCenter)

        self.endereco_line = lineEdit(self, 170, 420, 261, 41)
        self.endereco_label = label(self, "Endereço", 0, 400, 600, 20)
        self.endereco_label.setAlignment(QtCore.Qt.AlignCenter)

        self.telefone_line = lineEdit(self, 170, 500, 261, 41)
        self.telefone_label = label(self, "Telefone", 0, 480, 600, 20)
        self.telefone_label.setAlignment(QtCore.Qt.AlignCenter)

        self.email_line = lineEdit(self, 170, 580, 261, 41)
        self.email_label = label(self, "Email", 0, 560, 600, 20)
        self.email_label.setAlignment(QtCore.Qt.AlignCenter)

        self.cadastrar_botao = button(self, "Cadastrar", 170, 660, 261, 41)
        self.voltar_botao = button(self, "Voltar", 170, 720, 261, 41)


    def _set_style(self):
        self.setStyleSheet("background-color: rgb(235, 235, 235);")
        
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
        style_button(button=self.voltar_botao, cor="cinza", tam_fonte="12", border_radius=(10, 10, 10, 10), rgb_da_letra="(36, 36, 36)")


    def _setConnects(self):
        self.cadastrar_botao.clicked.connect(self.botaoCadastrar)
        self.voltar_botao.clicked.connect(self.botaoVoltar)


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

    def botaoVoltar(self):
        event = {"codigo": 26, "descricao": "Botão VOLTAR da tela CADASTRAR FUNCIONÁRIO"}
        self.subject.notify(event)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaCadastrarFornecedor()
    app.show()
    sys.exit(root.exec_())
