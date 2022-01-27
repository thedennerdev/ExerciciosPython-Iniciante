#Escreva um proegrama que leia um valor em metros e o exiba convertido em centimetros e milimetros
med = float(input('Escreva o valor em Metros à ser convertido:'))
print('A medida de {}m equivale à {:.4f}km'.format(med, med/1000))
print('A medida de {}m equivale à {:.3f}hm'.format(med, med/100))
print('A medida de {}m equivale à {:.2f}dam'.format(med, med/10))
print('A medida de {}m equivale à {:.0f}dm'.format(med, med*10))
print('A medida de {}m equivale à {:.0f}cm'.format(med, med*100))
print('A medida de {}m equivale à {:.0f}mm'.format(med, med*1000))
