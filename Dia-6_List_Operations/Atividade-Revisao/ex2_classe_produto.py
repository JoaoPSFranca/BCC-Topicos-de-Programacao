"""
2 - Implemente uma classe Produto com os atributos: nome, preco e estoque. A classe deve:
    • Ter um metodo __str__ para retornar a string: "Produto: <nome>, R$<preco>, Estoque: <estoque>".
    • Ter um metodo vender(qtd) que diminui o estoque e retorna o valor total da venda.
    • Proibir a venda se o estoque for insuficiente
"""

class Produto:
    def __init__(self):
        self.nome = ""
        self.preco = 0.0
        self.estoque = 0

    def vender(self, qtd):
        if self.estoque >= qtd:
            self.estoque -= qtd
            return qtd * self.preco
        else:
            return "Não tem estoque dog"

    def __str__(self):
        return f"Produto: {self.nome}, R${self.preco}, Estoque: {self.estoque}"