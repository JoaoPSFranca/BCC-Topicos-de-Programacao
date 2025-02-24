class Controller:
    def __init__(self, aluno=None):
        self.aluno = aluno

    def save(self):
        with open("./teste.txt", "a") as arq:
            arq.write(self.aluno.prontuario + " | " + self.aluno.nome + " | " + self.aluno.curso  + " | " + self.aluno.telefone + "\n")
            arq.close()

    def list_alunos(self):
        list = []
        with open("./teste.txt", "r") as arq:
            for i in arq.read().split("\n"):
                list.append(i.split(" | "))
            arq.close()
        return list

    def delete_aluno(self, pront):
        arq = open("./teste.txt", "r")
        lines = arq.readlines()
        arq.close()

        for line in lines[:]:
            if pront == (line.split(" | ")[0]):
                lines.remove(line)

        arq = open("./teste.txt", "w")
        arq.writelines(lines)
        arq.close()