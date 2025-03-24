class Client:
    def __init__(self):
        self.__idclient = 0
        self.__name = ""
        self.__address = ""
        self.__city = ""
        self.__uf = ""
        self.__cep = ""
        self.__credit = 10000.00
        self.__balance = 0.0
        self.__table = "client"
        self.__attributes = "idclient, name, address, city, uf, cep, credit, balance"
        self.__pkey = "idclient"

    @property
    def dataInsert(self):
        data = (f"{self.idclient}, '{self.name}', "
                f"'{self.address}', '{self.city}', "
                f"'{self.uf}', '{self.cep}', "
                f"{self.credit}, {self.balance}")
        return data

    @property
    def dataUpdate(self):
        data = (f"idclient = {self.idclient}, "
                f"name = '{self.name}', "
                f"address = '{self.address}', "
                f"city = '{self.city}', "
                f"uf = '{self.uf}', "
                f"cep = '{self.cep}', "
                f"credit = {self.credit}, "
                f"balance = {self.balance}")
        return data

    @property
    def dataDelete(self):
        data = f"where idclient = {self.idclient}"
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
    def city(self):
        return self.__city
    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def uf(self):
        return self.__uf
    @uf.setter
    def uf(self, value):
        self.__uf = value

    @property
    def cep(self):
        return self.__cep
    @cep.setter
    def cep(self, value):
        self.__cep = value

    @property
    def credit(self):
        return self.__credit
    @credit.setter
    def credit(self, value):
        self.__credit = value

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, value):
        self.__balance = value

    @property
    def table(self):
        return self.__table
    @table.setter
    def table(self, value):
        self.__table = value

    @property
    def attributes(self):
        return self.__attributes
    @attributes.setter
    def attributes(self, value):
        self.__attributes = value

    @property
    def pkey(self):
        return self.__pkey
    @pkey.setter
    def pkey(self, value):
        self.__pkey = value

    def __repr__(self):
        return (f"Client(idclient={self.idclient}, "
                f"name='{self.name}', "
                f"address='{self.address}', "
                f"city='{self.city}', "
                f"uf='{self.uf}', "
                f"cep='{self.cep}', "
                f"credit={self.credit}, "
                f"balance={self.balance})")
