timeA = str(input("Escreva o nome de um time:"))

timeb = str(input("Escreva o nome de um time:"))

golA = int(input(f"{timeA} fez qnts gols:"))
golb = int(input(f"{timeb} fez qnts gols:"))

if golA > golb:
    print(f"{timeA} Venceu o jogo!")
elif golb > golA:
    print(f"{timeb} Venceu o jogo!")