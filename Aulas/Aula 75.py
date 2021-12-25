from tkinter import *
def ImpVal():
    print("Valor: " + str(sb_valores.get()))
#sb_valores = Spinbox(app, from_=0, to = 10)
app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")
sb_valores = Spinbox(app, values = (1, 2, 3, 4, 5))
sb_valores.pack()
btn_valor = Button(app, text = "Imprimir valor", command = ImpVal)
btn_valor.pack()
app.mainloop()