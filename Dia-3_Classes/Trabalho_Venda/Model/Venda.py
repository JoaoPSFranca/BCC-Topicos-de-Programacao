from Cliente import Cliente
from Produto import Produto

class Venda:
    def __init__(self):
        self.codvenda = 0
        self.data = ""
        self.valor_total = 0.0
        self.codcliente = 0
        self.itens = []

