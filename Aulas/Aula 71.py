from tkinter import *
from tkinter import ttk
def impEsporte():
    ve = cb_esportes.get()
    print("Esporte " + ve)
app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")
listEsportes = ["Futebol", "Vôlei", "Basquete"]
lb_esportes = Label(app, text = "Esportes")
lb_esportes.pack()
cb_esportes = ttk.Combobox(app, values = listEsportes)
cb_esportes.set("Futebol")
cb_esportes.pack()
btn_esportes = Button(app, text = "Esporte selecionado: ", command = impEsporte)
btn_esportes.pack()
app.mainloop()