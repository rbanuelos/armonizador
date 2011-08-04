import os
import sys

path = os.path.join(os.path.abspath(__file__))

path = os.path.abspath(os.path.join(path, '..'))

root_directory = os.path.abspath(os.path.join(path, '..'))

clase_directory = os.path.abspath(os.path.join(root_directory, 'clases'))

gui_directory = os.path.abspath(os.path.join(root_directory, 'GUI'))

sys.path.append(clase_directory)
sys.path.append(gui_directory)

from clases import *
from armonizador import *

class Controller :
	"""
	Clase que controla la logica de los enlaces
	
	adapta los resultados del armonizador a la interfaz 
	grafica y viceversa.
	
	"""
	
	#registro de todos los acordes que se obtuvieron como resultado
	acordes = ['','','','', '', 
					'','' ,'', '', '',
					'','','','', '']
		
	#resultados del ejercicio de forma dibujable
	resultados = ['','','','', '', 
							'','' ,'', '', '',
							 '','','','', '']
	
	#nomenclatura para expresar los acordes segun su grado y estado
	#ej: I, III6, V6-4
	cifrados = ['','','','', '', 
					'','' ,'', '', '',
					 '','','','', '']
	#nomenclatura para expresar los acordes segun su nombre, modo y bajo
	#ej: mi, lam, fa#/do#, dom/eb
	cifrados_americanos = ['','','','', '', 
								'','' ,'', '', '',
								'','','','', '']
	
	def estado_actual( self, bajos_dados, nombre_tonalidad, index=0 ) :
		"""
		Este es el metodo que sirve de intermediario entre la interfaz
		grafica y la clase que realiza los enlaces
		
		Retorna los acordes en forma de posiciones que se pueden graficar
		en la pantalla y su cifrado
		
		"""
		for j in range( len( self.acordes )) :
			
			if self.acordes[j] != '' :
				print self.acordes[j].get_full_name()
		print '//////////////////////////////////////////'
		#creamos la tonalidad > nombre, alteracion, modo
		tonalidad = Tonalidad( nombre_tonalidad, '', '' )
		
		escala, alteraciones = tonalidad.crear_escala()
		
		while True :
			
			if bajos_dados[index] == None :
				break
			
			bajo_actual = bajos_dados[index]
			pos = escala.index(bajo_actual[0:len(bajo_actual)-1]) 
			alteracion = alteraciones[pos]
			
			#creamos una nota que representa al bajo
			bajo = Nota()
			#subtring del original 'mi2' se quita el '2' para que quede 'mi'
			bajo.nombre = bajo_actual[0:len(bajo_actual)-1]
			bajo.altura = int(bajo_actual[len(bajo_actual)-1])
			bajo.alteracion = alteracion
			
			#primer acorde debe ser tonica
			if index == 0 :
				
				acorde = armonizador.crear_primer_acorde( tonalidad, bajo )
				#backtracking
				if acorde == None :
					index -= 2
				
				else :
					
					#guardamos el resultado
					self.acordes[index] = acorde  
					self.resultados[index] = self.acordes_a_grafico( acorde ) 
					self.cifrados[index] = acorde.get_cifrado( tonalidad ) 
					self.cifrados_americanos[index] = acorde.get_cifrado_americano()
			
			#ultimo acorde debe ser la tonica
			elif index == 14 :
				acorde = armonizador.enlace( tonalidad, \
												self.acordes[index-1], bajo )
				#backtracking
				if acorde == None :
					index -= 2
				
				elif acorde.get_full_name() == self.acordes[0].get_full_name() :
					#guardamos el resultado
					self.acordes[index] = acorde 
					self.resultados[index] = self.acordes_a_grafico( acorde ) 
					self.cifrados[index] = acorde.get_cifrado( tonalidad ) 
					self.cifrados_americanos[index] = acorde.get_cifrado_americano()
				
				#backtracking
				else :
					index -= 1

			else :
				acorde = armonizador.enlace( tonalidad, \
												self.acordes[index-1], bajo )
				#backtracking
				if acorde == None :
					index -= 2
				
				else :
					#guardamos el resultado
					self.acordes[index] =  acorde 
					self.resultados[index] = self.acordes_a_grafico( acorde ) 
					self.cifrados[index] = acorde.get_cifrado( tonalidad ) 
					self.cifrados_americanos[index] = acorde.get_cifrado_americano()
			
			index += 1
			
			if index == 15 :
				break
		
	def acordes_a_grafico( self, acorde ) :
		"""
		Metodo que recibe un acorde y una posicion donde dibujar
		"""
		
		#el armonizador retorna None al no encontrar solucion
		if acorde == None :
			return 'No tiene solucion'
		
		soprano = str(acorde.soprano.nombre) \
											+str(acorde.soprano.altura)
		
		contralto = str(acorde.contralto.nombre) \
											+str(acorde.contralto.altura)
		
		tenor = str(acorde.tenor.nombre) + str(acorde.tenor.altura)
		
		to_draw = []
		to_draw.append( soprano )
		to_draw.append( contralto )
		to_draw.append( tenor )
		
		return to_draw
	
	def resolver( self, bajos_dados, nombre_tonalidad ) :
		"""
		Metodo que verifica el buen uso de los acordes de 6-4 y VII6
		"""
		
		#se le pasa al metodo el estado actual para que encuentre una 
		#solucion
		self.estado_actual( bajos_dados, nombre_tonalidad )
		
		'''
		#dada una solucion este metodo verifica que este correcto el uso
		#del acorde de 6-4
		for index in range(len(self.acordes)) :
			
			if self.acordes[index] == '' :
				break
			
			self.acordes[index].get_full_name()
			
			#verificar que use correctamente los acordes 6-4
			if self.acordes[index].estado == '6-4' :
				
				#comprobamos si alguna voz se movio mas de una 2da.
				#en el caso de ser asi esta incorrecto el uso de este 
				#acorde de 6-4
				for i in range(10) :
					if self.comprobar_salto( index ) :
						self.estado_actual( \
								bajos_dados, nombre_tonalidad, index=index )
					else :
						break
		'''
		return self.resultados, self.cifrados_americanos, self.cifrados  


#creamos una instancia para ser uilizada
controller = Controller()
