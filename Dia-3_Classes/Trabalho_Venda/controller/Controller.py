from model.Cliente import Cliente
from model.Produto import Produto
from model.Venda import Venda
from model.ItemVenda import ItemVenda

class Controller:
    def __init__(self, caminho, Cliente=None, Produto=None, Venda=None, ItemVenda=None):
        self.Cliente = Cliente
        self.Produto = Produto
        self.Venda = Venda
        self.ItemVenda = ItemVenda
        self.caminho = caminho
    
    def save(self, texto):
        with open(f"./bd/{self.caminho}.txt", "a") as arq:
            arq.write(texto)
            arq.close()

    def entityConverter(self, list):
        if self.caminho == "clientes":
            return Cliente(int(list[0]), list[1], list[2])
        elif self.caminho == "produtos":
            return Produto(int(list[0]), list[1], float(list[2]))
        elif self.caminho == "vendas":
            itens = []
            itensVenda = list[4].split(" / ")
            for item in itensVenda:
                item = item.split(" \ ")
                iv = ItemVenda(item[0], item[1], item[2], item[3])
                itens.append(iv)
            return Venda(int(list[0]), list[1], float(list[2]), int(list[3]), itens)

    def list_all(self):
        list = []
        try:
            with open(f"./bd/{self.caminho}.txt", "r") as arq:
                for i in arq.read().split("\n"):
                    if i:
                        entity = self.entityConverter(i.split(" | "))
                        list.append(entity)
                arq.close()
            return list
        except:
            print(f"Não há {self.caminho} cadastrados (as). ")
            return -1

    def max_code(self):
        try:
            with open(f"./bd/{self.caminho}.txt", "r") as arq:
                all = arq.read().split("\n")
                max = all[len(all) - 2].split(" | ")[0]
                arq.close()
            return int(max)
        except:
            return 0

    def list_vendas_cliente(self, code):
        list = []
        try:
            with open(f"./bd/{self.caminho}.txt", "r") as arq:
                for i in arq.read().split("\n"):
                    if i:
                        i = i.split(" | ")
                        if i[3] == code:
                            entity = self.entityConverter(i)
                            list.append(entity)
                arq.close()
            return list
        except:
            print(f"Não há {self.caminho} cadastradas. ")
        return -1

    def venda_cliente(self, codigo, numero_venda):
        entity = None
        try:
            with open(f"./bd/{self.caminho}.txt", "r") as arq:
                count = 0
                for i in arq.read().split("\n"):
                    if i:
                        i = i.split(" | ")
                        if i[3] == codigo:
                            count += 1
                            if count == numero_venda:
                                entity = self.entityConverter(i)
                                break
                arq.close()
            return entity
        except:
            print(f"Não há {self.caminho} cadastrados (as). ")
            return -1

    def get_entity(self, codigo):
        entity = None
        try:
            with open(f"./bd/{self.caminho}.txt", "r") as arq:
                for i in arq.read().split("\n"):
                    if i:
                        i = i.split(" | ")
                        if int(i[0]) == codigo:
                            entity = self.entityConverter(i)
                            break
                arq.close()
            return entity
        except:
            print(f"Não há {self.caminho} cadastrados (as). ")
            return None
