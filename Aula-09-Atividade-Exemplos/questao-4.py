"""Faça um programa que receba um número e que calcule e mostre a tabuada desse número."""

num = int(input('Digite um número para ver a tabuada dele: '))

print('Tabuada do {}'.format(num))

for multiplicando in range(0, 11):
    resultado = num * multiplicando
    print(str(num) + ' x ' + str(multiplicando) + ' = ' + str(resultado))