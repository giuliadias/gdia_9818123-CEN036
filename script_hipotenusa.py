#!/usr/bin/env python3 

import sys 

a = int(sys.argv[1])
b = int(sys.argv[2])

print(type(a), a, b)
print(isinstance(a and b, int))

if (a<=0 or a>1000):
	print('erro argv 1: insira um número maior que 0 e menor que 1000.')

if (b<=0 or b>1000):
	print('erro argv 2: insira um número maior que 0 e menor que  com 1000')

elif ((a>0 or a<1000) and (b>0 or b<1000)):
	resultado = round(((a**2 + b**2)**0.5),2)
	string = "O quadrado da hipotenusa para o triângulo retângulo com lados a = {} e b = {}, é {}."
	print(string.format(a,b,resultado))
