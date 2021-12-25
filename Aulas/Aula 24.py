class Carro:
    velMax = 0
    ligado = False
    cor = ""
    def __init__(self, v, l, c):# Self é usado ​​para inicializar o estado do objeto
        self.velMax = v
        self.ligado = l
        self.cor = c
    def mostrar(self):
        print("Velocidade Maxima: " + str(self.velMax))
        print("Cor: " + self.cor)
        estado = "Sim" if self.ligado else "N"#Carro está em estado de "Ligado" se o "self.ligado" for verdadeiro
        print("Ligado: " + estado)
        print("====================")
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def andar(self):
        if(self.ligado):
            print("Andando")
        else:
            print("Carro desligado")
c1 = Carro(200, False, "Preto")#Chama a função def __init__
c2 = Carro(120, False, "Branco")#Chama a função def __init__
c3 = Carro(250, False, "Vermelho")#Chama a função def __init__
c1.ligar()#Chama a função ligar
c1.mostrar()#Chama a função mostrar
c2.mostrar()#Chama a função mostrar
c3.mostrar()#Chama a função mostrar
c1.andar()#Chama a função andar
c2.andar()#Chama a função andar