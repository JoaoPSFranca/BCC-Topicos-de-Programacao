class Client:
    def __init__(self):
        self.__idclient = 0
        self.__name = ""
        self.__address = ""
        self.__table = "cliente"
        self.__attributes = "codcliente, nome, endereco"
        self.__pkey = "idclient"

    @property
    def dataInsert(self):
        data = (f"{self.idclient}, "
                f"'{self.name}', "
                f"'{self.address}'")
        return data

    @property
    def dataSearch(self):
        data = f"select * from {self.table} where idclient = {self.idclient}"
        return data

    @property
    def idclient(self):
        return self.__idclient
    @idclient.setter
    def idclient(self, value):
        self.__idclient = value

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def table(self):
        return self.__table

    @property
    def attributes(self):
        return self.__attributes

    @property
    def pkey(self):
        return self.__pkey