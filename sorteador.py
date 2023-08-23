import random
tent = 4
vida = 200
resto = 0

while resto == 0:
    num_sor = random.randrange(0, 100) #sorteia de 0 á 100
    resto = num_sor % 2 #define que é impar (dividindo por 2)
    print(" ♥ SORTEADOR - - - ADIVINHE O NÚMERO SORTEADO!")
    print("Você tem:",vida,"DE VIDA")

while tent > 0 and vida > 0: #enquanto a tentativa e vida é maior que zero... (para rodar)
    number = int(input ("Digite um número: ")) #Usuário define o numero que será guardado (criação da variavel escre_number)
    if number == num_sor:
        print("UHHHHHHUL Você venceu ♥☺")   #if é tipo o acerto, se não...
        break
    else:                      #se não...
        tent = tent - 1        # número de tentativas
        vida = vida - abs(number - num_sor)   #Número de vidas vida(número escrito - número sorteado)
        print("Você errou! poxa que pena, tente novamente ")
        print("Você tem:", vida, "DE VIDA")
        continue
if tent == 0 or vida <= 0:    #quando a tentativa for zero ou a vida menor ou igual a zero acaba o jogo
    print("Poxa camarada se perdeu ermão")
    print("o número sorteado era: ", num_sor)


