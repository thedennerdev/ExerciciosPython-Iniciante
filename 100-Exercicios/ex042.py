#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes 

a = int(input('Informe a primeira reta: '))
b = int(input('Informe a segunda reta: '))
c = int(input('Informe a terceira reta: '))

if  a < b + c and b < a + c and c < a + b:
        if a == b and a == c:
            print('Forma um triangulo EQUILÁTERO')
        elif a == b or a == c or b == c:
            print('Forma um triangulo ISÓSCELES')
        else:
            print('Forma um triangulo ESCALENO')
else:
    print(' não pode formar um triângulo')