'''
mostre a medias de nota_1 de cada turma
'''

import sqlite3

con = sqlite3.connect('banco_sql_python.db')
banco = con.cursor()

resultado = banco.execute('SELECT turma, AVG(nota_1), MAX(nota_1), MIN(nota_1) FROM Aluno GROUP BY turma')

turmas = resultado.fetchall()
print(     'turma | media | maior | menor ')
for turma, media, maior, menor in turmas:
    print(f'   {turma}  | {media:.2f}  | {maior}   | {menor}   ')