'''
Escreva um programa CRUD que faça as operações de:
    - CREATE(inserir um novo aluno)
    - READ( mostrar alunos )
    - UPDATE(atualizar registro de um aluno)
    - DELETE(remover um aluno pelo id)
'''
import sqlite3

con = sqlite3.connect('banco_sql_python.db')
banco = con.cursor()

def inserir():
    print('\nMENU INSERIR\n')
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
        query = '''INSERT INTO Aluno (nome, turma, nota_1, nota_2, nota_3, nota_4) 
                    VALUES
                    (?, ?, ?, ?, ?, ?)
                '''
        
        banco.execute(query, aluno)
        con.commit()
        
    print('valores adicionados no banco de dados')

def mostrar():
    print('\nMENU MOSTRAR\n')
    banco.execute('SELECT * FROM Aluno')

    alunos = banco.fetchall()

    for id, nome, turma, n1, n2, n3, n4 in alunos:
        tam = 20 - int(len(nome))
        vazio = ' '*tam
        print(f'ID {id} |{nome}{vazio} - turma {turma} | notas({n1}, {n2}, {n3}, {n4})')

def atualizar():
    print('\nMENU ATUALIZAR\n')
    params = {}
    params['id'] = input('id do aluno: ')
    params['nome'] = input('novo nome: ')
    params['turma'] = float(input('nova turma: '))
    query = '''
        UPDATE Aluno SET nome = :nome, turma = :turma WHERE id = :id
    '''
    banco.execute(query, params)
    con.commit()

def deletar():
    print('\nMENU DELETAR\n')
    query = '''
        DELETE FROM Aluno WHERE id = :id
    '''
    params = {}
    params['id'] = int(input('id do aluno: '))

    banco.execute(query, params)
    con.commit()

def menu():
    while True:
        print('-'*10)
        print('[1]- inserir')
        print('[2]- exibir ')
        print('[3]- atualizar')
        print('[4]- deletar')
        op = input('opção ->')
        print('-'*10)

        if op == '1':
            inserir()
        elif op == '2':
            mostrar()
        elif op == '3':
            atualizar()
        elif op == '4':
            deletar()
        else:
            print('digite uma opcao valida\n')

menu()