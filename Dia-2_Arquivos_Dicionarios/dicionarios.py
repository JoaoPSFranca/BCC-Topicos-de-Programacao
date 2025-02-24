def cadastrar_aluno():
    aluno = {}
    aluno["nome"] = str(input("Nome do aluno: "))
    aluno["idade"] = int(input("Idade: "))
    aluno["curso"] = str(input("Curso: "))
    print("Aluno cadastrado com sucesso! ")
    return aluno

def pesquisar_aluno(alunos):
    nome = str(input("Informe o nome do aluno: "))

    for aluno in alunos:
        if nome.lower() == aluno["nome"].lower():
            return aluno

    return -1

def listar_alunos(alunos):
    i = 0
    for aluno in alunos:
        i += 1
        print(f"Aluno {i}: {aluno["nome"]}")

if (__name__ == "__main__"):
    verify = True
    alunos = []

    while verify:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar aluno ")
        print("2 - Pesquisar aluno ")
        print("3 - listar alunos ")
        print("0 - Sair do Programa")

        opcao = int(input("\nInforme a opção desejada: "))

        if(opcao == 1):
            alunos.append(cadastrar_aluno())
        elif (opcao == 2):
            aluno_procurado = pesquisar_aluno(alunos)
            if aluno_procurado == -1:
                print("Aluno não encontrado.")
            else:
                print(f"""Aluno {aluno_procurado['nome']} encontrado.
Nome: {aluno_procurado['nome']}
Idade: {aluno_procurado['idade']}
Curso: {aluno_procurado['curso']}""")
        elif (opcao == 3):
            listar_alunos(alunos)
        elif (opcao == 0):
            verify = False
        else:
            print("Opção não reconhecida.")