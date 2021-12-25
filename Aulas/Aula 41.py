import re #RegEx
text = "Curso de Python do CFB Cursos"
res = re.search("Python", text)
if(res != None):
    pi = res.start()
    pf = res.end()
    tam = pf - pi
    print(res.start())
    print(res.end())
    print(tam)
else:
    print("Não encontrado")