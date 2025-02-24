class Controller:
    def __init__(self, caminho, Cliente=None, Produto=None, Venda=None, ItemVenda=None):
        self.Cliente = Cliente
        self.Produto = Produto
        self.Venda = Venda
        self.ItemVenda = ItemVenda
        self.caminho = caminho
    
    def save(self, texto):
        with open(f"./{self.caminho}.txt", "a") as arq:
            arq.write(texto)
            arq.close()