frase = input("ingresa una frase: ")
lista = []
lista = frase.split()
lista = frase.upper()

print("palabras de la frase", lista)

for continua in lista :
    print(continua.upper())