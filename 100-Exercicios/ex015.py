#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

#Custo por dia
alu = int(input('Informe quantos dias foi alugado o veículo:'))
custo_vei = alu*60
print('Deverá ser pago R${:.2f} pelos {} dias de aluguel.'.format(custo_vei, alu))
print('')

#Custo por KM
km = float(input('Informe quantos Km foram percorridos: '))
custo_km = km*0.15

print('Deverá ser pago R${:.2f}, por um total de {}Km percorridos.'.format(custo_km, km))
print('')

#Valor total a ser pago
print('O total à ser pago dos valores de aluguel e Km percorridos, são R${:.2f}'.format(custo_km+custo_vei))
