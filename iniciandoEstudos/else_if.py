MAIOR_IDADE = 18

idade = int(input("Infome sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você já pode tirar a sua CNH.")

elif idade < MAIOR_IDADE:
    print("Você ainda não pode tirar a CNH.")
    texto = f"Aguarde {MAIOR_IDADE - idade} anos!"
    print(texto)

else:
    print("Ainda não pode tirar a CNH")


#  elif é usado para estabelecer várias condições em python, é como se fosse o else if em Javascript 