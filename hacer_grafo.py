from tkinter import *
from grafo import Grafo
#crear ventana
ventana=Tk()
ventana.geometry("1240x700") #tamaño
#llamar a la clase grafo
conjunto=Grafo(ventana)
#mostrar la pantalla
ventana.mainloop()
