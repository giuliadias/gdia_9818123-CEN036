#!/usr/bin/env python3 

#importando sys

import sys 

#inserindo as variáveis a e b no script

try:
	a = int(sys.argv[1])
except ValueError:
	print("valor de a não é um número inteiro, insira-o novamente")


try:
	b  = int(sys.argv[2])
except ValueError:
	print('valor de b não um número inteiro, insira-o novamente')

#aparece para o usuário que tipo de variável é a e b
#print(type(a), a, b)

#verificação se a e b são valores inteiros

print(isinstance(a and b, int))


if (a<=0 or a>1000):
	print('erro argv 1: insira um número maior que 0 e menor que 1000.')
else:
	print('valor de a está correto')

if (b<=0 or b>1000):
	print('erro argv 2: insira um número maior que 0 e menor que  com 1000')
else:
	print('valor de b está correto')

if ((a>0 or a<1000) and (b>0 or b<1000)):
	resultado = round(((a**2 + b**2)**0.5),2)
	string = "O quadrado da hipotenusa para o triângulo retângulo com lados a = {} e b = {}, é {}."
	print(string.format(a,b,resultado))
