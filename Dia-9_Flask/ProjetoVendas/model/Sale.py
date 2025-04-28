class Sale:
    def __init__(self):
        self.__idsale = 0
        self.__date = ""
        self.__total_value = 0.0
        self.__idclient = 0
        self.__table = "venda"
        self.__attributes = "codvenda, data, valor_total, codcliente"
        self.__pkey = "idsale"

    @property
    def dataInsert(self):
        data = (f"{self.idsale}, "
                f"'{self.date}',"
                f"{self.total_value}, "
                f"{self.idclient}")
        return data

    @property
    def dataSearch(self):
        data = f"select * from {self.table} where idsale = {self.idsale}"
        return data

    @property
    def idsale(self):
        return self.__idsale
    @idsale.setter
    def idsale(self, value):
        self.__idsale = value

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, value):
        self.__date = value

    @property
    def total_value(self):
        return self.__total_value
    @total_value.setter
    def total_value(self, value):
        self.__total_value = value

    @property
    def idclient(self):
        return self.__idclient
    @idclient.setter
    def idclient(self, value):
        self.__idclient = value

    @property
    def table(self):
        return self.__table

    @property
    def attributes(self):
        return self.__attributes

    @property
    def pkey(self):
        return self.__pkey