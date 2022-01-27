#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
c = int(input('Informe o terceiro número: '))
print()
#Verificando menor número
if a > b and c:
    print(f'{a} é o maior numero entre {b} e {c}')
elif c > b and a:
    print(f'{c} é o maior número entre {b} e {a}')
else:
    print(f'{b} é o maior número entre {a} e {c}')
#Verificando menor número
if a < b and c:
    print(f'{a} é o menor numero entre {b} e {c}')
elif c < b and a:
    print(f'{c} é o menor número entre {b} e {a}')
else:
    print(f'{b} é o menor número entre {a} e {c}')