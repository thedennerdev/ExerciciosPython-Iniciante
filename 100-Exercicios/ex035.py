#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-*'*18)
print('        Analisando triângulo')
print('-*'*18)
print('        Analisando')
r1 = float(input('Informe o primeiro número da reta: '))
r2 = float(input('Informe o segundo número da reta: '))
r3 = float(input('Informe o terceiro número da retas: '))

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r2 + r1):
    print('As retas informadas podem formar um triângulo.')
else:
    print('As retas informadas não podem formar um triângulo.')