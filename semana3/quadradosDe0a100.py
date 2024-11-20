intervalo = int(input('defina o intervalo desejado: '))

for numero in range(0,intervalo+1):
    print(f'{numero} x {numero} = {numero**2}')