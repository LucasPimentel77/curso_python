def contar_vogais(texto):
    vogais = {'a','e','i','o','u'}
    for i in range(len(texto)):
        if (texto[i] in vogais):
            print(f'vogal {texto[i]}')

contar_vogais("hello word")