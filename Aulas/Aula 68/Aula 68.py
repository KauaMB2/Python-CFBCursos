from tkinter import *
from tkinter import messagebox
import os
pastaApp = os.path.dirname(__file__)
app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")
imgLogo = PhotoImage(file = pastaApp + "\\5B9U.gif")
i_logo = Label(app, image = imgLogo)
i_logo.place(x = 10, y = 10)
app.mainloop()