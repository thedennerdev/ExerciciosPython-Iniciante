#Faça um programa que leia a largura e a altura de uma parede em metros
#calcule sua area e a quantidade de tinta necessária para pinta-la,
#sabendo que cada litro de tinta pinta uma area de 2m²
larg = float(input('Qual a largura do ambiente? Digite:'))
alt = float(input('Qual a altura do ambiente? Digite:'))
área = larg*alt
print('A dimensão da parece {}x{} é uma área equivalente à: {}m²'.format(larg, alt, área))
tinta = área / 2
print('Serão necessárias {}L de tinta para pintar o ambiente inteiro'.format(tinta))