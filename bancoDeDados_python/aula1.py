import sqlite3

con = sqlite3.connect('banco_sql_python.db')
banco = con.cursor()

resultado = banco.execute('SELECT nome, FROM Aluno')

alunos = resultado.fetchall()
for nome, nota_maior in alunos:
    print(f'{nome} - turma:{nota_maior}')