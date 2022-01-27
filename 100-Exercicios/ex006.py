#crie um agoritimo que leia um numero e mostre o seu dobro, seu triplo e sua raiz quadrada
n = int(input('Digite um número:'))
print('O dobro de {} é {}'.format(n, (n*2)))
print('O triplo de {} é {}'.format(n, (n*3)))
print('O quadriplo de {} é {}'.format(n, (n*4)))
print('O 5x de {} é {}'.format(n, (n*5)))
print('A raiz quadrada de {} é {:.2f}'.format(n, (n**(1/2))))