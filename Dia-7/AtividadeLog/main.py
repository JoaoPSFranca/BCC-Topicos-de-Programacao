class Controller:
    def __init__(self):
        self.lista_de_conexoes = []

    def add(self, id, hora, host, porta, usuario, database):
        co = Conexao()
        co.id = id
        co.hora = hora
        co.host = host
        co.porta = porta
        co.usuario = usuario
        co.database = database
        self.lista_de_conexoes.append(co)

    def listar(self):
        return self.lista_de_conexoes

    def filtrar(self, user):
        list_filter = []

        for co in self.lista_de_conexoes:
            if co.usuario == user:
                list_filter.append(co)

        return list_filter

    def resumo(self):
        dicio = {}

        for co in self.lista_de_conexoes:
            if co.host not in dicio.keys():
                dicio[co.host] = {
                    "host": co.host,
                    "qtde acessos": 0,
                    "usuarios": [co.usuario]
                }
            else:
                if co.usuario not in dicio[co.host]["usuarios"]:
                    dicio[co.host]["usuarios"].append(co.usuario)
                dicio[co.host]["qtde acessos"] += 1

        return dicio

class Conexao:
    def __init__(self):
        self.__id = ""
        self.__hora = ""
        self.__host = ""
        self.__porta = ""
        self.__usuario = ""
        self.__database = ""

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def hora(self):
        return self.__hora
    @hora.setter
    def hora(self, value):
        self.__hora = value

    @property
    def host(self):
        return self.__host
    @host.setter
    def host(self, value):
        self.__host = value

    @property
    def porta(self):
        return self.__porta
    @porta.setter
    def porta(self, value):
        self.__porta = value

    @property
    def usuario(self):
        return self.__usuario
    @usuario.setter
    def usuario(self, value):
        self.__usuario = value

    @property
    def database(self):
        return self.__database
    @database.setter
    def database(self, value):
        self.__database = value

    def __str__(self):
        return f"{self.__id} {self.__hora} {self.__usuario} {self.__database} {self.__host} {self.__porta}"

def ler_arquivo(arquivo, controller):
    with open(arquivo, 'r') as f:
        lines = f.readlines()

    id = 0
    for i in range(len(lines)):
        if "connection received:" in lines[i]:
            parts = lines[i].replace("  ", " ").split()
            hora = f"{parts[0]} {parts[1]}"
            host = parts[7].split("=")[1]
            porta = parts[8].split("=")[1]

            if "connection authenticated:" in lines[i + 1] and  "connection authorized:" in lines[i + 2]:
                auth_parts = lines[i + 2].replace("  ", " ").split()
                usuario = auth_parts[7].split("=")[1]
                database = auth_parts[8].split("=")[1]
                id += 1
                controller.add(id, hora, host, porta, usuario, database)

if __name__ == "__main__":
    controle = Controller()
    ler_arquivo("log3.log", controle)

    print("Listar conexoes: ")
    for x in controle.listar():
        print(x)

    print("\nFiltrar conexoes: ")
    for x in controle.filtrar("vfmaziero"):
        print(x)

    print("\nResumo das conexoes: ")
    for x in controle.resumo().items():
        print(x[1])
