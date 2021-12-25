import datetime
data = datetime.datetime.now()
nasc = datetime.datetime(1978, 3, 7)
print(str(data.day) + "/" + str(data.month) + "/" + str(data.year))
print(nasc.strftime("%A"))
# %a texto dia da semana abreviado
# %A texto dia da semana 
# %W num dia da semana
# %d num dia do mês
# %b texto mês abreviado
# %B texto mês
# %m num do mês
# %y Ano com dois digitos
# %Y Ano com quatro digitos
# %H 00 - 23
# %I 00 - 12
# %p AM / PM
# %M minutos
# %S segundos
# %f microssegundos
#j dia do ano | 001 até 366