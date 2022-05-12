from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QListView
from PyQt5 import QtCore

import sys

from view.Widgets import button, label, textEdit, lineEdit, comboBox
from view.StyleButton import style_button

from model.Observer import ISubject


class TelaGerenciarPecas(QWidget):
    def __init__(self, parent=None):
        super(TelaGerenciarPecas, self).__init__(parent)

        self.subject = ISubject()
        
        self._settings()
        self._create_widgets()
        self._set_style()
        self._setConnects()


    def _settings(self):
        self.setFixedSize(600, 800)
        self.setWindowTitle("Gerenciar peças")
 

    def _create_widgets(self):
        self.gerenciar_label = label(self, "Gerenciar peças", 0, 0, 600, 60)
        self.gerenciar_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gerenciar_label.setAlignment(QtCore.Qt.AlignCenter)

        self.codigo_line = lineEdit(self, 170, 100, 261, 41)
        self.codigo_label = label(self, "Codigo da peça", 0, 80, 600, 20)
        self.codigo_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.buscar_botao = button(self, "Buscar", 170, 150, 261, 41)

        self.resultado_label = label(self, "Resultado", 0, 200, 600, 60)
        self.resultado_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.resultado_label.setAlignment(QtCore.Qt.AlignCenter)


        self.nome_line = lineEdit(self, 170, 300, 261, 41)
        self.nome_label = label(self, "Nome", 0, 280, 600, 20)
        self.nome_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.codigo_resultado_line = lineEdit(self, 170, 380, 261, 41)
        self.codigo_resultado_line.setEnabled(False)
        self.codigo_resultado_label = label(self, "Codigo", 0, 360, 600, 20)
        self.codigo_resultado_label.setAlignment(QtCore.Qt.AlignCenter)

        self.valor_custo_line = lineEdit(self, 170, 460, 261, 41)
        self.valor_custo_label = label(self, "Valor de custo", 0, 440, 600, 20)
        self.valor_custo_label.setAlignment(QtCore.Qt.AlignCenter)

        self.valor_venda_line = lineEdit(self, 170, 540, 261, 41)
        self.valor_venda_label = label(self, "Valor de venda", 0, 520, 600, 20)
        self.valor_venda_label.setAlignment(QtCore.Qt.AlignCenter)

        self.codigo_fornecedor_line = lineEdit(self, 170, 620, 261, 41)
        self.codigo_fornecedor_label = label(self, "Codigo do fornecedor", 0, 600, 600, 20)
        self.codigo_fornecedor_label.setAlignment(QtCore.Qt.AlignCenter)

        self.salvar_botao = button(self, "Salvar", 170, 680, 130, 41)
        self.excluir_botao = button(self, "Excluir", 300, 680, 130, 41)
        self.voltar_botao = button(self, "Voltar", 170, 740, 261, 41)


    def _set_style(self):
        self.setStyleSheet("background-color: rgb(235, 235, 235);")

        self.gerenciar_label.setStyleSheet("font: 16pt;")
        self.codigo_label.setStyleSheet("font: 12pt;")
        self.resultado_label.setStyleSheet("font: 16pt;")

        self.codigo_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")

        style_button(button=self.buscar_botao, cor="cinza_escuro", tam_fonte="12", border_radius=(10, 10, 10, 10), rgb_da_letra="(210, 210, 210)")

        self.nome_label.setStyleSheet("font: 12pt;")
        self.codigo_resultado_label.setStyleSheet("font: 12pt;")
        self.valor_custo_label.setStyleSheet("font: 12pt;")
        self.valor_venda_label.setStyleSheet("font: 12pt;")
        self.codigo_fornecedor_label.setStyleSheet("font: 12pt;")

        self.nome_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.codigo_resultado_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.valor_custo_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.valor_venda_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")
        self.codigo_fornecedor_line.setStyleSheet("font: 11pt; border: 1px solid; border-radius: 4px; border-color: rgb(84, 84, 84);")

        style_button(button=self.salvar_botao, cor="azul", tam_fonte="12", border_radius=(5, 0, 5, 0), border_color="(123, 166, 205)")
        style_button(button=self.excluir_botao, cor="vermelho", tam_fonte="12", border_radius=(0, 5, 0, 5), border_color="(205, 123, 123)")
        style_button(button=self.voltar_botao, cor="cinza", tam_fonte="12", border_radius=(10, 10, 10, 10), rgb_da_letra="(36, 36, 36)")


    def _setConnects(self):
        self.buscar_botao.clicked.connect(self.botaoBuscar)
        self.salvar_botao.clicked.connect(self.botaoSalvar)
        self.excluir_botao.clicked.connect(self.botaoExcluir)
        self.voltar_botao.clicked.connect(self.botaoVoltar)
        

    def clear(self, *widget_names):
        self.codigo_line.clear()
        self.nome_line.clear()
        self.codigo_resultado_line.clear()
        self.valor_custo_line.clear()
        self.valor_venda_line.clear()
        self.codigo_fornecedor_line.clear()
    

    def botaoBuscar(self):
        event = {"codigo": 4, "descricao": "Botão BUSCAR da tela GERENCIAR PEÇAS"}
        self.subject.notify(event)


    def botaoSalvar(self):
        event = {"codigo": 5, "descricao": "Botão SALVAR da tela GERENCIAR PEÇAS"}
        self.subject.notify(event)


    def botaoExcluir(self):
        event = {"codigo": 6, "descricao": "Botão EXCLUIR da tela GERENCIAR PEÇAS"}
        self.subject.notify(event)

    def botaoVoltar(self):
        event = {"codigo": 29, "descricao": "Botão VOLTAR da tela CADASTRAR PEÇAS"}
        self.subject.notify(event)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaGerenciarPecas()
    app.show()
    sys.exit(root.exec_())
