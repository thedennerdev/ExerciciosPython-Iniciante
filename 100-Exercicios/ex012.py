#faça um algoritimo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto
p = float(input('Qual o preço do produto? Digite: '))
print('Este produto com 5% de desconto tem o valor de R${:.2f}'.format(p - (p*5)/100))
