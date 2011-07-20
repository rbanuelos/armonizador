from clases import *
import random

class Armonizador :
	"""
	"""
	
	def enlace (self, tonalidad, acorde_anterior, bajo_dado) :
		"""
		Obtiene las combinaciones posibles de las voces y va filtrando
		esas combinaciones (acordes) mediante la validacion del 
		cumplimiento de las reglas
		"""
		combinaciones, s_dist, c_dist, t_dist = \
						util.posibles_disposiciones(tonalidad, \
											acorde_anterior, bajo_dado)
		#PRUEBA
		aplicar_regla_1 = False
		
		if aplicar_regla_1 :
			#Combinaciones que cumplen la primera regla
			combinaciones = util.regla_1 (combinaciones, s_dist, c_dist, \
															t_dist, bajo_dado)
			
		pass_regla_1 = []
		
		#instanciar las combinaciones
		for index in range(len(combinaciones)) :
			
			acorde = Acorde()
			#copiar los nombres
			acorde.soprano.nombre = combinaciones[index][0].nombre
			acorde.contralto.nombre = combinaciones[index][1].nombre
			acorde.tenor.nombre = combinaciones[index][2].nombre
			acorde.bajo.nombre = bajo_dado.nombre
			#copiar alteraciones
			acorde.soprano.alteracion = combinaciones[index][0].alteracion
			acorde.contralto.alteracion = combinaciones[index][1].alteracion
			acorde.tenor.alteracion = combinaciones[index][2].alteracion
			acorde.bajo.alteracion = bajo_dado.alteracion
			#copiar alturas
			acorde.soprano.altura = combinaciones[index][0].altura
			acorde.contralto.altura = combinaciones[index][1].altura
			acorde.tenor.altura = combinaciones[index][2].altura
			acorde.bajo.altura = bajo_dado.altura
			
			#validacion de distancia entre voces
			if not util.distancia_entre_voces ( acorde) :
				pass_regla_1.append(acorde)
		
		pass_regla_2 = []
		
		for index in range(len(pass_regla_1)) :
			if not util.regla_2(acorde_anterior, pass_regla_1[index]) :
				pass_regla_2.append (pass_regla_1[index])
		
		pass_regla_3 = []
		
		for index in range(len(pass_regla_2)) :
			if not util.regla_3(tonalidad, acorde_anterior, \
													pass_regla_2[index]) :
				pass_regla_3.append (pass_regla_2[index])
		
		pass_regla_4 = []
		
		for index in range(len(pass_regla_3)) :
			if not util.regla_4(acorde_anterior, pass_regla_3[index]) :
				pass_regla_4.append (pass_regla_3[index])
		
		pass_regla_7 = []
		
		for index in range(len(pass_regla_4)) :
			if not util.regla_7(acorde_anterior, pass_regla_4[index]) :
				pass_regla_7.append (pass_regla_4[index])
		
		return pass_regla_7
	
	def get_triadas (self, tonalidad, bajo_dado) :
		"""
		Dada una nota halla los posibles acordes que se pueden formar 
		a partir de esa nota
		
		A partir de una nota es posible obtener 3 acordes distintos
		ej. 
			Si el bajo es un Fa y la tonalidad es Do mayor dicho bajo 
			puede ser parte de un acorde de Fa en estado fundamental, 
			de un Re menor en primera inversion o de un si disminuido en 
			2 inversion
		"""
		#lista de acordes. Siempre 3 acordes
		triadas = []
		#posicion de la nota del bajo_dado
		pos = posibles_notas.index( bajo_dado.nombre) 
		
		triada = []
		
		triada.append( posibles_notas[pos])
		triada.append( posibles_notas[(pos+2)%7])
		triada.append( posibles_notas[(pos+4)%7])
		
		triadas.append( triada)
		
		
		triada = []
		
		triada.append( posibles_notas[(pos+5)%7])
		triada.append( posibles_notas[pos])
		triada.append( posibles_notas[(pos+2)%7])
		
		triadas.append( triada)
		
		triada = []
		
		triada.append( posibles_notas[(pos+3)%7])
		triada.append( posibles_notas[(pos+5)%7])
		triada.append( posibles_notas[pos])
		
		triadas.append( triada)
		
		
		return triadas
	
	def get_posibles_acordes (self, tonalidad, bajo_dado) :
		"""
		"""
		#las posibles triadas a partir de una nota
		triadas = self.get_triadas(tonalidad, bajo_dado)
		
		escala, alteraciones = tonalidad.crear_escala()
		
		grado_1 = escala.index( triadas[0][0])+1
		grado_2 = escala.index( triadas[1][0])+1
		grado_3 = escala.index( triadas[2][0])+1
		
		return self.validar_triada (triadas[2], grado_3, 2) 
		
	def validar_triada (self, triada, grado, inversion) :
		"""
		Metodo que determina que nota podemos duplicar de la triada segun
		el grado dentro de la tonalidad y su estado de inversion
		si inversion vale 0 entonces el acorde no esta invertido, si vale
		1 entonces esta en primera inversion y 2 si es que se encuentra en
		2da inversion
		"""
		
		if grado == 1 and inversion == 0 :
			triada.append( triada[0])
		
		if grado == 1 and inversion == 1 :
			triada.append( triada[0])
			triada.append( triada[2])
		
		if grado == 1 and inversion == 2 :
			triada.append( triada[2])
		
		if grado == 4 and inversion == 0 :
			triada.append( triada[0])
		
		if grado == 4 and inversion == 1 :
			triada.append( triada[0])
			triada.append( triada[2])
		
		if grado == 4 and inversion == 2 :
			triada.append( triada[2])
		
		return triada
		
	def reglas_filter (self, tonalidad, acorde_anterior, bajo_dado) :
		"""
		Metodo que determina que reglas deben aplicarse de acuerdo a los 
		acordes que componen el enlace
		"""
		
		reglas_a_aplicar = []
		
		#incializamos el array booleano que nos permite saber si aplicar
		#o no la regla de acuerdo a la posicion dentro del array
		for index in range(14):
			reglas_a_aplicar.append(False)
		
		#verifica si debe aplicarse la regla 1
		escala, alteraciones = tonalidad.crear_escala()
		acorde_anterior.get_full_name()
		acorde_anterior.get_full_name()
		nombre_1 = acorde_anterior.nombre
		#if  
