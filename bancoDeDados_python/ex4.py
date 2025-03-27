'''
atualizar a nota_1 de de um aluno
'''

import sqlite3

con = sqlite3.connect('banco_sql_python.db')
banco = con.cursor()

query = '''
    DELETE FROM Aluno WHERE id = :id
'''
params = {}
params['id'] = int(input('id: '))

banco.execute(query, params)
con.commit()