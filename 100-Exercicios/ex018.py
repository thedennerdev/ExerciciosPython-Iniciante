# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''import math
angulo = float(input('Informe o angulo desejado: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O valor do angulo {} possui o SENO {:.2f}'.format(angulo, sen))
print('O valor do angulo {} possui o COSSENO {:.2f}'.format(angulo,cos))
print('O valor de angulo {} possui a TANGENTE {:.2f}'.format(angulo, tan))'''


from math import radians, sin, cos, tan
angulo = float(input('Qual angulo desejado: '))
sen = sin(radians(angulo))
print('O angulo {} possui um SENO de {:.2f}'.format(angulo, sen))
cos = cos(radians(angulo))
print('O angulo {} possui um COSSENO de {:.2f}'.format(angulo, cos))
tan = tan(radians(angulo))
print('O angulo {} possui uma TANGENTE de {:.2}'.format(angulo, tan))

