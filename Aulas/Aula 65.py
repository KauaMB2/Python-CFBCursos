from tkinter import *
from tkinter import messagebox
def mostrarMsg(tipomsg, msg):
    if(tipomsg == "1"):
        messagebox.showinfo(title = "CFB Cursdos", message = msg)
    elif(tipomsg == "2"):
        messagebox.showwarning(title = "CFB Cursdos", message = msg)
    elif(tipomsg == "3"):
        messagebox.showerror(title = "CFB Cursdos", message = msg)
def resetarTB():
    res = messagebox.askyesno("vsbndf", "Confirma reset do textbox?")
    if(res == True):
        tb_num.delete(0, END)
        tb_num.insert(0, "1")
vmsg = "Curso de Python/Tkiter"
app = Tk()

app.title("CFB Cursos")
app.geometry("500x300")
vnum_cstexto = StringVar()
Label(app, text = "Tipo de cx(1, 2 ou 3)").pack()
tb_num = Entry(app, textvariable = vnum_cstexto)
vnum_cstexto.set("1")
tb_num.pack()
btn_msg = Button(app, text = "Mostrar mensagem", command = lambda: mostrarMsg(vnum_cstexto.get(), vmsg))
btn_msg.pack()
btn_reset = Button(app, text = "Resetar", command = resetarTB)
btn_reset.pack()
app.mainloop()