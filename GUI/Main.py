#!/bin/python

import os
import sys

path = os.path.join(os.path.abspath(__file__))

path = os.path.abspath(os.path.join(path, '..'))

root_directory = os.path.abspath(os.path.join(path, '..'))

controller_directory = os.path.abspath( \
							os.path.join(root_directory, 'controller'))

sys.path.append(controller_directory)

from controller import *

import pygame, time
import pygame.gfxdraw as dibujar
from pygame.locals import *
import os

#nombre de las lineas 64 en total
nombres = ['sol4', 'fa4', 'mi4','re4', 'do4', 
			'si3', 'la3', 'sol3', 'fa3', 'mi3','re3', 'do3',
			'si2', 'la2', 'sol2',
			
			'sol3', 'fa3', 'mi3','re3', 'do3',
			'si2', 'la2', 'sol2','fa2', 'mi2','re2', 'do2',
			'si1', 'la1', 'sol1', 'fa1', 'mi1',
			
			'sol4', 'fa4', 'mi4','re4', 'do4', 
			'si3', 'la3', 'sol3', 'fa3', 'mi3','re3', 'do3',
			'si2', 'la2', 'sol2',
			
			'sol3', 'fa3', 'mi3','re3', 'do3',
			'si2', 'la2', 'sol2','fa2', 'mi2','re2', 'do2',
			'si1', 'la1', 'sol1', 'fa1', 'mi1'
			]

class Color:
	WHITE = 255, 255, 255
	BLACK = 0, 0, 0
	GRAY = 191,191,191
	YELLOW = 255,255, 0
	BLUE = 255, 0, 255 

class VentanaPrincipal :

	width = 0
	height = 0
	screen = None
	
	#grillas ocupadas por alguna nota
	grilla_ocupada_arriba = [	False, False, 
								False, False,
								False, False,
								False, False
							]
							
	grilla_ocupada_abajo = [	False, False, 
								False, False,
								False, False,
								False, False
							]
						
	#lugares disponibles dentro del pentagrama en este caso 4/4 2 blancas
	#por compas
	grillas_arriba =	[	250, 350, 
							470, 570,
							690, 790,
							900, 1000
						]
				
	grillas_abajo =	[	250, 350, 
						470, 570,
						690, 790,
						900
					]
	
	#en el caso de redibujar la pantalla se mantiene un registro de
	#todas las notas que se dibujaron antes
	# nota = tupla(x, y) , plica 
	notas = []
	
	#bajos del ejercicio
	bajos_dados = [	None, None,
					None, None,
					None, None,
					None, None,
					None, None,
					None, None,
					None, None,
					None
					]
	
	def __init__( self, width=1100, height=800, title='Armonizador') :
		"""
		"""
		pygame.init()

		self.width, self.height = width, height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.screen.fill(Color.WHITE)

		pygame.display.set_caption(title)
		
		self.draw_fondo()
		self.draw()
		#self.draw_fondo()
		#self.draw_lineas_negras()
		self.draw_claves()
		self.draw_compases()
		#self.draw_nombre_lineas()
		self.draw_armadura_sostenido()
		self.draw_boton_armonizar()
		
		
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
				
				#resaltar el boton cuando el mouse esta encima
				if self.boton.collidepoint(mouse_x, mouse_y) :
					self.set_highligthed()
					pygame.display.flip()
					
				else :
					self.draw_boton_armonizar()
					pygame.display.flip()
				
				#evento clic en salir
				if event.type == pygame.QUIT:
					quit = True
					pygame.quit()
				
				#evento click sobre la pantalla
				elif event.type == 5: 
					
					print str(mouse_x) +' - '+ str(mouse_y)
					
					#evento que dibuja sobre la pantalla
					self.clic_handler_draw(mouse_x, mouse_y)
					
					#evento cuando se da clic sobre el boton armonizar
					self.clic_handler_boton(mouse_x, mouse_y)

			clock.tick(50)

	def clic_handler_draw( self, mouse_x, mouse_y ) :
		"""
		cada clic en el pentagrama es atendido por este metodo
		"""
		
		index = 0
		for linea in self.lineas :
			
			index += 1
			linea_y = linea.y 

			__linea = pygame.Rect(linea.x, linea_y,1100,7)
			
			if __linea.collidepoint( mouse_x, mouse_y ) :
				
				# se verifica si estamos en el primer endecagrama o el 
				# 2do
				if mouse_y >= 240 and mouse_y <= 336 :
					grilla = 'arriba'
				
				elif  mouse_y >= 576 and mouse_y <= 673 :
					grilla = 'abajo'
				
				else :
					break
				 
				int_x = int(mouse_x)
				
				#se obtiene la posicion en el eje X de la 
				#figura
				pos_x = self.get_grilla( int_x, grilla )

				#se verifica que sea una posicion valida 
				#dentro de la pantalla
				if pos_x != None :
					
					__x, __y =__linea.center
					
					if grilla == 'arriba' :
						pos_grilla = self.grillas_arriba.index( pos_x )
						
						#guardar el nombre de la linea seleccinoada
						self.bajos_dados[pos_grilla] = \
										nombres[self.lineas.index(linea)]
										
						#se verifica que este libre
						if not self.grilla_ocupada_arriba[pos_grilla] :
							self.draw_blanca(pos_x, __y)
							self.grilla_ocupada_arriba[pos_grilla] = True
							#guardar nota dibujada
							self.notas.append([(pos_x, __y), 'abajo'])
							
						else : 
							#reemplazar la figura
							self.reemplazar_figura( pos_x, __y, 'abajo')
							#dibujar todo de vuelta
							self.re_draw()
					else :
						pos_grilla = self.grillas_abajo.index( pos_x )
						
						#guardar el nombre de la linea seleccinoada
						self.bajos_dados[pos_grilla+8] = \
										nombres[self.lineas.index(linea)]
										
						#se verifica que este libre
						if not self.grilla_ocupada_abajo[pos_grilla] :
							self.draw_blanca(pos_x, __y)
							self.grilla_ocupada_abajo[pos_grilla] = True
							#guardar nota dibujada
							self.notas.append([(pos_x, __y), 'abajo'])
						
						else : 
							#reemplazar la figura
							self.reemplazar_figura( pos_x, __y, 'abajo')
							#dibujar todo de vuelta
							self.re_draw()
							
				pygame.display.flip()
				break
		return

	def clic_handler_boton( self, mouse_x, mouse_y ) :
		"""
		Se verifica que el click hecho por el usuario este dentro del 
		boton "Armonizar"
		"""
		self.re_draw()
		resultados = []
		cifrados = []
		
		if self.boton.collidepoint(mouse_x, mouse_y) :
			
			#se le llama al controlador
			resultados, cifrados_americanos, cifrados  = \
						controller.estado_actual( self.bajos_dados, "la" )
		
		for index in range(len(resultados)) : 
			
			if resultados[index] == '' :
				break
				
			#se dibujan los resultados
			self.draw_acorde( resultados[index][0], resultados[index][1], 
											resultados[index][2], index )
			#se dibujan los cifrados
			self.draw_cifrado( cifrados_americanos[index], cifrados[index] \
																,index )
			
		return
		
	def draw( self ) :
		"""
		Mbaez : 13/07/2011
		"""
		space = 8
		self.lineas = []
		
		######### 1er Endecagrama clave de Sol###########
		for i in range (3,4) :
			if i%2 != 0 :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)

			self.lineas.append(rect)
			
		for i in range (4,14) :
			if i%2 == 0 :
				rect = self.draw_line(50, 50 + space * i, Color.BLACK)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)

			self.lineas.append(rect)

		for i in range (14,18) :
			if i%2 != 0 :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)

			self.lineas.append(rect)
		
		######### 1er Endecagrama clave de Fa###########
		for i in range (20,25) :
			if i%2 != 0 :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)
				
			self.lineas.append(rect)
		
		for i in range (25,35) :
			if i%2 == 0 :
				rect = self.draw_line(50, 50 + space * i, Color.BLACK)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)

			self.lineas.append(rect)

		for i in range (35,37) :
			if i%2 == 0 :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)
			
			self.lineas.append(rect)
			
		######### 2do Endecagrama clave de Sol###########
		for i in range (45,46) :
			if i%2 != 0 :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)
				
			self.lineas.append(rect)
			
		for i in range (46,56) :
			if i%2 == 0 :
				rect = self.draw_line(50, 50 + space * i, Color.BLACK)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)

			self.lineas.append(rect)

		for i in range (56,60) :
			if i%2 != 0 :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)

			self.lineas.append(rect)
		
		######### 2do Endecagrama clave de Fa###########
		for i in range (62,67) :
			if i%2 != 0 :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)
				
			self.lineas.append(rect)
		
		for i in range (67,77) :
			if i%2 == 0 :
				rect = self.draw_line(50, 50 + space * i, Color.BLACK)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)

			self.lineas.append(rect)

		for i in range (77,79) :
			if i%2 == 0 :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)
				
			else :
				rect = self.draw_line(50, 50 + space * i, Color.WHITE)

			self.lineas.append(rect)
		
		pygame.display.flip()
	
	def draw_lineas_negras( self ) :
		"""
		dibuja las lineas negras de los pentagramas
		"""
		
		space = 8
		self.lineas = []
		
		for i in range (4,14) :
			if i%2 == 0 :
				rect = self.draw_line_negra(50, 50 + space * i, Color.BLACK)
				
				
		for i in range (25,35) :
			if i%2 == 0 :
				rect = self.draw_line_negra(50, 50 + space * i, Color.BLACK)
			
		for i in range (46,56) :
			if i%2 == 0 :
				rect = self.draw_line_negra(50, 50 + space * i, Color.BLACK)
		
		for i in range (67,77) :
			if i%2 == 0 :
				rect = self.draw_line_negra(50, 50 + space * i, Color.BLACK)

		pygame.display.flip()


	def draw_fondo( self ) :
		"""
		dibuja el fondo de la aplicacion
		"""
		
		#dibuja la clave de Sol
		fullname = os.path.join('img', 'White-Board.jpg')
		image = pygame.image.load(fullname)
		image = pygame.transform.scale(image, (1100, 800))
		#~ image = image.convert() # Set the right pixel depth
		#~ colorkey = image.get_at((0,0)) # Get pixel for transparent colour
		#~ image.set_colorkey(colorkey, RLEACCEL) # Set transparent colour
		#~ imagerect = image.get_rect() # Get the rect of the image
		#~ screenrect = self.screen.get_rect()
		#~ imagerect.centerx, imagerect.centery = 80, 120 + desp
		
		self.screen.blit(image, (0, 0))

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

	def draw_line_negra( self, ptox, ptoy, color ):
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
	
		pygame.Rect(pygame.draw.\
							lines(self.screen, color, False, puntos, 1))

	def draw_blanca(self, ptox, ptoy, borde=Color.BLACK, fondo=Color.WHITE,
															plica='abajo'):
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
							
		if plica == 'arriba' :
			
			fullname = os.path.join('img', 'half note up.gif')
			image = pygame.image.load(fullname)
			image = pygame.transform.scale(image, (30, 52))
			image = image.convert() # Set the right pixel depth
			colorkey = image.get_at((0,0)) # Get pixel for transparent colour
			image.set_colorkey(colorkey, RLEACCEL) # Set transparent colour
			imagerect = image.get_rect() # Get the rect of the image
			screenrect = self.screen.get_rect()
			imagerect.centerx, imagerect.centery = ptox, ptoy-16
			
		else :
			fullname = os.path.join('img', 'half note down.gif')
			image = pygame.image.load(fullname)
			image = pygame.transform.scale(image, (30, 52))
			image = image.convert() # Set the right pixel depth
			colorkey = image.get_at((0,0)) # Get pixel for transparent colour
			image.set_colorkey(colorkey, RLEACCEL) # Set transparent colour
			imagerect = image.get_rect() # Get the rect of the image
			screenrect = self.screen.get_rect()
			imagerect.centerx, imagerect.centery = ptox, ptoy+16
		
		self.screen.blit(image, imagerect)
		
		self.draw_lineas_adicionales( ptox, ptoy )
		
		pygame.display.flip()
	
	def draw_lineas_adicionales( self, pos_x, pos_y, cantidad=0 ) :
		"""
		Metodo para agregar lineas adicionales segun la posicion de la 
		nota dibujada
		"""
		
		endecagrama = 0
		
		if pos_y == 162 :
			cantidad = 1 
			dif = 0
		
		if pos_y == 170 :
			cantidad = 1
			dif = 8
		
		if pos_y == 178 :
			cantidad = 2
			dif = 16
		
		if pos_y == 186 :
			cantidad = 2
			dif = 24
		
		if pos_y == 210 :
			cantidad = 3 
			dif = 0
		
		if pos_y == 218 :
			cantidad = 2
			dif = -8
		
		if pos_y == 226 :
			cantidad = 2
			dif = 0
		
		if pos_y == 234 :
			cantidad = 1
			dif = -8
		
		if pos_y == 242 :
			cantidad = 1
			dif = 0
		
		if pos_y == 338 :
			cantidad = 1
			dif = 0
		
		
		#pentagrama de abajo
		distancia_entre_claves = 336
		if pos_y == 162 + distancia_entre_claves :
			cantidad = 1 
			dif = 0
			endecagrama = 336
			
		if pos_y == 170 + distancia_entre_claves :
			cantidad = 1
			dif = 8
			endecagrama = 336 
			
		if pos_y == 178 + distancia_entre_claves :
			cantidad = 2
			dif = 16
			endecagrama = 336
		
		if pos_y == 186 + distancia_entre_claves :
			cantidad = 2
			dif = 24
			endecagrama = 336
		
		if pos_y == 210 + distancia_entre_claves :
			cantidad = 3 
			dif = 0
			endecagrama = 336
		
		if pos_y == 218 + distancia_entre_claves :
			cantidad = 2
			dif = -8
			endecagrama = 336
		
		if pos_y == 226 + distancia_entre_claves :
			cantidad = 2
			dif = 0
			endecagrama = 336
		
		if pos_y == 234 + distancia_entre_claves :
			cantidad = 1
			dif = -8
			endecagrama = 336
			
		if pos_y == 242 + distancia_entre_claves :
			cantidad = 1
			dif = 0
			endecagrama = 336
			
		if pos_y == 338 + distancia_entre_claves :
			cantidad = 1
			dif = 0
			endecagrama = 336
			
		for index in range(cantidad) :
			desp = index*16-dif
			puntos = [(pos_x-16, pos_y+desp), \
									(pos_x+17, pos_y+desp)]
			pygame.Rect(pygame.draw.\
					lines(self.screen, Color.BLACK, False, puntos, 1))

	def draw_claves( self ) :
		"""
		"""
		for desp in (0, 336) :
			#dibuja la clave de Sol
			fullname = os.path.join('img', 'clave_de_sol.gif')
			image = pygame.image.load(fullname)
			image = pygame.transform.scale(image, (45, 95))
			image = image.convert() # Set the right pixel depth
			colorkey = image.get_at((0,0)) # Get pixel for transparent colour
			image.set_colorkey(colorkey, RLEACCEL) # Set transparent colour
			imagerect = image.get_rect() # Get the rect of the image
			screenrect = self.screen.get_rect()
			imagerect.centerx, imagerect.centery = 80, 120 + desp
			
			self.screen.blit(image, imagerect)
			
			#dibuja la clave de Fa
			fullname = os.path.join('img', 'ClaveFa.gif')
			image = pygame.image.load(fullname)
			image = pygame.transform.scale(image, (95, 96))
			image = image.convert() # Set the right pixel depth
			colorkey = image.get_at((0,0)) # Get pixel for transparent colour
			image.set_colorkey(colorkey, RLEACCEL) # Set transparent colour
			imagerect = image.get_rect() # Get the rect of the image
			screenrect = self.screen.get_rect()
			imagerect.centerx, imagerect.centery = 80, 284 + desp
			
			self.screen.blit(image, imagerect)
			
			#dibuja el corchete
			fullname = os.path.join('img', 'corchete2.gif')
			image = pygame.image.load(fullname)
			#image = pygame.transform.scale(image, (30, 260))
			image = pygame.transform.scale(image, (120, 600))
			image = image.convert() # Set the right pixel depth
			colorkey = image.get_at((0,0)) # Get pixel for transparent colour
			image.set_colorkey(colorkey, RLEACCEL) # Set transparent colour
			imagerect = image.get_rect() # Get the rect of the image
			screenrect = self.screen.get_rect()
			#imagerect.centerx, imagerect.centery = 25, 200 + desp
			imagerect.centerx, imagerect.centery = 40, 120 + desp
			
			self.screen.blit(image, imagerect)
	
	def draw_cifra_compas( self ) :
		"""
		Dibuja 4-4 o 6-4 segun el usuario elija
		"""
		
		#dibuja la cifra de compas
		fullname = os.path.join('img', '4-4.png')
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
		desp_y = 176
		
		for i in range(4) :
			dibujar.vline(self.screen, pos_x + i*210, pos_y, pos_y  \
											+ desp_y + tam, Color.BLACK )
		
		pos_y = 418
		for i in range(3) :
			dibujar.vline(self.screen, pos_x + i*210, pos_y, pos_y  \
											+ desp_y + tam, Color.BLACK )
			
		#rayas finales
		dibujar.vline(self.screen, pos_x + 3*208, pos_y, pos_y  \
											+ desp_y + tam, Color.BLACK )
		
		for i in range(4) :
			dibujar.vline(self.screen, pos_x + 3*210+i, pos_y, pos_y  \
											+ desp_y + tam, Color.BLACK )

	def draw_cursor( self ) :
		"""
		"""
		
		CURSOR_DATA = (	"              XXX       ",
						"              X.X       ", 
						"              X.X       ", 
						"              X.X       ", 
						"              X.X       ", 
						"              X.X       ", 
						"              X.X       ", 
						"              X.X       ", 
						"              X.X       ", 
						"              X.X       ", 
						"              X.X       ", 
						"              X.X       ", 
						"              X.X       ", 
						"              X.X       ", 
						"            XXX.X       ", 
						"         XXX.. .X       ", 
						"       XX..    .X       ", 
						"      XX..     .X       ", 
						"     XX..      .X       ", 
						"     XX..      .X       ", 
						"      XX..    .XX       ", 
						"        XX.. .XXX       ", 
						"          XXXXX X       ",
						"                        ")
		
						
		cur = pygame.cursors.compile(CURSOR_DATA)
		cursorSize = (len(CURSOR_DATA), len(CURSOR_DATA[0]))
		hotspot = (0, len(CURSOR_DATA)-1)            
		pygame.mouse.set_cursor(cursorSize, hotspot, *cur)
		
		pygame.display.update()

	def draw_nombre_lineas( self ) :
		"""
		Metodo para mostrar el nombre de las notas
		"""
		
		font = pygame.font.Font(None, 15)
		
		for i in range(32) :
			
			nombre = nombres[i]
			# Render the text
			text = font.render(nombre, True, (0, 0, 0), \
													(255, 255, 255, 255))
			
			textRect = text.get_rect()
			
			# posicion
			if i < 15 :
				textRect.centerx = 1070
				textRect.centery = 74 + i*8
			else :
				nombre = nombres[i]
				# Render the text
				text = font.render(nombre, True, (0, 0, 0), \
													(255, 255, 255, 255))
				textRect.centerx = 1070
				textRect.centery = 74 + (i+2)*8 
			
			self.screen.blit(text, textRect)
			
			# posicion
			if i < 15 :
				textRect.centerx = 1070
				textRect.centery = 74 + i*8+336
			else :
				nombre = nombres[i]
				# Render the text
				text = font.render(nombre, True, (0, 0, 0), \
													(255, 255, 255, 255))
				textRect.centerx = 1070
				textRect.centery = 74 + (i+2)*8+336 
			
			self.screen.blit(text, textRect)
			
	def draw_armadura_sostenido( self ) :
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
		
		fullname = os.path.join('img', 'sostenido.gif')
		image = pygame.image.load(fullname)
		image = pygame.transform.scale(image, (35, 60))
		image = image.convert() # Set the right pixel depth
		colorkey = image.get_at((0,0)) # Get pixel for transparent colour
		image.set_colorkey(colorkey, RLEACCEL) # Set transparent colour
		imagerect = image.get_rect() # Get the rect of the image
		screenrect = self.screen.get_rect()
		
		#distancia entre claves
		dist = 192
		#corrimiento en X
		desp_x = 9
		
		for desp in (0, 336):
			for i in range(orden_sostenidos["la"]) :
				
				if i == 0 :
					imagerect.centerx, imagerect.centery = 105+desp_x, 83+desp
				
				elif i == 1 :
					imagerect.centerx, imagerect.centery = 118+desp_x, 105+desp
				
				elif i == 2 :
					imagerect.centerx, imagerect.centery = 131+desp_x, 75+desp
				
				elif i == 3 :
					imagerect.centerx, imagerect.centery = 144+desp_x, 98+desp
				
				elif i == 4 :
					imagerect.centerx, imagerect.centery = 157+desp_x, 125+desp
				
				elif i == 5 :
					imagerect.centerx, imagerect.centery = 170+desp_x, 91+desp
				
				elif i == 6 :
					imagerect.centerx, imagerect.centery = 183+desp_x, 114+desp
				
				self.screen.blit(image, imagerect)
				
				#armadura para la clave de Fa
				if i == 0 :
					imagerect.centerx, imagerect.centery = 105+desp_x, 83+dist+desp
				
				elif i == 1 :
					imagerect.centerx, imagerect.centery = 118+desp_x, 105+dist+desp
				
				elif i == 2 :
					imagerect.centerx, imagerect.centery = 131+desp_x, 75+dist+desp
				
				elif i == 3 :
					imagerect.centerx, imagerect.centery = 144+desp_x, 98+dist+desp
				
				elif i == 4 :
					imagerect.centerx, imagerect.centery = 157+desp_x, 125+dist+desp
				
				elif i == 5 :
					imagerect.centerx, imagerect.centery = 170+desp_x, 91+dist+desp
				
				elif i == 6 :
					imagerect.centerx, imagerect.centery = 183+desp_x, 114+dist+desp
				
				self.screen.blit(image, imagerect)

	def draw_armadura_bemol( self ) :
		"""
		Metodo que dibuja la armadura de clave segun haya seleccionado 
		el usuario
		"""
		orden_sostenidos = d = {"fa": 1,
								"sib": 2,
								"mib": 3,
								"lab": 4,
								"reb": 5,
								"solb": 6,
								"dob": 7}
		
		fullname = os.path.join('img', 'bemol.gif')
		image = pygame.image.load(fullname)
		image = pygame.transform.scale(image, (35, 60))
		image = image.convert() # Set the right pixel depth
		colorkey = image.get_at((0,0)) # Get pixel for transparent colour
		image.set_colorkey(colorkey, RLEACCEL) # Set transparent colour
		imagerect = image.get_rect() # Get the rect of the image
		screenrect = self.screen.get_rect()
		
		#distancia entre claves
		dist = 192
		#corrimiento en X
		desp_x = 9
		
		for desp in (0, 336) :
			for i in range(orden_sostenidos["reb"]) :
				
				if i == 0 :
					imagerect.centerx, imagerect.centery = 105+desp_x, 105+desp
				
				elif i == 1 :
					imagerect.centerx, imagerect.centery = 118+desp_x, 79+desp
				
				elif i == 2 :
					imagerect.centerx, imagerect.centery = 131+desp_x, 112+desp
				
				elif i == 3 :
					imagerect.centerx, imagerect.centery = 144+desp_x, 88+desp
				
				elif i == 4 :
					imagerect.centerx, imagerect.centery = 157+desp_x, 120+desp
				
				elif i == 5 :
					imagerect.centerx, imagerect.centery = 170+desp_x, 96+desp
				
				elif i == 6 :
					imagerect.centerx, imagerect.centery = 183+desp_x, 128+desp
				
				self.screen.blit(image, imagerect)
				
				#armadura para la clave de Fa
				if i == 0 :
					imagerect.centerx, imagerect.centery = 105+desp_x, 105+dist+desp
				
				elif i == 1 :
					imagerect.centerx, imagerect.centery = 118+desp_x, 79+dist+desp
				
				elif i == 2 :
					imagerect.centerx, imagerect.centery = 131+desp_x, 112+dist+desp
				
				elif i == 3 :
					imagerect.centerx, imagerect.centery = 144+desp_x, 88+dist+desp
				
				elif i == 4 :
					imagerect.centerx, imagerect.centery = 157+desp_x, 120+dist+desp
				
				elif i == 5 :
					imagerect.centerx, imagerect.centery = 170+desp_x, 96+dist+desp
				
				elif i == 6 :
					imagerect.centerx, imagerect.centery = 183+desp_x, 128+dist+desp
				
				self.screen.blit(image, imagerect)

	def draw_cifrado( self, string, string2, pos_grilla ) :
		"""
		Metodo para dibuajar en pantalla el cifrado de un acorde
		"""
		
		font = pygame.font.Font('Fette Engschrift.ttf', 20)
		# Render the text
		text = font.render(string2, True, (0, 0, 0))
		textRect = text.get_rect()
		
		if pos_grilla > 7 :
			pos_grilla -= 8
			#para que se desplace al endecagrama de abajo
			index_desp = 720
			index_desp_2 = 400
		else :
			index_desp = 360
			index_desp_2 = 40
		
		
		textRect.centerx = self.grillas_arriba[pos_grilla]
		textRect.centery = index_desp
		
		self.screen.blit(text, textRect)
		
		
		# Render the text
		text = font.render(string, True, (0, 0, 0))
		textRect = text.get_rect()
		
		textRect.centerx = self.grillas_arriba[pos_grilla]
		textRect.centery = index_desp_2
		
		self.screen.blit(text, textRect)
		
	def get_grilla( self, pos_x, pos_grilla ) :
		"""
		Metodo que retorna en que posicion dentro del compas debe ser 
		colocada la figura
		"""
		if pos_grilla == 'arriba' :
			for grilla in self.grillas_arriba :
				dif = abs(pos_x - grilla)
				
				if dif < 50 :
					return grilla
		
		else :
			for grilla in self.grillas_abajo :
				dif = abs(pos_x - grilla)
				
				if dif < 50 :
					return grilla
					
		return None
	
	def reemplazar_figura( self, x, y, plica ) :
		"""
		Metodo que dado un x e y reemplaza por el que ocupa su misma
		grilla
		"""
		distancia_de_clave = 96
		
		for nota in self.notas :
			if nota[0][0] == x :
				dif = abs(nota[0][1]-y)
				
				if dif < distancia_de_clave :
					self.notas.remove( nota )
		
		self.notas.append([(x, y), plica])
	
	def draw_boton_armonizar( self ) :
		"""
		Despliega en pantalla el boton que sirve para que la maquina 
		proceda a resolver el ejercicio de armonia
		"""
		
		font = pygame.font.Font('Fifties Regular.ttf', 70)
		# Render the text
		text = font.render("Armonizar", True, (0, 0, 0))
		textRect = text.get_rect()
		#posicion
		textRect.centerx = 900
		textRect.centery = 750
	
		self.screen.blit(text, textRect)
		
		self.boton = textRect

	def set_highligthed( self ) :
		"""
		resalta el boton de armonizar cuando el mouse esta encima
		"""
		
		font = pygame.font.Font('Fifties Regular.ttf', 70)
		# Render the text
		text = font.render("Armonizar", True, (255, 0, 0))
		textRect = text.get_rect()
		#posicion
		textRect.centerx = 900
		textRect.centery = 750
	
		self.screen.blit(text, textRect)
		
		self.boton = textRect
	
	def draw_acorde( self, soprano, contralto, tenor, pos_grilla ) :
		"""
		Recibe una lista de notas y una posicion en donde ubicar
		"""
		
		#la posicion X lo determina la grilla a la cual corresponde
		if pos_grilla > 7 :
			pos_grilla -= 8
			#para que se desplace al endecagrama de abajo
			index_desp = 32
		else :
			index_desp = 0
		
		pos_x = self.grillas_arriba[pos_grilla]
		
		dy = 3
		#se busca en la lista de nombres para saber que linea es
		y_soprano = None
		for index in range(12) :
			if soprano == nombres[index] :
				y_soprano = self.lineas[index+index_desp].y + dy
				break
				
		y_contralto = None
		for index in range(4, 15) :
			if contralto == nombres[index] :
				y_contralto = self.lineas[index+index_desp].y + dy
				break
				
		y_tenor = None
		for index in range(15, 27) :
			if tenor == nombres[index] :
				y_tenor = self.lineas[index+index_desp].y + dy
				break
		
		self.draw_blanca( pos_x+2, y_soprano, plica='arriba')
		self.draw_blanca( pos_x, y_contralto )
		self.draw_blanca( pos_x+2, y_tenor, plica='arriba' )

	def re_draw( self ) :
		"""
		Redibuja toda la interfaz
		"""
		
		#dibujar todo de vuelta
		self.screen.fill(Color.WHITE)
		self.draw_fondo()
		self.draw()
		#self.draw_fondo()
		#self.draw_lineas_negras()
		self.draw_claves()
		self.draw_compases()
		#self.draw_nombre_lineas()
		self.draw_armadura_sostenido()
		#dibujar las figuras anteriores
		for index in range(len(self.notas)) :
			
			x = self.notas[index][0][0]
			y = self.notas[index][0][1]
			plica = self.notas[index][1]
			
			self.draw_blanca( x, y, plica=plica)
		

if __name__ == "__main__" :
	
	ventana = VentanaPrincipal()
	ventana.handler()
