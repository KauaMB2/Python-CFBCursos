import re #RegEx
text = "Curso de Python do CFB Cursos"
pesq = input("Pesquisar: ")
res = re.findall(pesq, text)
print(res)
qtde = len(res)
print("Qtde: " + str(qtde))
for t in res:
    print(t)