import os
import random
jogarNovamente = "s"
jogadas = 0
quemJoga = 2 # CPU = 1 | Jogador = 2
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
    quemJoga = 2
    global maxJogadas
    if quemJoga==2 and jogadas<maxJogadas:
        try:
            l = int(input("Linha..: "))
            c = int(input("Coluna.: "))
            while(velha[l][c]!= " "):
                l = int(input("Linha..: "))
                c = int(input("Coluna.: "))
            velha[l][c] = "X"
            quemJoga = 1
            jogadas += 1
        except:
            print("Jogada inválida")
            os.system("pause")
def cpuJoga():
    global jogadas
    global quemJoga
    quemJoga = 1
    global maxJogadas
    if quemJoga==1 and jogadas<maxJogadas:
        l = random.randrange(0,3)
        c = random.randrange(0,3)
        while velha[l][c]!= " ":
            l = int(input("Linha..:"))
            c = int(input("Coluna.:"))
        velha[l][c] = "O"
        quemJoga = 2
        jogadas += 1
def verificarVitoria():
    global velha
    vitoria = "n"
    simbolos = ["X", "O"]
    for s in simbolos:
        vitoria = "n"
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if (velha[il][ic]==s):
                    soma += 1
                il += 1
            if(soma == 3):
                vitoria = s
                break
            il += 1
        if(vitoria!= "n"):
            break
        while ic < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if (velha[il][ic]==s):
                    soma += 1
            if(soma == 3):
                vitoria = s
                break
            ic += 1
        if(vitoria!= "n"):
            break
        soma = 0
        idiagl = 0
        idiagc = 0
        while idiagc >= 0:
            if(velha[idiagl][idiagc]):
                soma += 1
            ic += 1
        if(soma == 3):
            vitoria = s
            break
        il += 1
def redefinir():
    global velha
    global jogadas 
    global quemJoga
    global vit
    jogadas = 0
    quemJoga = 0
    maxJogadas = 0
    vit = "n"
    velha = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
while True:
    tela()
    jogadorJoga()
    cpuJoga()
    vit = verificarVitoria()
    if(vit!="n")or(jogadas>=maxJogadas):
        break
    print("FIM DE JOGO")
    if():
        print("Resultado: Jogador " + vit + "venceu")
    else:
        print("Resultado: Empate")
    jogarNovamente = input("Jogar novamene [s/n]")
    redefinir()