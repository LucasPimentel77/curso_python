'''
atualizar a nota_1 de de um aluno
'''

import sqlite3

con = sqlite3.connect('banco_sql_python.db')
banco = con.cursor()

query = '''
    UPDATE Aluno SET nota_1 = :nova_nota WHERE nome = :nome
'''
params = {}
params['nome'] = input('nome: ')
params['nova_nota'] = float(input('nova nota: '))

banco.execute(query, params)
con.commit()