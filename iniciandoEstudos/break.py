while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break # o break é para parar a execução do código

    print(numero)

for numero in range(100):

    if numero %2 == 0:

        continue # o continue vai pular 

    print(numero, end=" ")