class Log:
    def __init__(self):
        self.__idConexao = 0
        self.__data = ""
        self.__hora = ""
        self.__usuario = ""
        self.__database = ""
        self.__host = ""
        self.__porta = ""
        self.__tempo = "00:00:00"

        self.__attributes= "id,dt,hora,usuario,db,hs,porta,tempo"
        self.__table = "log"
        self.__pkey = "id"

    def convertToObject(self, tuple):
        self.idConexao = tuple[0]
        self.data = tuple[1]
        self.hora = tuple[2]
        self.usuario = tuple[3]
        self.database = tuple[4]
        self.host = tuple[5]
        self.porta = tuple[6]
        self.tempo = tuple[7]
        return self

    @property
    def attributes(self):
        return self.__attributes

    @property
    def dataInsert(self):
        data = (f"{self.idConexao},'{self.data}','{self.hora}','{self.usuario}',"
                f"'{self.database}','{self.host}','{self.porta}', "
                f"'{self.tempo}'")
        return data

    def dataUpdate(self):
        return f"tempo = '{self.tempo}'"

    @property
    def dataSearch(self):
        data = f"select * from {self.table} where id={self.idConexao}"
        return data

    @property
    def dataSearchDate(self):
        data = f"select * from {self.table} where dt={self.data}"
        return data

    @property
    def table(self):
        return self.__table

    @property
    def idConexao(self):
        return self.__idConexao
    @idConexao.setter
    def idConexao(self, value):
        self.__idConexao = value

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def hora(self):
        return self.__hora
    @hora.setter
    def hora(self, value):
        self.__hora = value

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
    def tempo(self):
        return self.__tempo
    @tempo.setter
    def tempo(self, value):
        self.__tempo = value

    def __str__(self):
        return (f"{self.idConexao} {self.data} {self.hora} {self.usuario} "
                f"{self.database} {self.host} {self.porta} {self.tempo}")