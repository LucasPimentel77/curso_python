# https://dontpad.com/cyber120501
# 
# Complemente o exercício anterior, da seguinte forma:
# Implemente uma classe Registro com os seguintes atributos
#   - pessoas: lista de pessoas
#   - estudantes: lista de estudantes
#   - professores: lista de professores
#   - monitores: lista de monitores
#
# E com os seguintes métodos:
#   - registrar_pessoa()
#   - registrar_estudante()
#   - registrar_professor()
#   - registrar_monitor()
#
# Cada um desses métodos deve receber do usuário os dados necessários 
# para criação do objeto e então criar o objeto e adicioná-lo 
# em sua respectiva lista  

from pessoas import (
    Pessoa, 
    Estudante, 
    Monitor, 
    Professor
)

class Registro:
    pessoas = []
    estudantes = []
    professores = []
    monitores = []

    def registrar_pessoa(self):
        nome = input('Nome: ')
        cpf = input('CPF: ')
        nova_pessoa = Pessoa(nome, cpf)
        # Adiciona a pessoa na lista de pessoas
        self.pessoas.append(nova_pessoa)

        return (nome,cpf)

    def registrar_estudante(self):
        nome, cpf = self.registrar_pessoa()
        curso = input('Curso: ')
        semestre = input ('Semestre: ')

        novo_estudante = Estudante(nome, cpf, curso, semestre)
        self.estudantes.append(novo_estudante)

        return (nome, cpf, curso, semestre)

    def registrar_professor(self):
        nome, cpf = self.registrar_pessoa()
        graduacao = input('Graduação: ')
        materia = input ('Matéria: ')

        novo_professor = Professor(nome, cpf, graduacao, materia)
        self.professores.append(novo_professor)

    def registrar_monitor(self):
        nome, cpf, curso, semestre = self.registrar_estudante()
        bolsa = input('Bolsa: ')
        materia = input('Materia: ')

        novo_monitor = Monitor(nome, cpf, curso, semestre, materia, bolsa)
        self.monitores.append(novo_monitor)

    def listar(self, pessoas):
        for pessoa in pessoas:
            pessoa.detalhes()
    
    def listar_pessoa(self):
        self.listar(self.pessoas)

    def listar_estudante(self):
        self.listar(self.estudantes)

    def listar_professor(self):
        self.listar(self.professores)
    
    def listar_monitor(self):
        self.listar(self.monitores)