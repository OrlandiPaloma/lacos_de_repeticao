#Laços de repetição
#Imprima os valores de 1 a N
'''
Input numero maximo
valor inicial = 1
loop de valor inicial a numero_maximo
  print valor
'''

numero_maximo = int(input("Digite o numero maximo"))
valor_inicial = 1
for numero in range(valor_inicial, numero_maximo + 1):
  print(numero)