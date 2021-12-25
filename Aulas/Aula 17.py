carros = {
    "Carro1":{
        "Fabricante":"Honda",
        "Modelo":"HRV"
    },
    "Carro2":{
        "Fabricante": "Volkswagem",
        "Modelo":"Golf"
    },
    "Carro3":{
        "Fabricante":"Ford",
        "Modelo":"Focus"
    },
}
print(carros["Carro1"]["Fabricante"])
x = 0
y = 0
for x in carros:
    print(x + ": " + str(carros[x]))
    for y in carros[x]:
        print(y + ": " + str(carros[x][y]))
print("================================")
carro = {
    "Fabricante":"Honda",
    "Modelo":"HRV",
    "Ano":"2016",
    "Cor":"Prata"
}
carro["Cambio"] = "Automatico"
carro.pop("Cambio")
fab = carro.get("Fabricante")
carro["Cor"] = "Preto"
if "Modelo" in carro:
    print("Sim, modelo e uma chave\n")
controle = True
for c,v in carro.items():
    if(controle == True):
        print("Tamanho do dicionário: " + str(len(carro)))
    controle = False
print("Programa encerrado")