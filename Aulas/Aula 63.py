from tkinter import *
def imprimirEsporte():
    ve = vesporte.get()
    if(ve == "f"):
        print("Esporte Futebol")
    elif(ve == "v"):
        print("Esporte Vôlei")
    elif(ve == "b"):
        print("Esporte Basquete")
    else:
        print("Escolha um esporte")
app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")
vesporte = StringVar()
vcor = StringVar()
bl_esportes = Label(app, text = "Esportes")
bl_esportes.pack()
rb_futebol = Radiobutton(app, text = "Futebol de bosta", value ="f", variable = vesporte)
rb_futebol.pack()
rb_volei = Radiobutton(app, text = "Vôlei", value = "v", variable = vesporte)
rb_volei.pack()
rb_basquetete = Radiobutton(app, text = "Basquetin", value = "b", variable = vesporte)
rb_basquetete.pack()
rb_verde = Radiobutton(app, text = "Verde", value = "#0f0", variable = vcor)
rb_verde.pack()
rb_vermelho = Radiobutton(app, text = "Vermelho", value = "#f00", variable = vcor)
rb_vermelho.pack()
btn_esporte = Button(app, text = "Esporte selecionado", command = imprimirEsporte)
btn_esporte.pack()
app.mainloop()