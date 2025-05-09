# Solicita a entrada da frase e da letra
frase = input("Digite uma frase: ")
letra = input("Digite uma letra: ")

# Inicializa uma variável para armazenar o resultado
resultado = ""

# Substitui todas as ocorrências da letra (maiúscula ou minúscula) por '*'
for char in frase:
    if char.lower() == letra.lower():
        resultado += "*"
    else:
        resultado += char

# Imprime o resultado
print(resultado)