from tkinter import *
from tkinter import ttk
def valbarra(m):
    cont = 0
    etapas = m/100
    while(cont < etapas):
        cont = cont + 1
        i = 0
        while(i < 1000000):
            i = i + 1
        varBarra.set(cont)
        app.update()
app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")
varBarra = DoubleVar()
varBarra.set(0)
pb = ttk.Progressbar(app, variable = varBarra, maximum = 100)
pb.place(x = 0, y = 0, width = 500, height = 40)
btn2 = Button(app, text ="Definir Barra", command = lambda:valbarra(10000))
btn2.place(x = 0, y = 40, width = 100, height = 40)
app.mainloop()