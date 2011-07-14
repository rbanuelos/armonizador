#!/bin/python

import pygame, time

class Color:
	WHITE = 255, 255, 255
	BLACK = 0, 0, 0
	GRAY = 191,191,191
	YELLOW = 255,255, 0

class VentanaPrincipal :

	width = 0
	height = 0
	screen = None

	def __init__ (self,width=600 , height=300, title='Pyntagrama'):
		"""
		"""
		pygame.init()

		self.width, self.height = width, height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.screen.fill(Color.WHITE)

		pygame.display.set_caption(title)

	def handler (self, handler_method=None):
		"""
		"""
		clock = pygame.time.Clock()
		quit = False

		espaciado_x = 50.0
		espaciado_y = 4

		while not quit:
			for event in pygame.event.get():

				mouse_x, mouse_y = pygame.mouse.get_pos()
				mouse_y -= 6
				mouse_x += 1
				print "Mouse : " +str(mouse_x)+ ", "+ str(mouse_y)
				if event.type == pygame.QUIT:
					quit = True
					pygame.quit()

				elif event.type == 5: #Cuando hace click
					"""
					Mbaez : 13/07/2011
					Si se hizo click se verifica cada linea del pentagrama
					para saber donde se debe anhadir la figura
					"""
					index = 0
					for linea in self.lineas :
						index += 1
						linea_y = linea.y - 8

						__linea = pygame.Rect(linea.x, linea_y,501,7)
						"""
						Mbaez : 13/07/2011
						Se obtiene el centro de la linea, esto es para que cada
						figura se dibuje en el centro de la linea
						"""
						print str(index)+ " " +str(linea_y)+" "+str(mouse_y)
						#if abs(mouse_y  - linea_y) <= espaciado_y :
						if __linea.collidepoint(mouse_x, mouse_y) :
							print "len:"+str(len(self.lineas))
							if index > 17:
								print "index"  +str(index)
								break
							"""
							Mbaez : 13/07/2011
							Se controla si se supera el unbral definido por
							espaciado_y para saber a que linea pertenece la
							figura
							"""
							int_x = int(mouse_x/espaciado_x)
							_x = mouse_x/espaciado_x
							"""
							Mbaez : 13/07/2011
							Las figuras deben estar posicionada en un especie
							de grilla, por ese motivo se define un espaciado
							entre las figuras (espaciado_x), se verifica a que
							columna de la grilla deberia pertenecer la figura.
							"""
							print "mouse_x: " +str(mouse_x) +"\tint : " + str(int_x) + "\t x:" + str(_x)
							if (int_x+0.5 < _x):
								"""
								Mbaez : 13/07/2011
								Si se supera la mitad, la figura pertenece a la
								siguente columna de la grilla
								"""
								int_x += 1

							pos_x = espaciado_x*int_x
							"""
							Mbaez : 13/07/2011
							se establece la posicion de la figura como el centro
							de la grilla
							"""
							__x, __y =__linea.center
							self.draw_blanca(pos_x, __y)

							pygame.display.flip()
							break

				#handler_method()

			clock.tick(50)

	def draw(self):
		"""
		Mbaez : 13/07/2011
		"""
		space = 8
		self.lineas = []
		#Se anhaden las lineas adicionales de arriba
		for i in range (1,4) :
			if i%2 != 0 :
				rect = self.draw_line(50, 50 + space * i, Color.GRAY)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.YELLOW)

			self.lineas.append(rect)
		print self.lineas
		for i in range (4,14) :
			if i%2 == 0 :
				rect = self.draw_line(50, 50 + space * i, Color.BLACK)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.GRAY)

			self.lineas.append(rect)

		for i in range (14,18) :
			if i%2 != 0 :
				rect = self.draw_line(50, 50 + space * i, Color.GRAY)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.YELLOW)

			self.lineas.append(rect)


		pygame.display.flip()

	def draw_line (self, ptox, ptoy, color):
		"""
		Mbaez : 13/07/2011
		Dibuja una linea del pentagrama

		@type  ptox : Integer
		@param ptox : Coordenada X donde se va dibujar la linea

		@type  ptoy : Integer
		@param ptoy : Coordenada Y donde se va dibujar la linea

		@type  color : Lista
		@param color : Representa el color que va tener la linea

		@return Rect: La recta que contiene los puntos de la linea
		"""
		puntos = [(ptox,ptoy), (ptox+self.width -100,ptoy)]

		rect = pygame.Rect(pygame.draw.\
							lines(self.screen, Color.WHITE, False, puntos, 7))
		pygame.Rect(pygame.draw.\
							lines(self.screen, color, False, puntos, 1))
		return rect

	def draw_blanca(self, ptox, ptoy, borde=Color.BLACK, fondo=Color.WHITE,
					radio=7):
		"""
		Mbaez : 13/07/2011
		Dibuja una blanca
		"""
		pygame.draw.ellipse(self.screen, borde,(ptox,ptoy,21, 16))
		return pygame.draw.ellipse(self.screen, fondo,(ptox+1,ptoy+1,19, 14))

if __name__ == "__main__" :
	ventana = VentanaPrincipal()
	ventana.draw()

	ventana.handler()
