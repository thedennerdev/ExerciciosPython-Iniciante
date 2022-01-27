# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''import math
n1 = float(input('Digite um número real:'))
print('O numero interiro de {} é {}'.format(n1, math.trunc(n1)))'''

'''from math import trunc
n1 = float(input('Digite um valor:'))
print('O valor de número real {}, equivale à {} inteiro! '.format(n1, trunc(n1)))'''

n1 = float(input('Digite um valor:'))
print('O valor de número real {}, equivale à {} inteiro! '.format(n1, int(n1)))
