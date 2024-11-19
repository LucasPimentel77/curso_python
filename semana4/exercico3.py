def calculaImc(peso, altura):
    return peso/altura**2

def classeImc(imc):
    if(imc <= 19):
        print("abaixo do peso")
    elif(imc > 19 and imc <= 25):    
        print('peso normal')
    elif(imc > 25 and imc <= 30):
        print('acima do peso')
    elif(imc > 30 and imc <= 40):
        print('obesidade grau I')
    else:
        print('obesidade grau II')

peso = float(input('peso: '))
altura = float(input('altura: '))
imc = calculaImc(peso, altura)

print(f'seu imc é de: {imc}')
classeImc(imc)