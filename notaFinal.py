nota1 = float(input('digite o nota 1: '))
nota2 = float(input('digite o nota 2: '))
nota3 = float(input('digite o nota 3: '))
peso1 = float(input('digite o peso 1: '))
peso2 = float(input('digite o peso 2: '))
peso3 = float(input('digite o peso 3: '))

notaFinal = (nota1*peso1+nota2*peso2+nota3*peso3)/(peso1+peso2+peso3)

print()

if notaFinal < 5.0:
    print('reprovado')
elif notaFinal >= 5 and notaFinal <=7:
    print('prova final')
else:
    print('aprovado')
print(f'porque a sua nota final foi {notaFinal}\n')