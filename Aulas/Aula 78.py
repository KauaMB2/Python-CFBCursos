from tkinter import *
from tkinter import ttk
def mostrar():
    mostrarIdade = Label(app, text = "           ")
    mostrarIdade.grid(column = 0, row = 4, columnspan = 2, pady = 5)
    mostrarNome = Label(app, text = "            ")
    mostrarNome.grid(column = 1, row = 4, columnspan = 2, pady = 5)
    mostrarIdade = Label(app, text = "Idade: " + idade.get())
    mostrarIdade.grid(column = 0, row = 4, columnspan = 2, pady = 5)
    mostrarNome = Label(app, text = " | Nome: " + nome.get())
    mostrarNome.grid(column = 1, row = 4, columnspan = 2, pady = 5)
    app.update()
app = Tk()
nome = StringVar()
idade = StringVar()
app.title("CFB Cursos")
app.geometry("500x300")
lb_canal = Label(app, text = "CFB Cursos")
lb_nome = Label(app, text = "Digite seu nome")
lb_idade = Label(app, text = "Informe sua idade")
et_nome = Entry(app, textvariable = nome)
et_idade = Entry(app, textvariable = idade)
btn = Button(app, text = "Mostrar texto", command = mostrar)
lb_canal.grid(column = 0, row = 0, columnspan = 2, pady = 0)
lb_nome.grid(column = 0, row = 1, sticky = 'w')#n s e w
et_nome.grid(column = 0, row = 2, padx = 5)
lb_idade.grid(column = 1, row = 1, sticky = 'w')#n s e w
et_idade.grid(column = 1, row = 2, padx = 5)
btn.grid(column = 0, row = 3, columnspan = 2, pady = 5)
app.mainloop()