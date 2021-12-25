curso = "Curso de Python"
#res = "python" in texto.lower()
#print(res)
canal = "CFB Cursos"
cidade = "Santa Rita do Sapucaí"
dia = 31
mês = "Outubro"
ano = 2021
print(cidade + ", " + str(dia) + " de " + mês + " de " + str(ano))
data = "{}, {} de {} de {} - \"{}\""
a = data.format(cidade, dia, mês, ano, canal)
print(cidade + ", " + str(dia) + " de " + mês + " de " + str(ano) + " - " + "\"" + canal + "\"" + "\n" + a)