despezas = 0.0
receita = 0.0
alimentacao = []
lazer = []
transporte = []
educacao = []

def adicionarReceita(valor):
    global receita
    receita += valor

def adicionarDespeza(valor):
    global despezas
    print('[1] - alimentação')
    print('[2] - lazer')
    print('[3] - transporte')
    print('[4] - educação')
    op = int(input('qual área vai ser a despeza? '))

    if valor > receita:
        print('saldo insuficiente para tal gasto!')
        return
    else:
        despezas += valor
        if op == 1:
            alimentacao.append(valor)
        elif op == 2:
            lazer.append(valor)
        elif op == 3:
            transporte.append(valor)
        elif op == 4:
            educacao.append(valor)

def gerarGrafico():
    if despezas == 0:
        print('Nenhuma despesa registrada para gerar gráficos.')
        return

    perAlimentacao = sum(alimentacao) / despezas * 100
    perLazer = sum(lazer) / despezas * 100
    perTransporte = sum(transporte) / despezas * 100
    perEducacao = sum(educacao) / despezas * 100

    print('-' * 50)
    print(f'\ngasto total: {despezas}\n')
    print(f'alimentação: {"=" * int(perAlimentacao)} {perAlimentacao:.2f}%')
    print(f'      lazer: {"=" * int(perLazer)} {perLazer:.2f}%')
    print(f'   educação: {"=" * int(perEducacao)} {perEducacao:.2f}%')
    print(f' transporte: {"=" * int(perTransporte)} {perTransporte:.2f}%')
    print('-' * 50)

while True:
    print('-' * 50)
    print('gestao')
    print('-' * 50)
    print(f'\nsaldo: {receita - despezas}\n')
    print('[1] - adicionar receita')
    print('[2] - adicionar despeza')
    print('[3] - gerar graficos de barras')
    print('[4] - sair')
    op = int(input('digite a opção desejada: '))

    if op == 1:
        valor = float(input('digite o valor da receita a adicionar: '))
        adicionarReceita(valor)
    
    elif op == 2:
        valor = float(input('digite o valor da despeza a adicionar: '))
        adicionarDespeza(valor)
    
    elif op == 3:
        gerarGrafico()
    
    elif op == 4:
        break
    
    else:
        print('operação invalida!!\n\n')
