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
					index = -1
				
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
					index = -1
				
				elif acorde.get_full_name() == self.acordes[0].get_full_name() :
					#guardamos el resultado
					self.acordes[index] = acorde 
					self.resultados[index] = self.acordes_a_grafico( acorde ) 
					self.cifrados[index] = acorde.get_cifrado( tonalidad ) 
					self.cifrados_americanos[index] = acorde.get_cifrado_americano()
				
				#backtracking
				else :
					index = -1

			else :
				acorde = armonizador.enlace( tonalidad, \
												self.acordes[index-1], bajo )
				#backtracking
				if acorde == None :
					index = -1
				
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
		Metodo que continene la solucion final de los ejercicios
		"""
		#creamos la tonalidad > nombre, alteracion, modo
		tonalidad = Tonalidad( nombre_tonalidad, '', '' )
		
		#se le pasa al metodo el estado actual para que encuentre una 
		#solucion
		self.estado_actual( bajos_dados, nombre_tonalidad )
		
		while True :
			
			pos_error = self.verificador( tonalidad )
			
			if pos_error == None :
				return self.resultados, self.cifrados_americanos, \
															self.cifrados  
			else :
				self.estado_actual( bajos_dados, nombre_tonalidad, \
														index=pos_error )
			
	
	def verificador( self, tonalidad ) :
		"""
		
		Metodo que recibe una solucion completa y verifica si cumple con reglas
		especiales
		
		""" 
		 
		pos = None
		
		#buscamos un acorde VII6 en la solucion
		for index in range( len(self.acordes )) :
			if self.acordes[index] == '' :
				break

			if self.acordes[index].get_cifrado( tonalidad ) == 'VII6' :
				pos = index
				break

		if pos == None :
			return pos
		
		#la posicion del acorde de VII6 debe ser minimo 2. porque debe 
		#tener antes acorde de I y IV
		if pos < 2 :
			return pos
		
		#las posiciones de los acordes son I - IV - VII6 - I
		#posicion del acorde I
		pos_1 = pos-2 
		 
		#posicion del acorde IV
		pos_2 = pos-1 
		 
		#posicion del acorde VII6
		pos_3 = pos 
		 
		#posicion del acorde I
		pos_4 = pos+1 
		
		#si el acorde no es I no esta bien hecho 
		if not self.acordes[pos_1].get_cifrado( tonalidad ) == 'I' :
			return pos
		
		#si el acorde no es I no esta bien hecho 
		if not self.acordes[pos_2].get_cifrado( tonalidad ) == 'IV' :
			return pos
		
		#si el acorde no es I no esta bien hecho 
		if not self.acordes[pos_4].get_cifrado( tonalidad ) == 'I' :
			return pos
		
		#lista de nombres notas de los acordes 
		lista_1_nombre = []
		lista_2_nombre = []
		lista_3_nombre = []
		lista_4_nombre = []
		#lista de las alturas
		lista_1_altura = []
		lista_2_altura = []
		lista_3_altura = []
		lista_4_altura = []
		
		
		lista_1_nombre.append( self.acordes[pos_1].soprano.nombre )
		lista_1_nombre.append( self.acordes[pos_1].contralto.nombre )
		lista_1_nombre.append( self.acordes[pos_1].tenor.nombre )
		
		lista_1_altura.append( self.acordes[pos_1].soprano.altura )
		lista_1_altura.append( self.acordes[pos_1].contralto.altura )
		lista_1_altura.append( self.acordes[pos_1].tenor.altura )
		
		
		lista_2_nombre.append( self.acordes[pos_2].soprano.nombre )
		lista_2_nombre.append( self.acordes[pos_2].contralto.nombre )
		lista_2_nombre.append( self.acordes[pos_2].tenor.nombre )
		
		lista_2_altura.append( self.acordes[pos_2].soprano.altura )
		lista_2_altura.append( self.acordes[pos_2].contralto.altura )
		lista_2_altura.append( self.acordes[pos_2].tenor.altura )
		
		
		lista_3_nombre.append( self.acordes[pos_3].soprano.nombre )
		lista_3_nombre.append( self.acordes[pos_3].contralto.nombre )
		lista_3_nombre.append( self.acordes[pos_3].tenor.nombre )
		
		lista_3_altura.append( self.acordes[pos_3].soprano.altura )
		lista_3_altura.append( self.acordes[pos_3].contralto.altura )
		lista_3_altura.append( self.acordes[pos_3].tenor.altura )
		
		lista_4_nombre.append( self.acordes[pos_4].soprano.nombre )
		lista_4_nombre.append( self.acordes[pos_4].contralto.nombre )
		lista_4_nombre.append( self.acordes[pos_4].tenor.nombre )
		
		lista_4_altura.append( self.acordes[pos_4].soprano.altura )
		lista_4_altura.append( self.acordes[pos_4].contralto.altura )
		lista_4_altura.append( self.acordes[pos_4].tenor.altura )
		
		
		#necesitamos buscar el tetracordio superior ascendente
		pos_tonica = posibles_notas.index( self.acordes[pos_4].nombre )
		
		pos_7ma = (pos_tonica+6)%7
		
		pos_6ta = (pos_tonica+5)%7
		
		pos_5ta = (pos_tonica+4)%7
		
		#estas son las 4 notas que deben estar presentes en el tetracordio
		nombre_tonica = posibles_notas[pos_tonica]
		nombre_7ma = posibles_notas[pos_7ma]
		nombre_6ta = posibles_notas[pos_6ta]
		nombre_5ta = posibles_notas[pos_5ta]
		
		#buscamos la tonica en el ultimo acorde
		for i in range(3) :
			if nombre_tonica == lista_4_nombre[i] :
				#buscamos la sensible en el 3er acorde
				for j in range(3) :
					if nombre_7ma == lista_3_nombre[j] and \
								lista_3_altura[j] <= lista_4_altura[i] :
						#buscamos la 6ta en el 2do acorde
						for k in range(3) :
							if nombre_6ta == lista_2_nombre[k] and \
								lista_2_altura[k] <= lista_3_altura[j] :
								#buscamos la 5ta en el 1er acorde
								for l in range(3) :
									if nombre_5ta == lista_1_nombre[l] and \
									lista_1_altura[l] <= lista_2_altura[k] :
										return None
										
		return pos
		
		
#creamos una instancia para ser uilizada
controller = Controller()
