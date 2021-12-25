import json 
#Transformando array em json
carros = {
    "marca": "honda",
    "modelo": "HRV",
    "cor": "prata"
}
carros_json = json.dumps(carros)#Transforma o array e json
print(carros_json)
#Pegando algum valor de dentro do padrão json e exibindo
carros_json = '{"marca":"honda","modelo":"HRV","cor":"prata"}'
carros = json.loads(carros_json)#Carrega a variável carros_json na variavel carro
print(carros)
for k, v in carros.items():
    print(k, v)