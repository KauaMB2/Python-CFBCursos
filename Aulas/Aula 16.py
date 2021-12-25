carros = [
    ["Modelo", "HRV"],#Modelo = [0][0] | HRV = [0][1]
    ["Fabricante", "Honda"], #Fabricante = [1][0] | HRV = [1][1]
    ["Ano", 2016]#Ano = [0][2] | Ano = [1][2]
]
carros.append(["Cor", "Prata"])#Adiociona "Cor" dentro da matriz
carros[2][1] = 2019
print(carros[1][1] + "\n")
for l, c in carros:
    print("Linhas: " + l + " | Coluna: " + str(c))