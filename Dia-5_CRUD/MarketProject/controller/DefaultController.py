from Database import Database

class Controller:
    def __init__(self):
        self.db = Database()
        self.db.setting(ho="localhost",
                        db="escola",
                        us="root",
                        se="ifsp",
                        po=3306)

    def insert(self, object):
        self.db.openConnection()
        sql = f"insert into {object.table} "
        sql += f"({object.attibutes})"
        sql += f" values ({object.dataInsert})"

        try:
            self.db.execute(sql)
            self.db.save()
        except:
            print("Houve um erro")
            self.db.discard()