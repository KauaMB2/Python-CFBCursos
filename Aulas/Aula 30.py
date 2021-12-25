import os
import random
jogarNovamente = "s"
jogadas = 0
quemJoga = 9
maxJogadas = 9
vit = "n"
velha = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
def tela():
    global velha
    global jogadas
    os.system("cls")
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: " + str(jogadas))
def jogadorJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas:
        l = int(input("Linha..:"))
        c = int(input("Coluna.:"))
        try:
            while(velha[l][c]!= " "):
                l = int(input("Linha..:"))
                c = int(input("Coluna.:"))
            velha[l][c] = "X"
            quemJoga = 1
            jogadas += 1
        except:
            print("Jogada inválida")
            os.system("pause")
def cpuJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas
    if quemJoga == 1 and jogadas<maxJogadas:
        l = random.randrange(0,3)
        c = random.randrange(0,3)
        while(velha[l][c]!= " "):
            l = int(input("Linha..:"))
            c = int(input("Coluna.:"))
        velha[l][c] = "O"
        quemJoga = 1
        jogadas += 1
while True:
    tela()
    jogadorJoga()
    cpuJoga()