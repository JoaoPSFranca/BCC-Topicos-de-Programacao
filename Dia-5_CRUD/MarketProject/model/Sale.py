import datetime
from model.Client import Client
from model.ItemSale import ItemSale

class Sale:
    def __init__(self):
        self.__idsale = 0
        self.__date = ""
        self.__client = Client()
        self.__total = 0.0
        self.__items = []
        self.__table = "sale"
        self.__attributes = "idsale, date, idclient, total"
        self.__pkey = "idsale"

    def add_item(self, item: ItemSale):
        if isinstance(item, ItemSale):
            self.__items.append(item)
        else:
            raise ValueError("Item must be an instance of ItemSale.")

    def remove_item(self, item: ItemSale):
        if item in self.__items:
            self.__items.remove(item)
        else:
            raise ValueError("Item not found in the sale.")

    @property
    def dataInsert(self):
        data = (f"{self.idsale}, '{self.date}', "
                f"{self.client.idclient}, {self.total}")
        return data

    @property
    def dataUpdate(self):
        data = (f"idsale = {self.idsale}, "
                f"date = '{self.date}', "
                f"idclient = {self.client.idclient}, "
                f"total = {self.total}")
        return data

    @property
    def dataDelete(self):
        data = f"where idsale = {self.idsale}"
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
    def client(self):
        return self.__client
    @client.setter
    def client(self, value):
        self.__client = value

    @property
    def total(self):
        self.__total = sum(item.price for item in self.__items)
        return self.__total
    @total.setter
    def total(self, value):
        raise ValueError("Total is calculated automatically based on product price and amount.")

    @property
    def items(self):
        return self.__items
    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self.__items = value
        else:
            raise ValueError("Items must be a list of ItemSale objects.")

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

    def date_str(self, data):
        if isinstance(data, datetime.date):
            return data.strftime("%d/%m/%Y")
        return str(data)
