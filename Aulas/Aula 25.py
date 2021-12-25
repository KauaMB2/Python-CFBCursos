class NPC: #Base , pai, superclasse
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100
    def info (self):
        print("Nome: " + self.nome)
        print("Time: " +  str(self.time))
        print("Forca: " +  str(self.forca))
        print("Municao: " +  str(self.municao))
        print("Vivo: " +  ("Sim" if self.vivo else "Nao"))
        print("Energia: " +  str(self.energia))
        print("========================")
class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao)# Envia as informações da classe filho para a classe pai
class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome, time, self.forca, self.municao)# Envia as informações da classe filho para a classe pai
class Elite(NPC):
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500
        super().__init__(nome, time, self.forca, self.municao)# Envia as informações da classe filho para a classe pai
    def inf(self):
        super().info()
s1 = Guarda("Guarda1", 1)
s2 = Soldado("Solado1", 1)
s3 = Elite("Elite1", 1)
s4 = Guarda("Guarda1", 2)
s5 = Soldado("Soldado1", 2)
s6 = Elite("Elite1", 2)
s1.vivo = False
s2.vivo = False
s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.inf()