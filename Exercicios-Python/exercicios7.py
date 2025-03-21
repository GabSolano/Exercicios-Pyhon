#receber numero inteiro 0 a 99
aux = input("Digite um numero entre 00 a 99:")
num_a = int(aux)

#e imprime o dígito das dezenas e o dígito das unidades desse número.
dez = num_a // 10
uni = num_a % 10
print("Dezena", dez)
print("Unidade", uni)
