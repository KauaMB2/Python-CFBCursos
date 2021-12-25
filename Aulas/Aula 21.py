valores = [1, 5, 3, 2, 10, 4, 8]
def somar(num):
    r = 0
    for n in num:
        r+=n
    return r
r = somar(valores)
print(str(valores) + ": Soma = " + str(r))