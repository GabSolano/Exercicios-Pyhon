dec = int(input("informe um numero inteiro positivo: "))

while dec < 0:
    print("numero invalido")
    dec = int(input("informe um numero inteiro positivo: "))

binario = 0
pot10 = 1
while dec != 0:
    restpos = dec % 2
    binario = binario + restpos * pot10
    dec = dec // 2
    pot10 = pot10 * 10

print("binario: ", binario)