from model.Product import Product

class SaleItem:
    def __init__(self):
        self.__idsale = 0
        self.__product = Product()
        self.__quantity = 0
        self.__value = 0.0
        self.__table = "item_venda"
        self.__attributes = "codvenda, codproduto, qtde, valor"
        self.__pkey = "idsale, idproduct"

    @property
    def dataInsert(self):
        data = (f"{self.idsale}, "
                f"{self.product}, "
                f"{self.quantity}, "
                f"{self.value}")
        return data

    @property
    def dataSearch(self):
        data = f"select * from {self.table} where idsale = {self.idsale} and idproduct = {self.product.idproduct}"
        return data

    @property
    def idsale(self):
        return self.__idsale
    @idsale.setter
    def idsale(self, value):
        self.__idsale = value

    @property
    def product(self):
        return self.__product
    @product.setter
    def product(self, value: Product):
        if isinstance(value, Product):
            self.__product = value
        else:
            raise ValueError("Product must be an instance of Product class.")

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def table(self):
        return self.__table

    @property
    def attributes(self):
        return self.__attributes

    @property
    def pkey(self):
        return self.__pkey