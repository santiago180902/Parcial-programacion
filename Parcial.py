from tkinter import *
import numpy as np

def limpiar():
    Funcion_Problema.set("")
    Funcion_Problema1.set("")


def matriz(): 
    filas=int(Funcion_Problema.get()) 
    columnas=int(Funcion_Problema1.get())
    matriz=[]

    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            valor=int(input("fila{},columna{}:".format(i+1,j+1)))
            matriz[i].append(valor)
    print()
    for fila in matriz:
        print("[",end=" ")
        for elemento in fila:
            print("{}".format(elemento),end=" ")
            print("]")
    print()


def Revisar_Numero():
    diction = [3,2,3,4,5]
    maxInt = max(diction)
    counter = [0] * (maxInt+1)
    for i in diction:
        counter[i] += 1
    
    result = {}
    for i in range(maxInt):
        if(counter[i]>1):
            result[i] = i * counter [i]
    
    return result


ventana=Tk()
ventana.title("MATRICES")
ventana.geometry("800x500")
ventana.config(bg="yellow")

panel2=Frame()
panel3=Frame()

panel2.config(width="800",height="470",bg="Blue1")
panel2.place(x=0,y=120)
panel3.config(width="800",height="470",bg="red")
panel3.place(x=0,y=190)

Funcion_Problema=StringVar()
Funcion3=Entry(ventana,textvariable=Funcion_Problema).place(x=320,y=240)


Funcion_Problema1=StringVar()
Funcion3=Entry(ventana,textvariable=Funcion_Problema1).place(x=320,y=284)

solucion_matriz=StringVar()
Funcion3=Entry(ventana,textvariable=solucion_matriz).place(x=320,y=414)

boton1=Button(ventana,text="Solucionar",width=10,height=1,bg="LightBlue1",relief="groove",command=matriz)
boton1.place(x=460, y=204)

boton2=Button(ventana,text="Limpiar",width=10,height=1,bg="LightBlue1",relief="groove",command=limpiar)
boton2.place(x=460, y=254)

titulo=Label(ventana,text="x",bg="dark slate gray",font=('Arial',16,),fg="white")
titulo.place(x=135,y=204)

titulo1=Label(ventana,text="+",bg="dark slate gray",font=('Arial',16,),fg="white")
titulo1.place(x=290,y=204)

titulo2=Label(ventana,text="Matrices",bg="dark slate gray",font=('Arial',16,),fg="white")
titulo2.place(x=230,y=4)


titulo5=Label(ventana,text="Numero_de_columnas",bg="dark slate gray",font=('Arial',16,),fg="white")
titulo5.place(x=0,y=240)

titulo6=Label(ventana,text="Numero_de_fiilas",bg="dark slate gray",font=('Arial',16,),fg="white")
titulo6.place(x=0,y=284)


titulo7=Label(ventana,text="Resultado",bg="dark slate gray",font=('Arial',16,),fg="white")
titulo7.place(x=0,y=414)
ventana.mainloop()