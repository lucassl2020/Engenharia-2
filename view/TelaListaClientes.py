from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QListView, QTableWidgetItem
from PyQt5 import QtCore

import sys

from view.Widgets import button, label, textEdit, lineEdit, comboBox, table
from view.StyleButton import style_button

from model.Observer import ISubject


class TelaListaClientes(QWidget):
    def __init__(self, parent=None):
        super(TelaListaClientes, self).__init__(parent)

        self.subject = ISubject()
        
        self._settings()
        self._create_widgets()
        self._set_style()
        self._setConnects()


    def _settings(self):
        self.setFixedSize(600, 790)
        self.setWindowTitle("Clientes")
 

    def _create_widgets(self):
        self.realizar_venda_label = label(self, "Clientes", 0, 0, 600, 60)
        self.realizar_venda_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.realizar_venda_label.setAlignment(QtCore.Qt.AlignCenter)

        self.tabela = table(self, 9, 60, 582, 651)
        #Table will fit the screen horizontally
        self.tabela.horizontalHeader().setStretchLastSection(True)
        self.tabela.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tabela.horizontalHeader().setDefaultSectionSize(260)
        self.tabela.setColumnCount(5)  

        self.voltar_botao = button(self, "Voltar", 170, 730, 261, 41)


    def _set_style(self):
        self.setStyleSheet("background-color: rgb(235, 235, 235);")
        
        self.realizar_venda_label.setStyleSheet("font: 16pt;")

        style_button(button=self.voltar_botao, cor="cinza", tam_fonte="12", border_radius=(10, 10, 10, 10), rgb_da_letra="(36, 36, 36)")


    def _setConnects(self):
        self.voltar_botao.clicked.connect(self.botaoVoltar)


    def clear(self, *widget_names):
        self.tabela.clear()

    def adicionarItemTabela(self, linha, valores):
        self.tabela.setItem(linha, 0, QTableWidgetItem(str(valores[0])))
        self.tabela.setItem(linha, 1, QTableWidgetItem(str(valores[1])))
        self.tabela.setItem(linha, 2, QTableWidgetItem(str(valores[2])))
        self.tabela.setItem(linha, 3, QTableWidgetItem(str(valores[3])))
        self.tabela.setItem(linha, 4, QTableWidgetItem(str(valores[4])))

    def botaoVoltar(self):
        event = {"codigo": 32, "descricao": "Botão VOLTAR da tela LISTA CLIENTES"}
        self.subject.notify(event)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaListaClientes()
    app.show()
    sys.exit(root.exec_())
