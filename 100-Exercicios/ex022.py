#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

#Input do nome
nome = str(input('Informe seu nome completo: ')).strip()
pNome = nome.split()

#Saudações
print(f'Prazer em conhecer {pNome [0]}! Adorei se como se chama!')
print('Analizando seu nome...')

#Mostra resultado nome com maisúsculas
print(f'Seu nome maiúsculas é: {nome.upper()}')

#Mostra resultado nome com miúsculas
print(f'Seu nome maiúsculas é: {nome.lower()}')

#Mostra quant letras ao todo sem espaço
qntLetras = len(nome.replace(' ', ''))
print(f'Seu nome completo possui {qntLetras} letras.')

#Mostra quant letras primeiro nome
print(f'Seu primeiro nome possui {len(pNome[0])} letras.')
#print('Seu primeiro nome possui {} letras'.format(len(pNome[0])))




