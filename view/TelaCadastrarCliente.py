from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QListView
from PyQt5 import QtCore

import sys

from view.Widgets import button, label, textEdit, lineEdit, comboBox
from view.StyleButton import style_button

from model.Observer import ISubject


class TelaCadastrarCliente(QWidget):
    def __init__(self, parent=None):
        super(TelaCadastrarCliente, self).__init__(parent)

        self.subject = ISubject()
        
        self._settings()
        self._create_widgets()
        self._set_style()
        self._setConnects()


    def _settings(self):
        self.setFixedSize(800, 740)
        self.setWindowTitle("Cadastrar cliente")
 

    def _create_widgets(self):
        self.formulario_label = label(self, "Formulario para Cliente", 240, 0, 561, 60)
        self.formulario_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.formulario_label.setAlignment(QtCore.Qt.AlignCenter)

        self.nome_line = lineEdit(self, 390, 100, 261, 41)
        self.nome_label = label(self, "Nome", 240, 80, 561, 20)
        self.nome_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.cpf_line = lineEdit(self, 390, 180, 261, 41)
        self.cpf_label = label(self, "Cpf", 240, 160, 561, 20)
        self.cpf_label.setAlignment(QtCore.Qt.AlignCenter)

        self.endereco_line = lineEdit(self, 390, 260, 261, 41)
        self.endereco_label = label(self, "Endereço", 240, 240, 561, 20)
        self.endereco_label.setAlignment(QtCore.Qt.AlignCenter)

        self.data_nascimento_line = lineEdit(self, 390, 340, 261, 41)
        self.data_nascimento_label = label(self, "Data de nascimento", 240, 320, 561, 20)
        self.data_nascimento_label.setAlignment(QtCore.Qt.AlignCenter)

        self.telefone_line = lineEdit(self, 390, 420, 261, 41)
        self.telefone_label = label(self, "Telefone", 240, 400, 561, 20)
        self.telefone_label.setAlignment(QtCore.Qt.AlignCenter)

        self.cadastrar_botao = button(self, "Cadastrar", 390, 500, 261, 41)

        self.listView = QListView(self)
        self.listView.setGeometry(QtCore.QRect(0, 0, 241, 741))


    def _set_style(self):
        self.setStyleSheet("background-color: rgb(235, 235, 235);")

        self.listView.setStyleSheet("background-color: rgb(32, 29, 29);")
        
        self.formulario_label.setStyleSheet("font: 16pt;")
        self.nome_label.setStyleSheet("font: 12pt;")
        self.cpf_label.setStyleSheet("font: 12pt;")
        self.endereco_label.setStyleSheet("font: 12pt;")
        self.data_nascimento_label.setStyleSheet("font: 12pt;")
        self.telefone_label.setStyleSheet("font: 12pt;")

        self.nome_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.cpf_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.endereco_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.data_nascimento_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.telefone_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")

        style_button(button=self.cadastrar_botao, cor="cinza_escuro", tam_fonte="12", border_radius=(10, 10, 10, 10), rgb_da_letra="(210, 210, 210)")


    def _setConnects(self):
        self.cadastrar_botao.clicked.connect(self.botaoCadastrar)
        

    def clear(self, *widget_names):
        self.nome_line.clear()
        self.cpf_line.clear()
        self.endereco_line.clear()
        self.data_nascimento_line.clear()
        self.telefone_line.clear()

    
    def botaoCadastrar(self):
        event = {"codigo": 3, "descricao": "Botão CADASTRAR da tela CADASTRAR CLIENTE"}
        self.subject.notify(event)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaCadastrarCliente()
    app.show()
    sys.exit(root.exec_())
