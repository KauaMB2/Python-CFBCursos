nome = "teste.txt"
f = open("C:/Users/Rafael/Desktop/ETE Escola Kauã/Python - CFB Cursos/Aula 44/"+nome, "wt")
#r - read - Leitura
#a - append - Anexar
#w - write - Escrita
#x - creaete - criar
#t - texto
#b - binário
f.write("Kaua Moreira Batista\n")
f.write("Curso de Python\n")
txt = input("Digite um texto:" )
f.write(txt + "\n")
f.close()