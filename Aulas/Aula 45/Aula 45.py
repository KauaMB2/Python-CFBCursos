import re
nome = "teste.txt"
f = open("C:/Users/Rafael/Desktop/ETE Escola Kauã/Python - CFB Cursos/Aula 45/"+nome, "rt")
#for l in f:
#    print(l)
res = re.sub("\s", "-", f.readline())
f.close()
f = open("C:/Users/Rafael/Desktop/ETE Escola Kauã/Python - CFB Cursos/Aula 45/"+nome, "wt")
f.write(res)
f.close()
#r - read - Leitura
#a - append - Anexar
#w - write - Escrita
#x - creaete - criar
#t - texto
#b - binário