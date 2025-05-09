##. Crie um programa que imprime uma String contendo os caracteres da entrada palavra separados por espaços. Por exemplo, se a entradao for a palavra "Manga", seu programa deverá
##imprimir "M a n g a ".

# Solicita a entrada de uma palavra
palavra = input("Digite uma palavra: ")

# Junta os caracteres da palavra com espaços entre eles
resultado = ' '.join(palavra)

# Imprime o resultado
print(resultado)
