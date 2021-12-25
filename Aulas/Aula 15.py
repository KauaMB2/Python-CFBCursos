t_carros = ("HRV", "Golf", "Argo")#lista
l_carros = list(t_carros)
l_carros[2] = "Focus"
#Na lista pode modificar os elementos dentro dela, na tupla não, a tupla é imutável...
#...mas se criarmos uma lista e iguaar uma tupla à essa lista...
#...poderemos modificar a lista e indiretamente a tupla
t_carros =  tuple(l_carros)#tupla
for x in t_carros:
    print(x)