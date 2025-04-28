class Product:
    def __init__(self):
        self.__idproduct = 0
        self.__name = ""
        self.__price = 0.0
        self.__table = "produto"
        self.__attributes = "codproduto, nome, preco"
        self.__pkey = "idproduct"

    @property
    def dataInsert(self):
        data = (f"{self.idproduct}, "
                f"'{self.name}', "
                f"'{self.price}'")
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
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def table(self):
        return self.__table

    @property
    def attributes(self):
        return self.__attributes

    @property
    def pkey(self):
        return self.__pkey