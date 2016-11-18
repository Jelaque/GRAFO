from tkinter import *
from grafo import Grafo
#crear ventana
ventana=Tk()
ventana.geometry("1240x700") #tamaño
#llamar a la clase grafo
conjunto=Grafo(ventana)
#mostrar la pantalla
ventana.mainloop()
ventana2=Tk()
ventana2.geometry("1240x700")
conjunto2=Grafo(ventana2)
ventana2.mainloop()
