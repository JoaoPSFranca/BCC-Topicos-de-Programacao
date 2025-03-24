class Product:
    def __init__(self):
        self.__idproduct = 0
        self.__name = ""
        self.__amount = 0
        self.__price = 0.0
        self.__table = "product"
        self.__attributes = "idproduct, name, amount, price"
        self.__pkey = "idproduct"

    @property
    def dataInsert(self):
        data = (f"{self.idproduct}, '{self.name}', "
                f"{self.amount}, {self.price}")
        return data

    @property
    def dataUpdate(self):
        data = (f"idproduct = {self.idproduct}, "
                f"name = '{self.name}', "
                f"amount = {self.amount}, "
                f"price = {self.price}")
        return data

    @property
    def dataDelete(self):
        data = f"where idproduct = {self.idproduct}"
        return data

    @property
    def dataSearch(self):
        data = f"select * from {self.table} where idproduct = {self.idproduct}"
        return data

    @property
    def idproduct(self):
        return self.__idproduct

    @idproduct.setter
    def idproduct(self, value):
        self.__idproduct = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

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
        return (f"Product(idproduct={self.idproduct}, "
                f"name='{self.name}', "
                f"amount={self.amount}, "
                f"price={self.price})")
