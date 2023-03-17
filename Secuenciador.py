from tkinter import *
from tkinter import messagebox
from turtle import width

raiz = Tk()
raiz.title('Secuenciador')
raiz.resizable(0,0)
#raiz.geometry('200x200')
miFrame=Frame()
miFrame.pack()
miFrame.config(width="400", height="200")


boletas = StringVar()
seleccion = IntVar()
oki = StringVar()

lista = ""

def acercaDe():
    messagebox.showinfo(title="Acerca de:", message="Creado por Marcos Tapia")

barraMenu = Menu(miFrame)
menuAcerca = Menu(barraMenu, tearoff=1)
menuAcerca.add_command(label="Acerca de", command=acercaDe)

raiz.config(menu=menuAcerca)

label1=Label(miFrame, text='Ingrese la cantidad de boletas:')
label1.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

label2=Label(miFrame, text=oki.get())
label2.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

cuadroBoletas=Entry(miFrame, textvariable=boletas)
cuadroBoletas.grid(row=1, column=0, columnspan=4, sticky="ew", padx=5, pady=5)


def codigoBoton(num):
    global tope
    global cont
    global lista
    global oki

    tope = StringVar()
    cont = 0
    
    tope = int(num) * 3 + 1

    if seleccion.get()==1:
        for i in range(1,tope):
            cont += 1
            if cont != 1:
                if i != tope - 1:
                    lista = lista + str(i) + ","
                else:
                    lista = lista + str(i)
            if cont == 3:
                cont = 0

    if seleccion.get()==2:
        for i in range(tope):
            cont += 1
            if cont == 3:
                cont = 0
            else:
                if i != 0:
                    if i != tope - 1:
                        lista = lista + str(i) + ","
                    else:
                        lista = lista + str(i)

    if seleccion.get()==3:
        for i in range(1,tope):
            cont += 1
            if cont != 3:
                if i != tope - 2:
                        lista = lista + str(i) + ","
                else:
                        lista = lista + str(i)
            if cont == 3:
                cont = 0


    boletas.set(lista)
    tope = 0
    cont = 0
    i = 0
    lista = ""
    oki = "Se ha generado la secuencia de páginas a eliminar"
    label2.config(text=oki)


botonCalcular=Button(miFrame, text="Calcular", command=lambda:codigoBoton(boletas.get()))
botonCalcular.grid(row=3, column=1, padx=5)


def copiar_al_portapapeles():
    miFrame.clipboard_clear()
    miFrame.clipboard_append(cuadroBoletas.get())
    label2.config(text="Se copió la secuencia al portapapeles")

botonCopiar = Button(miFrame, text="Copiar",command=copiar_al_portapapeles)
botonCopiar.grid(row=3, column=2, sticky="w", padx=5)

def clearTextInput():
    cuadroBoletas.delete(0, END)
    label2.config(text="")

BotonLimpiar=Button(miFrame, text="Limpiar", command=clearTextInput)
BotonLimpiar.grid(row=3, column=3, padx=5)

seleccion.set(1)

radio1 = Radiobutton(miFrame, text="Original", variable=seleccion, value=1)
radio1.grid(row=3, column=0, sticky="w", padx=10)

radio2 = Radiobutton(miFrame, text="Duplicado", variable=seleccion, value=2)
radio2.grid(row=4, column=0, sticky="w", padx=10)

radio3 = Radiobutton(miFrame, text="Triplicado", variable=seleccion, value=3)
radio3.grid(row=5, column=0, sticky="w", padx=10)

raiz.mainloop()