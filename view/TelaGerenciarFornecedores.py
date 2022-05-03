from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QListView
from PyQt5 import QtCore

import sys

from view.Widgets import button, label, textEdit, lineEdit, comboBox
from view.StyleButton import style_button

from model.Observer import ISubject


class TelaGerenciarFornecedores(QWidget):
    def __init__(self, parent=None):
        super(TelaGerenciarFornecedores, self).__init__(parent)

        self.subject = ISubject()
        
        self._settings()
        self._create_widgets()
        self._set_style()
        self._setConnects()


    def _settings(self):
        self.setFixedSize(800, 840)
        self.setWindowTitle("Gerenciar fornecedores")
 

    def _create_widgets(self):
        self.gerenciar_label = label(self, "Gerenciar fornecedores", 240, 0, 561, 60)
        self.gerenciar_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gerenciar_label.setAlignment(QtCore.Qt.AlignCenter)

        self.CNPJ_line = lineEdit(self, 390, 100, 261, 41)
        self.CNPJ_label = label(self, "CNPJ do fornecedor", 240, 80, 561, 20)
        self.CNPJ_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.buscar_botao = button(self, "Buscar", 390, 150, 261, 41)

        self.resultado_label = label(self, "Resultado", 240, 200, 561, 60)
        self.resultado_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.resultado_label.setAlignment(QtCore.Qt.AlignCenter)


        self.nome_fantasia_line = lineEdit(self, 390, 300, 261, 41)
        self.nome_fantasia_label = label(self, "Nome fantasia", 240, 280, 561, 20)
        self.nome_fantasia_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.razao_social_line = lineEdit(self, 390, 380, 261, 41)
        self.razao_social_label = label(self, "Razão social", 240, 360, 561, 20)
        self.razao_social_label.setAlignment(QtCore.Qt.AlignCenter)

        self.inscricao_estadual_line = lineEdit(self, 390, 460, 261, 41)
        self.inscricao_estadual_label = label(self, "Inscrição estudal", 240, 440, 561, 20)
        self.inscricao_estadual_label.setAlignment(QtCore.Qt.AlignCenter)

        self.endereco_line = lineEdit(self, 390, 540, 261, 41)
        self.endereco_label = label(self, "Endereço", 240, 520, 561, 20)
        self.endereco_label.setAlignment(QtCore.Qt.AlignCenter)

        self.telefone_line = lineEdit(self, 390, 620, 261, 41)
        self.telefone_label = label(self, "Telefone", 240, 600, 561, 20)
        self.telefone_label.setAlignment(QtCore.Qt.AlignCenter)

        self.email_line = lineEdit(self, 390, 700, 261, 41)
        self.email_label = label(self, "Email", 240, 680, 561, 20)
        self.email_label.setAlignment(QtCore.Qt.AlignCenter)


        self.salvar_botao = button(self, "Salvar", 390, 760, 130, 41)
        self.excluir_botao = button(self, "Excluir", 521, 760, 130, 41)

        self.listView = QListView(self)
        self.listView.setGeometry(QtCore.QRect(0, 0, 241, 841))


    def _set_style(self):
        self.setStyleSheet("background-color: rgb(235, 235, 235);")

        self.listView.setStyleSheet("background-color: rgb(32, 29, 29);")
        
        self.gerenciar_label.setStyleSheet("font: 16pt;")
        self.CNPJ_label.setStyleSheet("font: 12pt;")
        self.resultado_label.setStyleSheet("font: 16pt;")

        self.CNPJ_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")

        style_button(button=self.buscar_botao, cor="cinza_escuro", tam_fonte="12", border_radius=(10, 10, 10, 10), rgb_da_letra="(210, 210, 210)")

        self.nome_fantasia_label.setStyleSheet("font: 12pt;")
        self.razao_social_label.setStyleSheet("font: 12pt;")
        self.inscricao_estadual_label.setStyleSheet("font: 12pt;")
        self.endereco_label.setStyleSheet("font: 12pt;")
        self.telefone_label.setStyleSheet("font: 12pt;")
        self.email_label.setStyleSheet("font: 12pt;")

        self.nome_fantasia_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.razao_social_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.inscricao_estadual_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.endereco_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.telefone_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.email_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")

        style_button(button=self.salvar_botao, cor="azul", tam_fonte="12", border_radius=(5, 0, 5, 0), border_color="(123, 166, 205)")
        style_button(button=self.excluir_botao, cor="vermelho", tam_fonte="12", border_radius=(0, 5, 0, 5), border_color="(205, 123, 123)")


    def _setConnects(self):
        self.buscar_botao.clicked.connect(self.botaoBuscar)
        self.salvar_botao.clicked.connect(self.botaoSalvar)
        self.excluir_botao.clicked.connect(self.botaoExcluir)
        

    def clear(self, *widget_names):
        self.CNPJ_line.clear()
    

    def botaoBuscar(self):
        event = {"codigo": 10, "descricao": "Botão BUSCAR da tela GERENCIAR PEÇAS"}
        self.subject.notify(event)


    def botaoSalvar(self):
        event = {"codigo": 11, "descricao": "Botão SALVAR da tela GERENCIAR PEÇAS"}
        self.subject.notify(event)


    def botaoExcluir(self):
        event = {"codigo": 12, "descricao": "Botão EXCLUIR da tela GERENCIAR PEÇAS"}
        self.subject.notify(event)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaGerenciarFornecedores()
    app.show()
    sys.exit(root.exec_())
