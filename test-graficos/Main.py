#!/bin/python

import pygame, time
import pygame.gfxdraw as dibujar
from pygame.locals import *
import os

class Color:
	WHITE = 255, 255, 255
	BLACK = 0, 0, 0
	GRAY = 191,191,191
	YELLOW = 255,255, 0

class VentanaPrincipal :

	width = 0
	height = 0
	screen = None

	def __init__( self, width=1100, height=800, title='Armonizador') :
		"""
		"""
		pygame.init()

		self.width, self.height = width, height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.screen.fill(Color.WHITE)

		pygame.display.set_caption(title)
		
		
		self.draw()
		self.draw_claves()
		self.draw_compases()
		#self.draw_cifra_compas()
		self.draw_nombre_lineas()
		self.draw_armadura()
		
		pygame.display.flip()
		
	def handler( self, handler_method=None ) :
		"""
		"""
		clock = pygame.time.Clock()
		quit = False

		espaciado_x = 50.0
		espaciado_y = 4

		while not quit:
			
			for event in pygame.event.get():

				mouse_x, mouse_y = pygame.mouse.get_pos()
				mouse_y -= 2
				mouse_x += 0.5
				#print "Mouse : " +str(mouse_x)+ ", "+ str(mouse_y)
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

	def draw( self ):
		"""
		Mbaez : 13/07/2011
		"""
		space = 8
		self.lineas = []
		#Se anhaden las lineas adicionales de arriba
		for i in range (1,4) :
			if i%2 != 0 :
				rect = self.draw_line(50, 50 + space * i, Color.YELLOW)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.GRAY)

			self.lineas.append(rect)
		
		for i in range (4,14) :
			if i%2 == 0 :
				rect = self.draw_line(50, 50 + space * i, Color.BLACK)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.YELLOW)

			self.lineas.append(rect)

		for i in range (14,18) :
			if i%2 != 0 :
				rect = self.draw_line(50, 50 + space * i, Color.YELLOW)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.GRAY)

			self.lineas.append(rect)

		for i in range (18,23) :
			if i%2 != 0 :
				rect = self.draw_line(50, 50 + space * i, Color.YELLOW)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.GRAY)

			self.lineas.append(rect)
		
		print self.lineas
		for i in range (23,33) :
			if i%2 == 0 :
				rect = self.draw_line(50, 50 + space * i, Color.BLACK)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.YELLOW)

			self.lineas.append(rect)

		for i in range (33,37) :
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
		dif_1 = ptox - int(ptox)
		dif_2 = ptoy - int(ptoy)
		
		if dif_1 > 0.5 :
			ptox = int(ptox) + 1
		else :
			ptox = int(ptox)
		
		if dif_2 > 0.5 :
			ptoy = int(ptoy) + 1
		else :
			ptoy = int(ptoy)

		dibujar.aaellipse(self.screen, ptox, ptoy, 10, 7, borde )
		dibujar.aaellipse(self.screen, ptox+1, ptoy+1, 8, 5, fondo)
		
		dibujar.vline(self.screen, ptox+11, ptoy-30, ptoy+5, \
															Color.BLACK )
		
	def draw_claves( self ) :
		"""
		"""
		#dibuja la clave de Sol
		fullname = os.path.join('', 'clave_de_sol.gif')
		image = pygame.image.load(fullname)
		image = pygame.transform.scale(image, (45, 95))
		image = image.convert() # Set the right pixel depth
		colorkey = image.get_at((0,0)) # Get pixel for transparent colour
		image.set_colorkey(colorkey, RLEACCEL) # Set transparent colour
		imagerect = image.get_rect() # Get the rect of the image
		screenrect = self.screen.get_rect()
		imagerect.centerx, imagerect.centery = 80, 120
		
		self.screen.blit(image, imagerect)
		
		#dibuja la clave de Fa
		fullname = os.path.join('', 'ClaveFa.gif')
		image = pygame.image.load(fullname)
		image = pygame.transform.scale(image, (95, 96))
		image = image.convert() # Set the right pixel depth
		colorkey = image.get_at((0,0)) # Get pixel for transparent colour
		image.set_colorkey(colorkey, RLEACCEL) # Set transparent colour
		imagerect = image.get_rect() # Get the rect of the image
		screenrect = self.screen.get_rect()
		imagerect.centerx, imagerect.centery = 80, 269
		
		self.screen.blit(image, imagerect)
		
		#dibuja el corchete
		fullname = os.path.join('', 'corchete.gif')
		image = pygame.image.load(fullname)
		image = pygame.transform.scale(image, (30, 230))
		image = image.convert() # Set the right pixel depth
		colorkey = image.get_at((0,0)) # Get pixel for transparent colour
		image.set_colorkey(colorkey, RLEACCEL) # Set transparent colour
		imagerect = image.get_rect() # Get the rect of the image
		screenrect = self.screen.get_rect()
		imagerect.centerx, imagerect.centery = 25, 194
		
		self.screen.blit(image, imagerect)
	
	def draw_cifra_compas( self ) :
		"""
		Dibuja 4-4 o 6-4 segun el usuario elija
		"""
		
		#dibuja la cifra de compas
		fullname = os.path.join('', '4-4.png')
		image = pygame.image.load(fullname)
		image = pygame.transform.scale(image, (110, 80))
		image = image.convert() # Set the right pixel depth
		colorkey = image.get_at((0,0)) # Get pixel for transparent colour
		image.set_colorkey(colorkey, RLEACCEL) # Set transparent colour
		imagerect = image.get_rect() # Get the rect of the image
		screenrect = self.screen.get_rect()
		imagerect.centerx, imagerect.centery = 230, 120
		
		self.screen.blit(image, imagerect)
		
		#dibuja la cifra de compas
		imagerect.centerx, imagerect.centery = 230, 280
		
		self.screen.blit(image, imagerect)

	def draw_compases( self ) :
		"""
		Dibuja las lineas divisorias de los compases
		"""
		#posicion del eje x del primer compas
		pos_x = 420
		#tamanho de la barra del compas
		tam = 64
		pos_y = 82
		#desplazamiento hacia abajo
		desp_y = 160
		
		for i in range(3) :
			
			dibujar.vline(self.screen, pos_x + i*210, pos_y, pos_y+tam, \
															Color.BLACK )
			dibujar.vline(self.screen, pos_x + i*210, pos_y + desp_y, pos_y  \
											+ desp_y + tam, Color.BLACK )
		
		#raya final
		dibujar.vline(self.screen, pos_x + 3*210, pos_y, pos_y+tam, \
															Color.BLACK )
		dibujar.vline(self.screen, pos_x + 3*210, pos_y + desp_y, pos_y  \
											+ desp_y + tam, Color.BLACK )
		
	def draw_cursor( self ) :
		"""
		"""
		mouse_image = pygame.image.load('blanca.gif').convert_alpha()

		mouse_pos = pygame.mouse.get_pos()
		self.screen.blit(mouse_image, mouse_pos)
		pygame.display.update()

	def draw_nombre_lineas( self ) :
		"""
		Metodo para mostrar el nombre de las notas
		"""
		
		font = pygame.font.Font(None, 15)
		
		notas = ['do', 'si', 'la', 'sol', 'fa', 'mi', 're']
		alturas = [5, 4, 3, 2, 1] 
		
		total_notas = []
		
		#creamos la lista de notas con su altura
		for i in range(5) :
			 for j in range(7) :
				nombre = str(notas[j])+str(alturas[i])
				total_notas.append( nombre )
		
		total_notas.append( 'do1' )
		
		for i in range(35) :
			
			nombre = total_notas[i+1]
			# Render the text
			text = font.render(nombre, True, (0, 0, 0), \
													(255, 255, 255, 255))
			
			textRect = text.get_rect()
			
			# posicion
			textRect.centerx = 1070
			textRect.centery = 58 + i*8
			
			self.screen.blit(text, textRect)

	def draw_armadura( self ) :
		"""
		Metodo que dibuja la armadura de clave segun haya seleccionado 
		el usuario
		"""
		orden_sostenidos = d = {"do": 0,
								"sol": 1,
								"re": 2,
								"la": 3,
								"mi": 4,
								"si": 5,
								"fa#": 6,
								"do#": 7}
		
		fullname = os.path.join('', 'sostenido.gif')
		image = pygame.image.load(fullname)
		image = pygame.transform.scale(image, (35, 60))
		image = image.convert() # Set the right pixel depth
		colorkey = image.get_at((0,0)) # Get pixel for transparent colour
		image.set_colorkey(colorkey, RLEACCEL) # Set transparent colour
		imagerect = image.get_rect() # Get the rect of the image
		screenrect = self.screen.get_rect()
		
		#distancia entre claves
		dist = 175
		#corrimiento en X
		desp_x = 9
		
		for i in range(orden_sostenidos["la"]) :
			
			if i == 0 :
				imagerect.centerx, imagerect.centery = 105+desp_x, 83
			
			elif i == 1 :
				imagerect.centerx, imagerect.centery = 118+desp_x, 105
			
			elif i == 2 :
				imagerect.centerx, imagerect.centery = 131+desp_x, 75
			
			elif i == 3 :
				imagerect.centerx, imagerect.centery = 144+desp_x, 98
			
			elif i == 4 :
				imagerect.centerx, imagerect.centery = 157+desp_x, 125
			
			elif i == 5 :
				imagerect.centerx, imagerect.centery = 170+desp_x, 91
			
			elif i == 6 :
				imagerect.centerx, imagerect.centery = 183+desp_x, 114
			
			self.screen.blit(image, imagerect)
			
			#armadura para la clave de Fa
			if i == 0 :
				imagerect.centerx, imagerect.centery = 105+desp_x, 83+dist
			
			elif i == 1 :
				imagerect.centerx, imagerect.centery = 118+desp_x, 105+dist
			
			elif i == 2 :
				imagerect.centerx, imagerect.centery = 131+desp_x, 75+dist
			
			elif i == 3 :
				imagerect.centerx, imagerect.centery = 144+desp_x, 98+dist
			
			elif i == 4 :
				imagerect.centerx, imagerect.centery = 157+desp_x, 125+dist
			
			elif i == 5 :
				imagerect.centerx, imagerect.centery = 170+desp_x, 91+dist
			
			elif i == 6 :
				imagerect.centerx, imagerect.centery = 183+desp_x, 114+dist
			
			self.screen.blit(image, imagerect)

if __name__ == "__main__" :
	
	ventana = VentanaPrincipal()
	ventana.handler()
