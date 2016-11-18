from tkinter import*
import tkinter.simpledialog
import tkinter.messagebox

class Grafo:
	"""Clase de grafos"""

	def __init__(self,ventana):
		self.matriz=[]
		self.conjunto=[]
		self.posicion=[]
		self.canvas= Canvas(ventana, width=1240, height=700)
		menu=Menu(ventana)
		ventana.config(menu=menu)

		herramientas=Menu(menu)
		menu.add_cascade(label="Herramientas", menu=herramientas)
		herramientas.add_command(label="Agregar Arista", command=self.p_arista)
		herramientas.add_command(label="Agregar Relacion", command=self.p_agregar)
		herramientas.add_command(label="Eliminar Relacion", command=self.p_eliminar)

		opciones=Menu(menu)
		menu.add_cascade(label="Opciones", menu=opciones)
		opciones.add_command(label="Salir", command=ventana.destroy)
		opciones.add_separator()
		opciones.add_command(label="Mostrar Matriz", command=self.mostrar_matriz)

		self.label = Label(ventana, text="", bd=1, relief=SUNKEN, anchor=W)
		self.label.pack(side=BOTTOM, fill=X)

		ventana.bind("<space>", lambda event:self.dibujar())

		grafo=Button(ventana, text="Mostrar Grafo", command=self.dibujar)
		grafo.pack(side=BOTTOM)

		ventana.bind("<Escape>", lambda event:ventana.destroy())
		ventana.bind("<F1>", lambda event:self.p_arista())
		ventana.bind("<F2>",lambda event:self.p_agregar())
		ventana.bind("<F3>", lambda event:self.p_eliminar())

#############ESTO CREA LAS PESTAÑAS DE LA VENTANA, AÑADIENDO LOS METODOS EN CADA OPCION#############

	def dibujar(self):
		self.canvas.delete("all")
		for i in range(len(self.conjunto)):
			x=self.posicion[i][0]
			y=self.posicion[i][1]
			self.canvas.create_oval(x, y, x+16, y+16)
			self.canvas.create_text(x+8, y+8, text=str(self.conjunto[i]))
		for i in range(len(self.matriz)):
			for j in range(len(self.matriz)):
				if self.matriz[i][j]==1:
					if i==j:
						x=self.posicion[i][0]+8
						y=self.posicion[i][1]+8
						self.canvas.create_arc(x, y, x+22, y+22, start=180, extent=270, style=ARC)
						self.canvas.create_text(x+8, y, text=str("◄"))
					else:
						x1=self.posicion[i][0]+8
						y1=self.posicion[i][1]+8
						x2=self.posicion[j][0]+8
						y2=self.posicion[j][1]+8
						self.canvas.create_line(x1, y1, x2, y2, arrow=LAST)
		self.canvas.pack()

	def p_arista(self):
		arista = tkinter.simpledialog.askstring("Grafo", "Ingresa una arista:")
		if not arista:
			return
		else:
			self.agregar_arista(arista)
			return

	def p_agregar(self):
		desde = tkinter.simpledialog.askstring("Grafo", "Desde:")
		if (desde==None):
			return
		hasta = tkinter.simpledialog.askstring("Grafo", "Hasta:")
		if (hasta==None):
			return
		self.agregar_relacion(desde,hasta)
		return

	def p_eliminar(self):
		desde = tkinter.simpledialog.askstring("Grafo", "Desde:")
		if (desde==None):
			return
		hasta = tkinter.simpledialog.askstring("Grafo", "Hasta:")
		if (hasta==None):
			return
		self.eliminar_relacion(desde,hasta)
		return

	def agregar_arista(self,arista):
		"""Agregar una arista al conjunto"""

		for j in range(len(self.conjunto)):
			if (self.conjunto[j]==arista):
				tkinter.messagebox.showerror("Error", "Ya se ha creado esta arista")
				return
		self.conjunto.append(arista)
		self.matriz.append([0])
		for i in range(len(self.conjunto)-1):
			self.matriz[i].append(0)
			self.matriz[len(self.conjunto)-1].append(0)
		x = tkinter.simpledialog.askinteger("Grafo", "Posicion X positiva:")
		while (x==None):
			x = tkinter.simpledialog.askinteger("Grafo", "Posicion X positiva:")
		y = tkinter.simpledialog.askinteger("Grafo", "Posicion Y negativa:")
		while (y==None):
			x = tkinter.simpledialog.askinteger("Grafo", "Posicion Y negativa:")
		self.posicion.append([x,y])

	def mostrar_matriz(self):
		"""Muestra la matriz"""

		if len(self.conjunto)==1:
			print("["+str(matriz[0][0])+"]")
		else:
			for i in range(len(self.conjunto)):
				for j in range(len(self.conjunto)):
					if j==0:
						print("[ "+str(self.matriz[i][j]),end=" ")
					elif j==len(self.conjunto)-1:
						print(str(self.matriz[i][j])+" ]",end="")
					else:
						print(str(self.matriz[i][j]),end=" ")
				print()

	def agregar_relacion(self, desde, hacia):
		"""Relaciona a con b"""

		indice1=0
		indice2=0
		a=False
		b=False
		for i in range(len(self.conjunto)):
			if self.conjunto[i]==desde:
				indice1=i
				a=True
			if self.conjunto[i]==hacia:
				indice2=i
				b=True
		if a==True and b==True and self.matriz[indice1][indice2]!=1:	
			self.matriz[indice1][indice2]=1
		else:
			tkinter.messagebox.showerror("Error", "Ya se ha creado esta relacion")
			return

	def eliminar_relacion(self, desde, hasta):
		"""Elimina la relacion de a con b"""

		indice1=0
		indice2=0
		a=False
		b=False
		for i in range(len(self.conjunto)):
			if self.conjunto[i]==desde:
				indice1=i
				a=True
			if self.conjunto[i]==hasta:
				indice2=i
				b=True
		if a==True and b==True and self.matriz[indice1][indice2]!=0:	
			self.matriz[indice1][indice2]=0
		else:
			return

	def obtener_matriz(self):
		return self.matriz

	def obtener_len_matriz(self):
		return len(self.conjunto)
