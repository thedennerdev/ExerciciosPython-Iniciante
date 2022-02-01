#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

print('======= LOJAS ESTE & DD =======')
compras = float(input('Informe o valor total das compras: '))
print('')
print('''Escolha a opção de pagamento: 
      [ 1 ] À vista dinheiro
      [ 2 ] À vista no cartão
      [ 3 ] Em até 2x no cartão
      [ 4 ] Em 3x ou mais no cartão''')
opcao = int(input('Digite aqui: '))
print('')

if opcao == 1:
    desc10 = (compras * 10) / 100
    print('======= RESULTADO =======')
    print(f'Suas compras de R${compras:.0f} tem um desconto de R${desc10:.2f}')
    print(f'O valor final à ser pago é de R${compras - desc10:.2f}.')
elif opcao == 2:
    desc5 = (compras * 5) / 100
    print('======= RESULTADO =======')
    print(f'Suas compras de R${compras:.0f} tem um desconto de R${desc5:.2f}')
    print(f'O valor final à ser pago é de R${compras - desc5:.2f}.')
elif opcao == 3:
    parcela = compras / 2
    print('======= RESULTADO =======')
    print(f'Suas compras de R${compras:.0f} foram parceladas em 2x de R${parcela:.2f}')
    print(f'O valor final à ser pago é de R${compras:.2f}.')
else:
    qnt_parc = int(input('Deseja parcelar em quantas vezes: '))
    juros = (compras * 20) / 100
    parc_final = (compras + juros) / qnt_parc
    print('======= RESULTADO =======')
    print(f'Suas compras de R${compras:.0f} foram parceladas em {qnt_parc}x, É acrescentado juros de 20% no valor de R${juros:.2f}')
    print(f'O valor final à ser pago é de R${compras + juros:.2f}. Cada parcela tem o valor de R${parc_final:.2f}.')
print('\nBOAS COMPRAS!')