from tkinter import *
from tkinter import messagebox
def mostrarMsg():
    messagebox.showinfo(title = "CFB Cursos", message = "CFB Cursos")
vmsg = "Curso de Python/Tkiter"
app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")
vnum1_cstexto = StringVar()
fr_quadrado1 = Frame(app, borderwidth = 1, relief = "sunken")
fr_quadrado1.place(x = 10, y = 10, width = 300, height = 100)
Label(fr_quadrado1, text = "Tipo de cx(1, 2 ou 3)").pack()
tb_num = Entry(fr_quadrado1, textvariable = vnum1_cstexto)
vnum1_cstexto.set("")
tb_num.pack()
btn_msg = Button(fr_quadrado1, text = "Mostrar mensagem", command = lambda: mostrarMsg())
btn_msg.pack()
vnum2_cstexto = StringVar()
fr_quadrado2 = Frame(app, borderwidth = 1, relief = "sunken", background = "#008")
fr_quadrado2.place(x = 10, y = 120, width = 300, height = 100)
lb_Label = Label(fr_quadrado2, text = "Kauã", background = "#008", foreground = "#fff", font = ("Arial", 25))
lb_Label.pack(side = LEFT, fill = X, expand = TRUE)
app.mainloop()