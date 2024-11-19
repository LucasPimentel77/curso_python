def calculaImc(peso, altura):
    return peso/altura**2

peso = float(input('peso: '))
altura = float(input('altura: '))
imc = calculaImc(peso, altura)

print(f'seu imc é de: {imc}')