#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('<>'*18)
print('       Minha casa Minha vida')
print('<>'*18)
print('')

valor_casa = float(input('Valor da casa: R$'))
salário = float(input('Valor salário: R$'))
anos = int(input('Parcelado em quantos anos: '))
meses = anos * 12
parcela_mensal = valor_casa/meses

if parcela_mensal > salário * 0.3:
    print(f' A parcela mensal será: R${parcela_mensal:.2f}! Emprestimo NEGADO!')
else:
    print(f' A parcela mensal será: R${parcela_mensal:.2f}! Emprestimo OK!')

