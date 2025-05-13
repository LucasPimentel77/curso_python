class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def detalhes(self):
        print(f'\nNome: {self.nome}')
        print(f'CPF: {self.cpf}')

class Estudante(Pessoa):
    def __init__(self, nome, cpf, curso, semestre):
        super().__init__(nome, cpf)
        # Pessoa.__init__(self, nome, cpf)
        self.curso = curso
        self.semestre = semestre
    
    def detalhes(self):
        super().detalhes()
        print(f'Curso: {self.curso}')
        print(f'Semestre: {self.semestre}')

class Professor(Pessoa):
    def __init__(self, nome, cpf, graduacao, materia):
        super().__init__(nome, cpf)
        self.graduacao = graduacao
        self.materia = materia 

    def detalhes(self):
        super().detalhes()
        print(f'Graduação: {self.graduacao}')
        print(f'Materia: {self.materia}')

class Monitor(Estudante):
    def __init__(self, nome, cpf, curso, semestre, materia, bolsa):
        super().__init__(nome, cpf, curso, semestre)
        self.materia = materia 
        self.bolsa = bolsa

    def detalhes(self):
        super().detalhes()
        print(f'Bolsa: {self.bolsa}')
        print(f'Materia: {self.materia}')
