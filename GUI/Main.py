#!/bin/python

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

tesitura_soprano = ['sol4', 'fa4', 'mi4','re4', 'do4', 
					'si3', 'la3', 'sol3', 'fa3', 'mi3','re3', 'do3'
					]

tesitura_contralto = ['do4', 'si3', 'la3', 'sol3', 'fa3', 'mi3',
						're3', 'do3', 'si2', 'la2', 'sol2',
						]
						
tesitura_tenor = ['sol3', 'fa3', 'mi3','re3', 'do3','si2', 
					'la2', 'sol2','fa2', 'mi2','re2', 'do2'
					]
					
tesitura_bajo = ['do3', 'si2', 'la2', 'sol2','fa2', 'mi2','re2', 'do2',
									'si1', 'la1', 'sol1', 'fa1', 'mi1',]

class Color:
	WHITE = 255, 255, 255
	BLACK = 0, 0, 0
	GRAY = 191,191,191
	YELLOW = 255,255, 0

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
	#todas las notas que se dibujaron
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
		
		#self.draw_fondo()
		self.draw()
		self.draw_claves()
		self.draw_compases()
		self.draw_nombre_lineas()
		self.draw_armadura_sostenido()
		self.draw_boton_armonizar ()
		
		print len(self.lineas)
				
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
			
			if __linea.collidepoint(mouse_x, mouse_y) :
				
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
							self.notas.append((pos_x, __y))
						
						else : 
							#reemplazar la figura
							self.reemplazar_figura( pos_x, __y )
							#dibujar todo de vuelta
							self.screen.fill(Color.WHITE)
							self.draw()
							self.draw_claves()
							self.draw_compases()
							self.draw_nombre_lineas()
							self.draw_armadura_sostenido()
							#dibujar las figuras anteriores
							for tupla in self.notas :
								self.draw_blanca(tupla[0], tupla[1])
					else :
						pos_grilla = self.grillas_abajo.index( pos_x )
						
						#guardar el nombre de la linea seleccinoada
						self.bajos_dados[pos_grilla+8] = \
										nombres[self.lineas.index(linea)]
										
						#se verifica que este libre
						if not self.grilla_ocupada_abajo[pos_grilla] :
							self.draw_blanca(pos_x, __y)
							self.grilla_ocupada_abajo[pos_grilla] = True
							self.notas.append((pos_x, __y))
						
						else : 
							#reemplazar la figura
							self.reemplazar_figura( pos_x, __y )
							#dibujar todo de vuelta
							self.draw()
							self.draw_claves()
							self.draw_compases()
							self.draw_nombre_lineas()
							self.draw_armadura_sostenido()
							#dibujar las figuras anteriores
							for tupla in self.notas :
								self.draw_blanca(tupla[0], tupla[1])
							
				pygame.display.flip()
				break
		return

	def clic_handler_boton( self, mouse_x, mouse_y ) :
		"""
		Se verifica que el clikc hecho por el usuario este dentro del 
		boton "armonizar"
		"""
		
		if self.boton.collidepoint(mouse_x, mouse_y) :
			print 'Click sobre el boton'
			
		return
	
	def armonizador_handler()
		"""
		Luego de seleccionar el boton "Armonizar" este metodo se encarga
		de pasar estos datos a la clase armonizador
		"""
		
		
	def draw( self ):
		"""
		Mbaez : 13/07/2011
		"""
		space = 8
		self.lineas = []
		
		######### 1er Endecagrama clave de Sol###########
		for i in range (3,4) :
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
		
		######### 1er Endecagrama clave de Fa###########
		for i in range (20,25) :
			if i%2 != 0 :
				rect = self.draw_line(50, 50 + space * i, Color.YELLOW)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.GRAY)

			self.lineas.append(rect)
		
		for i in range (25,35) :
			if i%2 == 0 :
				rect = self.draw_line(50, 50 + space * i, Color.BLACK)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.YELLOW)

			self.lineas.append(rect)

		for i in range (35,37) :
			if i%2 == 0 :
				rect = self.draw_line(50, 50 + space * i, Color.GRAY)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.YELLOW)

			self.lineas.append(rect)
			
		######### 2do Endecagrama clave de Sol###########
		for i in range (45,46) :
			if i%2 != 0 :
				rect = self.draw_line(50, 50 + space * i, Color.YELLOW)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.GRAY)

			self.lineas.append(rect)
			
		for i in range (46,56) :
			if i%2 == 0 :
				rect = self.draw_line(50, 50 + space * i, Color.BLACK)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.YELLOW)

			self.lineas.append(rect)

		for i in range (56,60) :
			if i%2 != 0 :
				rect = self.draw_line(50, 50 + space * i, Color.YELLOW)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.GRAY)

			self.lineas.append(rect)
		
		######### 2do Endecagrama clave de Fa###########
		for i in range (62,67) :
			if i%2 != 0 :
				rect = self.draw_line(50, 50 + space * i, Color.YELLOW)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.GRAY)

			self.lineas.append(rect)
		
		for i in range (67,77) :
			if i%2 == 0 :
				rect = self.draw_line(50, 50 + space * i, Color.BLACK)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.YELLOW)

			self.lineas.append(rect)

		for i in range (77,79) :
			if i%2 == 0 :
				rect = self.draw_line(50, 50 + space * i, Color.GRAY)
			else :
				rect = self.draw_line(50, 50 + space * i, Color.YELLOW)

			self.lineas.append(rect)
		
		pygame.display.flip()

	def draw_fondo( self ) :
		"""
		dibuja el fondo de la aplicacion
		"""
		
		#dibuja la clave de Sol
		fullname = os.path.join('', 'fondo2.jpg')
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

		"""
		fullname = os.path.join('', 'half note up.gif')
		image = pygame.image.load(fullname)
		image = pygame.transform.scale(image, (30, 52))
		image = image.convert() # Set the right pixel depth
		colorkey = image.get_at((0,0)) # Get pixel for transparent colour
		image.set_colorkey(colorkey, RLEACCEL) # Set transparent colour
		imagerect = image.get_rect() # Get the rect of the image
		screenrect = self.screen.get_rect()
		imagerect.centerx, imagerect.centery = ptox, ptoy-16
		
		self.screen.blit(image, imagerect)
		
		pygame.display.flip()
		"""
		
		fullname = os.path.join('', 'half note down.gif')
		image = pygame.image.load(fullname)
		image = pygame.transform.scale(image, (30, 52))
		image = image.convert() # Set the right pixel depth
		colorkey = image.get_at((0,0)) # Get pixel for transparent colour
		image.set_colorkey(colorkey, RLEACCEL) # Set transparent colour
		imagerect = image.get_rect() # Get the rect of the image
		screenrect = self.screen.get_rect()
		imagerect.centerx, imagerect.centery = ptox, ptoy+16
		
		self.screen.blit(image, imagerect)
		
		pygame.display.flip()
		
	def draw_claves( self ) :
		"""
		"""
		for desp in (0, 336) :
			#dibuja la clave de Sol
			fullname = os.path.join('', 'clave_de_sol.gif')
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
			fullname = os.path.join('', 'ClaveFa.gif')
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
			fullname = os.path.join('', 'corchete2.gif')
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
		
		fullname = os.path.join('', 'sostenido.gif')
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
		
		fullname = os.path.join('', 'bemol.gif')
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
	
	def reemplazar_figura( self, x, y ) :
		"""
		Metodo que dado un x e y reemplaza por el que ocupa su misma
		grilla
		"""
		distancia_de_clave = 96
		
		for tupla in self.notas :
			if tupla[0] == x :
				dif = abs(tupla[1]-y)
				
				if dif < distancia_de_clave :
					self.notas.remove( tupla )
		
		self.notas.append((x, y))
	
	def draw_boton_armonizar( self ) :
		"""
		Despliega en pantalla el boton que sirve para que la maquina 
		proceda a resolver el ejercicio de armonia
		"""
		
		font = pygame.font.Font(None, 80)
		# Render the text
		text = font.render("Armonizar", True, (0, 0, 0), \
												(255, 255, 255, 255))
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
		
		font = pygame.font.Font(None, 80)
		# Render the text
		text = font.render("Armonizar", True, (255, 0, 0), \
												(255, 255, 255, 255))
		textRect = text.get_rect()
		#posicion
		textRect.centerx = 900
		textRect.centery = 750
	
		self.screen.blit(text, textRect)
		
		self.boton = textRect
		
		
if __name__ == "__main__" :
	
	ventana = VentanaPrincipal()
	ventana.handler()
