from tkinter import*

class Grafo:
	"""Clase de grafos"""

	def __init__(self, ventana):
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
		opciones.add_command(label="Salir", command=ventana.quit)
		opciones.add_separator()
		opciones.add_command(label="Mostrar Matriz", command=self.mostrar_matriz)

		grafo=Button(ventana, text="Mostrar Grafo", command=self.dibujar)
		grafo.pack(side=BOTTOM)

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
						y1=self.posicion[i][1]+8
						y1=self.posicion[i][1]+8
						x1=self.posicion[i][0]+8
						y1=self.posicion[i][1]+8
						x2=self.posicion[j][0]+8
						y2=self.posicion[j][1]+8
						self.canvas.create_line(x1, y1, x2, y2, arrow=LAST)
		self.canvas.pack()

	def p_arista(self):
		arista=input("Arista? ")
		self.agregar_arista(arista)
		return

	def p_agregar(self):
		desde=input("Desde? ")
		hasta=input("Hasta? ")
		self.agregar_relacion(desde,hasta)
		return

	def p_eliminar(self):
		desde=input("Desde? ")
		hasta=input("Hasta? ")
		self.eliminar_relacion(desde,hasta)
		return

	def agregar_arista(self,arista):
		"""Agregar una arista al conjunto"""

		self.conjunto.append(arista)
		self.matriz.append([0])
		for i in range(len(self.conjunto)-1):
			self.matriz[i].append(0)
			self.matriz[len(self.conjunto)-1].append(0)
		x=int(input("Posicion x positiva: "))
		y=int(input("Posicion y negativa "))
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