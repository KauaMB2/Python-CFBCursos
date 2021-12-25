import re #RegEx
text = "Curso de Python do CFB Cursos, canal do youtube"
res = re.split("\s", text)#Divide os caracteres cada vez que encontra um espaço
print(res)
print(res[2])
for t in res:
    print(t)
