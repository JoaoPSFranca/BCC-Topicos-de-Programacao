from Product import Product

class ItemSale:
    def __init__(self):
        self.product = Product()
        self.idsale = 0
        self.amount = 0
        self.price = 0
        self.table = "item_sale"
        self.attributes = "idproduct, idsale, amount, price"

    @property
    def dataInsert(self):
        data = f"{self.product.idproduct}, {self.idsale}, {self.amount}, {self.price}"
        return data

    @property
    def dataUpdate(self):
        data = (f"idproduct = {self.product.idproduct}, "
                f"idsale = {self.idsale}, "
                f"amount = {self.amount}, "
                f"price = {self.price}")
        return data

    @property
    def dataDelete(self):
        data = f"where idproduct = {self.product.idproduct} and idsale = {self.idsale}"
        return data

    @property
    def dataSearch(self):
        data = (f"select * from {self.table} where "
                f"idproduct = {self.product.idproduct} and "
                f"idsale = {self.idsale}")
        return data

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
    def idsale(self):
        return self.__idsale

    @idsale.setter
    def idsale(self, value):
        self.__idsale = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if value >= 0:
            self.__amount = value
        else:
            raise ValueError("Amount cannot be negative.")

    @property
    def price(self):
        return self.__product.price * self.__amount

    @price.setter
    def price(self, value):
        raise ValueError("Price is calculated automatically based on product price and amount.")

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

    def __repr__(self):
        return (f"ItemSale(idsale={self.idsale}, "
                f"product={self.product.name}, "
                f"amount={self.amount}, "
                f"price={self.price})")
