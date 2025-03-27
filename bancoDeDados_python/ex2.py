'''
inserir alunos no banco de dados
'''

import sqlite3

con = sqlite3.connect('banco_sql_python.db')
banco = con.cursor()

while True:
    nome = input('nome: ')

    if nome == '':
        break

    turma = input('turma: ')
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    nota3 = float(input('nota 3: '))
    nota4 = float(input('nota 4: '))

    aluno = (nome, turma, nota1, nota2, nota3, nota4)

    banco.execute('''INSERT INTO Aluno (nome, turma, nota_1, nota_2, nota_3, nota_4) 
                VALUES
                (?, ?, ?, ?, ?, ?)
                ''', aluno)
    
print('valores adicionados no banco de dados')

con.commit()