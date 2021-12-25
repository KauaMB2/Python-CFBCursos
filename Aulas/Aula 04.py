print("===============Int===============")
x = 1 #int
print("Valor: " + str(x))
print("Tipo: " + str(type(x)))
print("===============String===============")
x = "CFB Cursos" #string
print("Valor: " + str(x))
print("Tipo: " + str(type(x)))
print("===============Float===============")
x = 15.6 #float
print("Valor: " + str(x))
print("Tipo: " + str(type(x)))
print("===============Bool===============")
x = False #bool
print("Valor: " + str(x))
print("Tipo: " + str(type(x)))
print("===============Complexo===============")
n1 = 5; n2 = 2;x = complex(n1, n2) #complexo
print("Parte real: " + str(x.real))
print("Parte imaginária: " + str(x.imag))
print("Valor: " + str(x))
print("Tipo: " + str(type(x)))
print("===============Lista/Array===============")
x = ["carro", "aviao", "navio"] #lista / array
print("Valor: " + x[0])
print("Valor: " + x[1])
print("Valor: " + x[2])
print("Tipo: " + str(type(x)))
print("===============Tupla===============")
x = ("carro", "aviao", "navio") #tupla
print("Valor: " + x[0])
print("Valor: " + x[1])
print("Valor: " + x[2])
print("Tipo: " + str(type(x)))
print("===============Lista int===============")
x = range(0, 100, 1) #List int
print("Valor: " + str(x))
print("Tipo: " + str(type(x)))
print("===============Dicionário===============")
x = { #dicionário
    "canal": "CFB Cursos",
    "curso": "Curso de python",
    "nome": "Bruno"
}
print("Valor: " + x["canal"])
print("Valor: " + x["curso"])
print("Valor: " + x["nome"])
print("Tipo: " + str(type(x)))
x = {7, 8, 7, 0, 9, 1, 5, 2, 10, 3, 4, 6} #set
print("===============Set modificável===============")
print("Valor: " + str(x))
print("Tipo: " + str(type(x)))
x = frozenset({7, 8, 7, 0, 9, 1, 5, 2, 10, 3, 4, 6}) #set
print("===============Set fixo===============")
print("Valor: " + str(x))
print("Tipo: " + str(type(x)))