import sqlite3

con = sqlite3.connect('banco_sql_python.db')
banco = con.cursor()


banco.execute('SELECT nome, MAX(nota_1) FROM Aluno')
alunos = banco.fetchall()


for nome, nota_maior in alunos:
    print(f'{nome} - turma:{nota_maior}')