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
	acordes = []
	
	resultados = []
	cifrados = []
	
	def estado_actual( self, bajos_dados, nombre_tonalidad ) :
		"""
		Este es el metodo que sirve de intermediario entre la interfaz
		grafica y la clase que realiza los enlaces
		
		Retorna los acordes en forma de posiciones que se pueden graficar
		en la pantalla y su cifrado
		
		"""
		self.acordes = ['','','','', '', 
							'','' ,'', '', '',
							 '','','','', '']
		
		
		self.resultados = ['','','','', '', 
							'','' ,'', '', '',
							 '','','','', '']
		
		self.cifrados = ['','','','', '', 
							'','' ,'', '', '',
							 '','','','', '']
		
		#creamos la tonalidad > nombre, alteracion, modo
		tonalidad = Tonalidad( nombre_tonalidad, '', '' )
		
		escala, alteraciones = tonalidad.crear_escala()
		
	
		index = 0
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
			
			
			if index == 0 :
				
				acorde = armonizador.crear_primer_acorde( tonalidad, bajo )
				#backtracking
				if acorde == None :
					index -= 2
				
				else :
					#guardamos el resultado
					self.acordes[index] = acorde 
					self.resultados[index] = self.acordes_a_grafico( acorde ) 
					self.cifrados[index] = acorde.get_full_name() 
			else :
				acorde = armonizador.enlace( tonalidad, \
												self.acordes[index-1], bajo )
				#backtracking
				if acorde == None :
					index -= 2
				
				else :
					#guardamos el resultado
					self.acordes[index] = acorde 
					self.resultados[index] = self.acordes_a_grafico( acorde ) 
					self.cifrados[index] = acorde.get_full_name() 
			
			index += 1
			
			if index == 15 :
				break
			
		return self.resultados, self.cifrados 
		
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

#creamos una instancia para ser utilizada
controller = Controller()
