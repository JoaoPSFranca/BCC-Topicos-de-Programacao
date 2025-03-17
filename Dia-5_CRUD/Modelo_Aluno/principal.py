from controller.controleAluno import ControleAluno
from model.aluno import Aluno
from datetime import datetime

dao = ControleAluno()
aluno = Aluno()
lista = dao.listarTodos(aluno)

print('Lista dados')
for x in lista:
    aluno = dao.converteObjeto(x)
    print(aluno)

print('Incluindo aluno')
aluno.idaluno = 2
aluno.nome = 'joao'
aluno.endereco = 'rua 1'
aluno.cidade = 'belo horizonte'
aluno.uf = 'MG'
aluno.cep = '123456'
aluno.nascimento = '2025-03-11'
dao.incluir(aluno)

print('Alterando aluno')
aluno.endereco = 'RUA MIGUEL COUTINHO'
dao.alterar(aluno)

#aluno.idaluno = 8
#dao.deletarAluno(aluno)

print('Pesquisando aluno')
aluno = Aluno()
aluno.idaluno = 1
aluno = dao.pesquisaCodigo(aluno)
print(aluno)
print('Json')
print(dao.dadosJson(aluno))


