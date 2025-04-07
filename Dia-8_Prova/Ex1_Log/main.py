from controller.ControllerDefault import Controller
from model.Log import Log

def ler_arquivo(arquivo, controller):
    with open(arquivo, 'r') as f:
        lines = f.readlines()

    temp = []

    for i in range(len(lines)):
        if "connection received:" in lines[i]:
            parts = lines[i].replace("  ", " ").split()
            data = f"{parts[0]}"
            hora = parts[1].split(".")[0]
            id = int(parts[3].replace("[", "").replace("]", ""))
            host = parts[7].split("=")[1]
            porta = parts[8].split("=")[1]

            if "connection authenticated:" in lines[i + 1] and  "connection authorized:" in lines[i + 2] and id not in temp:
                auth_parts = lines[i + 2].replace("  ", " ").split()
                usuario = auth_parts[7].split("=")[1]
                database = auth_parts[8].split("=")[1]

                log = Log()
                log.idConexao = id
                log.data = data
                log.hora = hora
                log.usuario = usuario
                log.database = database
                log.host = host
                log.porta = porta

                controller.insert(log)
                temp.append(log.idConexao)
        if "disconnection: session time:" in lines[i]:
            parts = lines[i].replace("  ", " ").split()
            idConexao = int(parts[3].replace("[", "").replace("]", ""))
            tempo = parts[8].split(".")[0]
            controller.update("log", tempo, idConexao)

def gerar_arquivo(arquivo, logs):
    for log in logs:
        with open(arquivo, "a") as arq:
            arq.write(log.__str__() + "\n")

def resumo(logs):
    dicio = {}

    for log in logs:
        if log.host not in dicio.keys():
            dicio[log.host] = {
                "host": log.host,
                "qtde acessos": 0,
                "usuarios": [log.usuario]
            }
        else:
            if log.usuario not in dicio[log.host]["usuarios"]:
                dicio[log.host]["usuarios"].append(log.usuario)
            dicio[log.host]["qtde acessos"] += 1

    return dicio

def menu():
    print(f"""Menu:
1 - Ler Arquivo TXT
2 - Gravar no banco
3 - Listar 
4 - Gerar Arquivo Texto
5 - Gerar Resumo
6 - Sair
""")
    try:
        opt = input("Opção desejada: ")
        opt = int(opt)
        if opt > 6 or opt < 1:
            print("Opção inválida. Informe valores entre 1 e 6")
        else:
            return opt
    except KeyboardInterrupt:
        print("Era só ter digitado 6 cara. ")
    except Exception as e:
        print(f"Algo deu errado: {str(e)}")
    return -1

def opcoes(opt, arq):
    # Ler nome do arquivo
    if opt == 1:
        arq = input("Informe o nome do arquivo a ser lido: ")
        print()

    # Gravar dados do arquivo no banco
    elif opt == 2:
        control = Controller()
        ler_arquivo(arq, control)
        print()

    # Listar Registros na data escolhida
    elif opt == 3:
        control = Controller()
        date = input("Informe a data a ser pesquisada: ")
        logs = control.search(query=f"select * from log where dt = '{date}'")

        logs = [Log().convertToObject(x) for x in logs]

        for log in logs:
            print(log)

    # Gerar um arquivo texto com as informações do listar
    elif opt == 4:
        control = Controller()
        date = input("Informe a data a ser pesquisada: ")
        logs = control.search(query=f"select * from log where dt = '{date}'")
        logs = [Log().convertToObject(x) for x in logs]
        arquivo = input("Informe o nome do arquivo a ser gerado: ")
        gerar_arquivo(arquivo, logs)

    # Resumo do que aconteceu
    elif opt == 5:
        control = Controller()
        logs = control.search_all(Log())
        logs = [Log().convertToObject(x) for x in logs]
        res = resumo(logs)

        for re in res.items():
            print(f"Host: {re[1]['host']} usuarios: {re[1]['usuarios']} qtde_acesso: {re[1]['qtde acessos']}")

    return arq

if __name__ == '__main__':
    verify = True
    arq = ""

    while verify:
        op = menu()
        if op == 6:
            verify = False
        else:
            arq = opcoes(op, arq)
