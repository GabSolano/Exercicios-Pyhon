
plac1 = int(input("Digite os gols do Corinthians: "))
plac2 = int(input("Digite os gols do Palmeiras: "))

if plac1 > plac2:
    print(f"VAI CORINTHIANS: {plac1} x {plac2}")
elif plac2 > plac1:
    print(f"VAI TMNC PALMEIRAS: {plac1} x {plac2}")
else:
    print(f"Os dois times empataram: {plac1} x {plac2}")