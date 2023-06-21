from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING
from backup import *

root = Tk()
root.title('Respaldos')
root.geometry('500x500')

def mensaje():
    pregunta = askokcancel (title='Confirmation', message='Seguro que quieres respaldar este proceso puede tardar varios minutos', icon=WARNING)
    if pregunta:
        texto = funcion()
        mostrar.config(state="normal")
        mostrar.insert(INSERT, texto) 
        mostrar.config(state="disable") 
    else:
        mostrar.config(state="normal")
        mostrar.delete(1.0, END) 
        mostrar.insert(INSERT, "ERROR") 
        mostrar.config(state="disable") 
    

e=Label(root, text='Respaldos')
btn=ttk.Button(root, text='Respaldar ahora', command=mensaje)
mostrar=Text(root, state="disable")

mostrar.config(font=("Consolas",16))
e.pack()
btn.pack()
mostrar.pack(padx=20, pady=20)

root.mainloop()