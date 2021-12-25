from tkinter import *
def imprimirEsporte():
    print("Esporte: " + str(lb_esportes.get(ACTIVE)))
def addEsportes():
    lb_esportes.insert(END, vnovoesporte.get())
app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")
listaEsportes = ["Futebol", "Vôlei", "Basquete"]
lb_esportes =Listbox(app)
for esportes in listaEsportes:
    lb_esportes.insert(END, esportes)
lb_esportes.pack()
btn_esporte = Button(app, text = "Imprimir esporte", command = imprimirEsporte)
btn_esporte.pack()
vnovoesporte = Entry(app)
vnovoesporte.pack()
btn_inserir = Button(app, text = "Adionar esporte", command = addEsportes)
btn_inserir.pack()
app.mainloop()