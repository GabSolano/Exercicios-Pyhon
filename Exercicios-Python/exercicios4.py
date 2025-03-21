#Lendo um numero do telcado
aux = input("Digite o primeiro numeros inteiros")
#Convertendo a informacao para int
num_a = int(aux)

aux = input("Digite o segundo numeros inteiros")
num_b = int(aux)

#processamento
prod = num_a * num_b #multiplicaco
soma = num_a + num_b #somar
div = num_a // num_b #Divisao
resto = num_a % num_b # Resto da divisao

print("soma", soma)
print("Multiplicaco", prod)
print("Divisao", div)
print("Resto", resto)