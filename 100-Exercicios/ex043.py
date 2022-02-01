#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

print('#'*18)
print('    CALCULO IMC')
print('#'*18)

peso = float(input('Informe seu peso em Kg: '))
altura = float(input('Informe sua altura em M: '))
imc = peso / (altura*altura)

if imc < 18.5:
    print(f'IMC de {imc:.1f}\nEstá ABAIXO DO PESO!')
elif imc > 18.5 and imc <= 25:
    print(f'IMC de {imc:.1f}\nEstá no PESO IDEAL')
elif imc > 25 and imc < 30:
    print(f'IMC de {imc:.1f}\nEstá com SOBREPESO')
elif imc > 30 and imc < 40:
    print(f'IMC de {imc:.1f}\nEstá com OBESIDADE')
else:
    print(f'IMC de {imc:.1f}\nEstá com OBESIDADE MÓRBIDA')