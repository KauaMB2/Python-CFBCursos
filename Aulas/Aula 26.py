num = -10
try:
    print(x)
except:
    print("Erro no programa")
else:
    print("Tudo certo")
finally:
    print("Fim do tratamento")
    print("===================")
num = "Kauã"
if not type(num) is int:#Se o tipo de variável atribuido à "num" não for inteiro, irá executar o comando de aviso abaixo
    raise Exception("Somente numeros permitidos")
else: #Se não...
    print(str(num))
    