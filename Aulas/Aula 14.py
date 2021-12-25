import os
i = 0
while (i < 1000):
    print(i)
    i+=1
    if(i == 500):
        break
p = input("Digite \"p\" para limpar a tela ou qualquer outra tecla para manter")
if (p == 'p' or p == 'P'):
    os.system('cls')
print("Digite \"-1\" para encerrar")
carros =[]
carro = input("Digite o nome de pelomenos um carro: ")
while (carro != "-1"):
    carros.append(carro)
    carro =  input("Digite o nome do novo carro: ")
print("Loop de entrada de carros encerrado")
p =""
p = input("Digite \"p\" para limpar a tela ou qualquer outra tecla para manter")
if (p == 'p' or p == 'P'):
    os.system('cls')
for x in carros:
    print(x)
print("\nFim do programa")
os.system('pause')