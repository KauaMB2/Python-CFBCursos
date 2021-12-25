import re #RegEx
import os 
nome = "teste.txt"
caminho = ("C:/Users/Rafael/Desktop/ETE Escola Kauã/Python - CFB Cursos/Aula 46/")
if os.path.exists(caminho + nome):
    print("Arquivo Existente")
else:
    f = open(caminho + nome, "x")
    f.close()
    os.system('pause')
if os.path.exists(caminho + nome):
    os.remove(caminho + nome)
    print("Arquivo Removido")
else:
    print("Arquivo inexistente")