#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. 

print('~~'*18)
print('         CONVERSOR NÚMERICO')
print('~~'*18)
print('')
num = int(input('Digite o número para ser convertido: '))
print('')
print('''ESCOLHA UMA OPÇÃO
 [ 1 ]- BINÁRIO
 [ 2 ]- OCTAL
 [ 3 ]- HEXADECIMAL''')
opcao = int(input(' '))

if opcao == 1:
    print(f'O número {num} convertido em Binário equivale à {bin(num)[2:]}')
elif opcao == 2:
    print(f'O número {num} convertido em Octal equivale à {oct(num)[2:]}')
elif opcao == 3:
    print(f'O número {num} convertido em Hexadecimal equivale à {hex(num)[2:]}')
else:
    print('Opção Iválida!')
