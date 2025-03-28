entrada = input("Digite um numero inteiro")
num = int(entrada)
resto = num % 2
if resto == 0:
    print(num, "é par")
else:
    print(num, "é impar")
    