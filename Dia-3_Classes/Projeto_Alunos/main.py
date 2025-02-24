from controller import Controller

class Aluno:
    def __init__(self):
        self.prontuario = ''
        self.nome = ''
        self.curso = ''
        self.telefone = ''

    def atrubuir(self):
        self.prontuario = input("Prontuario: ")
        self.nome = input("Nome do aluno: ")
        self.curso = input("Curso: ")
        self.telefone = input("Telefone: ")

def cadastrar():
    aluno = Aluno()
    aluno.atrubuir()
    controll = Controller(aluno)
    controll.save()

def listar():
    control = Controller()
    lista = control.list_alunos()
    print("\nLista de Alunos:")
    for i in range(len(lista) - 1):
        print(f"Prontuario: {lista[i][0]}")
        print(f"Aluno: {lista[i][1]}")
        print(f"Curso: {lista[i][2]}")
        print(f"Telefone: {lista[i][3]}\n")

def pesquisar(pront):
    controll = Controller()
    lista = controll.list_alunos()
    pos = -1
    for i in range(len(lista) - 1):
        if pront == lista[i][0]:
            pos = i
            break
    if pos == -1:
        print("\nAluno não encontrado. ")
    else:
        print(f"\nAluno {pront} encontrado! ")
        print(f"Prontuario: {lista[pos][0]}")
        print(f"Nome completo: {lista[pos][1]}")
        print(f"Curso: {lista[pos][2]}")
        print(f"Telefone: {lista[pos][3]}\n")

def excluir(pront):
    control = Controller()
    control.delete_aluno(pront)

def menu():
    verify = True

    while verify:
        print(f"""Menu:
1 - Cadastrar aluno
2 - Listar alunos
3 - Pesquisar aluno
4 - Excluir aluno
0 - Sair
""")
        try:
            opt = input("Opção desejada: ")
            opt = int(opt)

            if opt == 0:
                verify = False
            elif opt == 1:
                cadastrar()
                print("Aluno cadastrado com sucesso! ")
            elif opt == 2:
                listar()
            elif opt == 3:
                pront = input("Informe o prontuario a ser pesquisado: ")
                pesquisar(pront)
            elif opt == 4:
                pront = input("Informe o prontuario a ser excluido: ")
                excluir(pront)
        except KeyboardInterrupt:
            print("Era só ter digitado 0 cara. ")
        except Exception as e:
            print(f"Algo deu errado: {str(e)}")

if __name__ == "__main__":
    menu()
