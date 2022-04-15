"""Desenvolva um programa que verifique e mostre os números entre 1.000 e 2.000 que, quando divididos por 11, produzam o resto igual a 5.
"""

for i in range(1000, 2001):
    if (i % 11) == 5:
        print(i)

"""Se i for dividio por 11 e o resto da divisão for 5 será impreso o valor de i"""