from PyQt5.QtWidgets import QApplication, QMessageBox

import sys

from view.TelaCadastrarCliente import TelaCadastrarCliente
from view.TelaCadastrarFornecedor import TelaCadastrarFornecedor
from view.TelaCadastrarPeca import TelaCadastrarPeca
from view.StackTelas import StackTelas

from model.CreateDatabase import create_database
from model.SalvarPeca import SalvarPeca
from model.SalvarCliente import SalvarCliente
from model.SalvarFornecedor import SalvarFornecedor

# from model.AbrirTelaCriarFlashcards import AbrirTelaCriarFlashcards
# from model.AbrirTelaFlashcards import AbrirTelaFlashcards
# from model.VoltarParaTelaInicial import VoltarParaTelaInicial
# from model.CriarESalvarFlashcards import CriarESalvarFlashcards
# from model.DefinirDatasDosFlashcards import DefinirDatasDosFlashcards
# from model.AbrirTelaOpcoesRevisao import AbrirTelaOpcoesRevisao
# from model.AbrirTelaRevisao import AbrirTelaRevisao
# from model.ControleDaRevisaoFlashcards import ControleDaRevisaoFlashcards
# from model.DeletarFlashcard import DeletarFlashcard
# from model.AbrirTelaCriarRotina import AbrirTelaCriarRotina
# from model.CriarESalvarRotina import CriarESalvarRotina
# from model.AbrirTelaRotina import AbrirTelaRotina
# from model.SalvarEstadoDaAtividade import SalvarEstadoDaAtividade
# from model.AbrirTelaHistorico import AbrirTelaHistorico
# from model.AbrirTelaEditarHistorico import AbrirTelaEditarHistorico
# from model.VoltarTelaCriarFlashcards import VoltarTelaCriarFlashcards


def create_screens():
	telas = []

	telas.append(TelaCadastrarCliente()) # 0

	telas.append(TelaCadastrarFornecedor()) # 1

	telas.append(TelaCadastrarPeca()) # 2

	return telas


def create_observers(stack_telas):
	# voltar_para_tela_inicial = VoltarParaTelaInicial(stack_telas)
	# criar_e_salvar_flashcards = CriarESalvarFlashcards(stack_telas, QMessageBox)
	# abrir_tela_revisoes = AbrirTelaRevisoes(stack_telas)
	# controle_da_revisao_flashcards = ControleDaRevisaoFlashcards(stack_telas, abrir_tela_revisoes)
	# abrir_tela_historico = AbrirTelaHistorico(stack_telas)
	# abrir_tela_editar_historico = AbrirTelaEditarHistorico(stack_telas)
	# salvar_estado_da_atividade = SalvarEstadoDaAtividade(stack_telas, abrir_tela_editar_historico)

	stack_telas.screens[2].subject.subscribe(SalvarPeca(stack_telas))

	stack_telas.screens[0].subject.subscribe(SalvarCliente(stack_telas))

	stack_telas.screens[1].subject.subscribe(SalvarFornecedor(stack_telas))
	
	# stack_telas.screens[0].subject.subscribe(AbrirTelaCriarFlashcards(stack_telas))
	# stack_telas.screens[0].subject.subscribe(AbrirTelaFlashcards(stack_telas))
	# stack_telas.screens[0].subject.subscribe(AbrirTelaCriarRotina(stack_telas))
	# stack_telas.screens[0].subject.subscribe(AbrirTelaRotina(stack_telas))
	# stack_telas.screens[0].subject.subscribe(abrir_tela_historico)

	# stack_telas.screens[1].subject.subscribe(voltar_para_tela_inicial)
	# stack_telas.screens[2].subject.subscribe(voltar_para_tela_inicial)
	# stack_telas.screens[6].subject.subscribe(voltar_para_tela_inicial)

	# stack_telas.screens[0].subject.subscribe(criar_e_salvar_flashcards)
	# stack_telas.screens[2].subject.subscribe(criar_e_salvar_flashcards)
	# stack_telas.screens[5].subject.subscribe(criar_e_salvar_flashcards)

	# stack_telas.screens[2].subject.subscribe(DefinirDatasDosFlashcards(stack_telas, QMessageBox))

	# stack_telas.screens[1].subject.subscribe(AbrirTelaOpcoesRevisao(stack_telas))
	# stack_telas.screens[4].subject.subscribe(abrir_tela_revisoes)

	# stack_telas.screens[4].subject.subscribe(AbrirTelaRevisao(stack_telas))

	# stack_telas.screens[3].subject.subscribe(abrir_tela_revisoes)

	# stack_telas.screens[1].subject.subscribe(controle_da_revisao_flashcards)
	# stack_telas.screens[4].subject.subscribe(controle_da_revisao_flashcards)
	# stack_telas.screens[3].subject.subscribe(controle_da_revisao_flashcards)

	# stack_telas.screens[6].subject.subscribe(DeletarFlashcard(stack_telas, QMessageBox))

	# stack_telas.screens[7].subject.subscribe(voltar_para_tela_inicial)

	# stack_telas.screens[7].subject.subscribe(CriarESalvarRotina(stack_telas))

	# stack_telas.screens[8].subject.subscribe(voltar_para_tela_inicial)
	# stack_telas.screens[8].subject.subscribe(salvar_estado_da_atividade)

	# stack_telas.screens[9].subject.subscribe(voltar_para_tela_inicial)

	# stack_telas.screens[9].subject.subscribe(abrir_tela_editar_historico)
	# stack_telas.screens[10].subject.subscribe(abrir_tela_historico)
	# stack_telas.screens[10].subject.subscribe(salvar_estado_da_atividade)

	# stack_telas.screens[5].subject.subscribe(VoltarTelaCriarFlashcards(stack_telas))


if __name__ == '__main__':
	root = QApplication(sys.argv)


	create_database()
	stack_telas = StackTelas(create_screens())
	create_observers(stack_telas)

	stack_telas.open_screen(2)


	sys.exit(root.exec_())
