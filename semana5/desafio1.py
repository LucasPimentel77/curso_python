tarefas = []

def adicionarTarefa(tarefa, urgencia):
    if urgencia == 1:
        tarefas.insert(0,tarefa)
        print(f'{tarefa} adicionada em urgencia com sucesso!\n')

    if urgencia == 2:
        tarefas.append(tarefa)
        print(f'{tarefa} adicionada com sucesso!\n')


def listarTarefas():
    print('-'*50)
    if len(tarefas) == 0:
        print('lista vazia')
    else:
        c = 1
        for tarefa in tarefas:
            print(f'{c}- {tarefa}')
            c+=1
    print('-'*50)

def concluirTarefa(numero):
    if numero <= len(tarefas):
        concluida = tarefas.pop(numero-1)
        print(f'{concluida} concluido com sucesso')


while True:
    print('[1] - adicionar tarefa')
    print('[2] - listar tarefas')
    print('[3] - concluir tarefas')
    print('[s] - sair')
    op = input('digite uma opção: ')
    if op == '1':
        tarefa = input('qual tarefa deseja adicionar: ')
        urgencia = int(input('ela é urgente? [1]sim [2]não: '))

        adicionarTarefa(tarefa, urgencia)
    
    elif op == '2':
        listarTarefas()

    elif op == '3':
        concluir = input('digite a tarefa a ser concluida: ')
        concluirTarefa(concluir)
    
    elif op == 's' or op == 'S':
        break