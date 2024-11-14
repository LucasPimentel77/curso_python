n = int(input('digite um numero: '))
soma = 0

while n<0:
    n = int(input('digite um numero positivo: '))

for i in range(0,n+1):
    soma+=i
print(f'a soma dos numeros de 0 a {i} é: {soma}')

soma = soma + i