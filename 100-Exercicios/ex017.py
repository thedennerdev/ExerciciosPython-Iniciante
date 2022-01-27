#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.

"""co = float(input('Valor cateto oposto: '))
ca = float(input('valor cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('O valor da hipotenusa é {:.2f}'.format(hi))"""

'''import math
co = float(input('Informe o valor Cateto Oposto: '))
ca = float(input('Informe o valor Cateto Adjacente: '))
hi = math.hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hi))'''

from math import hypot
co = float(input('Valor cateto oposto: '))
ca = float(input('Valor cateto adjacente: '))
hi = hypot(co, ca)
print('O valor da hipotenusa será {:.2f}'.format(hi))