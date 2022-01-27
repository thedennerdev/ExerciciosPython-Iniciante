#crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos Dólares ela pode comprar
#US1,00 = 5,19 Reais
real = float(input("Quanto tem em sua carteira digital? Digite:"))
dolar = real/5.19
euro = real /6.17
libra = real/7.20
iene = real / 0.047

print('Você possui R${:.2f} reais.'.format(real))
print('')
print('Irei realizar a conversão de algumas moeadas para você!')
print('Com sua quantia em dinheiro, voce pode comprar os seguintes valores:')
print('')
print('Em DOLAR US${:.2f} (Americano).'.format(dolar))
print('Em EURO EUR€{:.2f} (Europa).'.format(euro))
print('Em LIBRA £{:.2f} (Inglaterra).'.format(libra))
print('Em IENE ¥{:.2f} (Japão).'.format(iene))

