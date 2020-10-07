#!/usr/bin/env python3

#aceitando argumentos da linha de comando

import sys

try:
	DNA = str(sys.argv[1])
except ValueError:
	print('DNA não é uma string')

DNA1 = DNA.upper()

try:
	n1 = int(sys.argv[2])
	n2 = int(sys.argv[3])
	n3 = int(sys.argv[4])
	n4 = int(sys.argv[5])
except ValueError:
	print('n1, n2, n3 e n4 devem ser valores inteiros')

#conferir os valores da linha de comando

if isinstance(DNA, str):
	print('correto:DNA é uma string')
else: 
	print('erro: insira DNA como uma string')

if isinstance(n1 and n2 and n3 and n4, int):
	print('correto: n1, n2, n3 e n4 são número inteiros')
else:
	print('erro: n1, n2, n3 e n4 devem ser números inteiros')

if n1 < n2 < n3 < n4 < len(DNA1):
	print('correto: n1, n2, n3 e n4 são menores que DNA')
else: 
	print('erro: insira n1, n2, n3 e n4 em ordem crescente e sendo menor que DNA')

#extrair a sequencia da CDS 1 e conferir se inicia com códon ATG


if(DNA1[n1-1:n1+2])== "ATG":
	print('inicia com o codon ATG')
else:
	print('CDS não inicia com o codon ATG')

CDS1 = DNA1[n1-1:n2-1]

#conferir se termina com o códon de parada

if(DNA1[n4-1:n4+2]) == "TAA":
	print('termina com codon de parada')
elif(DNA1[n4-1:n4+2]) == "TGA":
	print('termina com códon de parada')
elif(DNA1[n4-1:n4+2]) == "TAG":
	print('termina com códon de parada')
else:
	print('CDS2 não termina com codon TAG, TAA, TGA')

CDS2 = DNA1[n3-1:n4-1]

#junção do CDS1 e do CDS2 
print(CDS1+CDS2)
