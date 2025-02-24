class Manipula_String:
    def __init__(self):
        self.texto = ""

    def inverter(self):
        return self.texto[-1:]

    def primeira_palavra(self):
        return self.texto.split()[0]

    def maiusculo(self):
        return self.texto.upper()

    def minusculo(self):
        return self.texto.lower()

    def atribuir(self, texto2):
        self.texto = texto2

if __name__ == '__main__':
    manipular = Manipula_String()
    manipular.atribuir("testando teste")
    print(f"""Inverter: {manipular.inverter()}
Primeira palavra: {manipular.primeira_palavra()}
Maiusculo: {manipular.maiusculo()}
Minusculo: {manipular.minusculo()} """)
