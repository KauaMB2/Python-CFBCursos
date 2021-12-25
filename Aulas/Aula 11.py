a = 10
b = 5
res = 0
op= "/"
if op== "+":
    print("Foi escolhido soma")
    res = a + b
elif op == "-":
    print("Foi escolhido subtração")
    res = a-b
elif op == "*":
    print("Foi escolhido multiplicação")
    res = a*b
elif op == "/":
    print("Foi escolhido divisão")
    res =  a/b
print("O resultado do cálculo é: " + str(res))
print("===============================")
clima = "sol"
dinheiro = 650
lugar = ""
if (clima == "sol" or ((dinheiro>= 300) and (dinheiro <=500))):
    lugar = "clube"
else:
    lugar = "cinema"
print("Vou ao " + lugar)