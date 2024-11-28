def contarPalavras(texto):
    cont = 0
    for i in range(len(texto)):
        if texto[i] == ' ' and texto[i-1] != ' ':
            cont+=1
    cont+=1
    print(f'esse texto possui {cont} palavras')

contarPalavras('oi meu amor')