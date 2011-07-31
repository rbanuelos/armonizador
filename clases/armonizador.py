from clases import *
import random

class Armonizador :
	"""
	"""
	
	def crear_primer_acorde( self, tonalidad, bajo ) :
		"""
		Crea el primer acorde del ejercicio.
		Este acorde debe ser la tonica y debe estar en estado 
		fundamental.
		"""
		#creamos la escala
		escala, alteraciones = tonalidad.crear_escala()
		
		if escala[0] != bajo.nombre :
			return 'Error'
		
		notas = []
		notas.append( escala[0] )
		notas.append( escala[2] )
		notas.append( escala[4] )
		
		#combinaciones de posiciones distintas
		disposiciones = self.disposiciones_primer_acorde( notas ) 
		
		#PRUEBA
		acorde = Acorde()
		#copiar los nombres
		acorde.soprano.nombre = notas[1]
		acorde.contralto.nombre = notas[0]
		acorde.tenor.nombre = notas[2]
		acorde.bajo.nombre = bajo.nombre
		
		#copiar alteraciones
		acorde.soprano.alteracion = alteraciones[0]
		acorde.contralto.alteracion = alteraciones[1]
		acorde.tenor.alteracion = alteraciones[2]
		acorde.bajo.alteracion = bajo.alteracion
		
		#copiar alturas
		acorde.soprano.altura = 4
		acorde.contralto.altura = 3
		acorde.tenor.altura = 3
		acorde.bajo.altura = bajo.altura
		
		return acorde
		
	def disposiciones_primer_acorde( self, notas ) :
		"""
		Realiza combinaciones de las 3 notas. Estas combinaciones son 
		un caso especial en el primer acorde
		""" 
		
		disposiciones = []
		
		for i in range(3) :
			nombre_1 = notas[i]
			for j in range(3) :
				nombre_2 = notas[j]
				for k in range(3) :
					
					nombre_3 = notas[k]
					disposicion = [nombre_1, nombre_2, nombre_3]
					
					if len(set(disposicion)) == 3 :
						disposiciones.append(disposicion)
		
		return disposiciones
		
	def enlace( self, tonalidad, acorde_anterior, bajo_dado ) :
		"""
		Obtiene las combinaciones posibles de las voces y va filtrando
		esas combinaciones (acordes) mediante la validacion del 
		cumplimiento de las reglas
		"""
		posibles_acordes = self.get_posibles_acordes(tonalidad, bajo_dado)
		
		resultados = []
		
		for index in range(len (posibles_acordes)) :
			
			pass_regla_1 = [] 
			pass_regla_2 = [] 
			pass_regla_3 = [] 
			pass_regla_4 = [] 
			pass_regla_7 = [] 
			pass_regla_9 = [] 
			pass_regla_10 = [] 
			
			combinaciones, s_dist, c_dist, t_dist = \
			util.posibles_disposiciones(tonalidad, acorde_anterior, \
									bajo_dado, posibles_acordes[index])
			
			#de acuerdo al enlace que se desea hacer se establece que 
			#verificar reglas
			verificar_regla = self.reglas_filter( tonalidad, \
									acorde_anterior, combinaciones[0] )
			
			#return verificar_regla
			
			#se pregunta si se debe aplicar la regla o no 
			if verificar_regla[0] :
				#Combinaciones que cumplen la primera regla
				combinaciones = util.regla_1 (combinaciones, s_dist, \
												c_dist, t_dist, bajo_dado)
				
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
				
				#validacion de distancia entre voces y tesitura
				if not util.distancia_entre_voces ( acorde ) and \
									not util.comprobar_tesitura( acorde ):
					pass_regla_1.append(acorde)
			
				
			
			if verificar_regla[1] :
				for index in range(len(pass_regla_1)) :
					if not util.regla_2(acorde_anterior, pass_regla_1[index]) :
						pass_regla_2.append(pass_regla_1[index])
			else :
				#si no se aplico la regla se toma como que todas las
				#anteriores combinaciones pasaron la regla
				pass_regla_2 += pass_regla_1
			
			
			if verificar_regla[2] :
				for index in range(len(pass_regla_2)) :
					if not util.regla_3(tonalidad, acorde_anterior, \
															pass_regla_2[index]) :
						pass_regla_3.append(pass_regla_2[index])
			else :
				pass_regla_3 += pass_regla_2
			
			
			if verificar_regla[3] :
				for index in range(len(pass_regla_3)) :
					if not util.regla_4(acorde_anterior, pass_regla_3[index]) :
						pass_regla_4.append (pass_regla_3[index])
			else :
				pass_regla_4 += pass_regla_3
			
			
			if verificar_regla[6] :
				for index in range(len(pass_regla_4)) :
					if not util.regla_7(acorde_anterior, pass_regla_4[index]) :
						pass_regla_7.append (pass_regla_4[index])
			else :
				pass_regla_7 += pass_regla_4
			
			if verificar_regla[8] :
				for index in range(len(pass_regla_7)) :
					if not util.regla_9(acorde_anterior, pass_regla_7[index]) :
						pass_regla_9.append (pass_regla_7[index])
			else :
				pass_regla_9 += pass_regla_7
			
			if verificar_regla[9] :
				for index in range(len(pass_regla_9)) :
					if not util.regla_10( acorde_anterior, pass_regla_9[index] ) :
						pass_regla_10.append( pass_regla_9[index] )
			else :
				pass_regla_10 += pass_regla_9
				
			resultados += pass_regla_10

		return resultados
	
	def get_triadas( self, tonalidad, bajo_dado ) :
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
	
	def get_posibles_acordes( self, tonalidad, bajo_dado ) :
		"""
		"""
		#las posibles triadas a partir de una nota
		triadas = self.get_triadas( tonalidad, bajo_dado )
		
		escala, alteraciones = tonalidad.crear_escala()
		
		grado_1 = escala.index( triadas[0][0] ) + 1
		grado_2 = escala.index( triadas[1][0] ) + 1
		grado_3 = escala.index( triadas[2][0] ) + 1
		
		posibles_acordes = []
		tuplas = []
		
		tuplas.append( self.validar_triada( triadas[0], grado_1, 0 )) 
		tuplas.append( self.validar_triada( triadas[1], grado_2, 1  )) 
		tuplas.append( self.validar_triada( triadas[2], grado_3, 2 )) 
		
		
		#dentro de las tuplas tenemos diferentes longitudes porque en 
		#algunas se puede duplicar no solo una nota sino varias. 
		#Hay que transformar aquellas tuplas en tuplas
		#de 4 notas (3 distintas y 1 duplicada) para que formen acordes. 
		return self.acordes_parser(tuplas)
	
	def acordes_parser( self, tuplas ) :
		"""
		Metodo que construye acordes de 4 notas a partir de tuplas de 
		distinta longitud. Si alguna tupla tiene 4 notas significa que
		esta completo. En cambio si alguna tupla tiene longitud mayor a 
		4 entonces se deben formar tuplas de 4 notas
		ej : 
			longitud = 5
			[do, mi, sol, do, mi]
			
			las tuplas resultados son :
			[do, mi, sol, do] y [do, mi, sol, mi]
		"""
		
		acordes = []
		
		for index in range(len(tuplas)) :
			
			if len( tuplas[index] ) == 4 :
				acordes.append(tuplas[index])
			
			if len( tuplas[index] ) == 5 :
				acorde_1 = []
				acorde_2 = []
				
				acorde_1.append(tuplas[index][0])
				acorde_1.append(tuplas[index][1])
				acorde_1.append(tuplas[index][2])
				acorde_1.append(tuplas[index][3])
				
				acordes.append(acorde_1)
				
				acorde_2.append(tuplas[index][0])
				acorde_2.append(tuplas[index][1])
				acorde_2.append(tuplas[index][2])
				acorde_2.append(tuplas[index][4])
				
				acordes.append(acorde_2)
			
			if len( tuplas[index] ) == 6 :
				
				acorde_1 = []
				acorde_2 = []
				acorde_3 = []
				
				acorde_1.append(tuplas[index][0])
				acorde_1.append(tuplas[index][1])
				acorde_1.append(tuplas[index][2])
				acorde_1.append(tuplas[index][3])
				
				acordes.append(acorde_1)
				
				acorde_2.append(tuplas[index][0])
				acorde_2.append(tuplas[index][1])
				acorde_2.append(tuplas[index][2])
				acorde_2.append(tuplas[index][4])
				
				acordes.append(acorde_2)
				
				acorde_3.append(tuplas[index][0])
				acorde_3.append(tuplas[index][1])
				acorde_3.append(tuplas[index][2])
				acorde_3.append(tuplas[index][5])
				
				acordes.append(acorde_3)
			
		return acordes

	def validar_triada( self, triada, grado, inversion ) :
		"""
		Metodo que determina que nota o notas podemos duplicar de la 
		triada segun el grado dentro de la tonalidad y su estado de 
		inversion si inversion vale 0 entonces el acorde no esta 
		invertido, si vale 1 entonces esta en primera inversion y 2 si 
		es que se encuentra en 2da inversion
		
		En este metodo estan de forma implicita la reglas 8, 11, 13, 14,
		15 y 16 de manera completo o parcial. 
		
		Las reglas antes mencionadas definen que notas se pueden 
		duplicar segun el acorde y su estado
		"""
		
		#Acordes de I grado
		if grado == 1 and inversion == 0 :
			triada.append( triada[0])
		
		if grado == 1 and inversion == 1 :
			triada.append( triada[0])
			triada.append( triada[2])
		
		if grado == 1 and inversion == 2 :
			triada.append( triada[2])
		
		#Acordes de II grado
		if grado == 2 and inversion == 0 :
			triada.append( triada[1])
			triada.append( triada[2])
		
		if grado == 2 and inversion == 1 :
			triada.append( triada[1])
			triada.append( triada[2])
		
		#no se usa el acorde de II grado en segunda inversion
		if grado == 2 and inversion == 2 :
			return []
		
		#Acordes de III grado. Solo se usa en estado fundamental
		if grado == 3 and inversion == 0 :
			triada.append( triada[0])
			triada.append( triada[1])
		
		if grado == 3 and inversion == 1 :
			return []
			
		if grado == 3 and inversion == 2 :
			return []
		
		#Acordes de IV grado
		if grado == 4 and inversion == 0 :
			triada.append( triada[0])
		
		if grado == 4 and inversion == 1 :
			triada.append( triada[0])
			triada.append( triada[2])
		
		if grado == 4 and inversion == 2 :
			triada.append( triada[2])
		
		#Acordes de V grado
		if grado == 5 and inversion == 0 :
			triada.append( triada[0])
		
		if grado == 5 and inversion == 1 :
			triada.append( triada[0])
			triada.append( triada[2])
		
		if grado == 5 and inversion == 2 :
			triada.append( triada[2])
		
		#Acordes de VI grado. Solo se usa en estado fundamental
		if grado == 6 and inversion == 0 :
			triada.append( triada[0])
			triada.append( triada[1])
			triada.append( triada[2])
		
		if grado == 6 and inversion == 1 :
			return []
			
		if grado == 6 and inversion == 2 :
			return []
		
		#Acordes de VII grado. solo se usa en 1era inversion
		if grado == 7 and inversion == 0 :
			return []
		
		if grado == 7 and inversion == 1 :
			triada.append( triada[1])
			triada.append( triada[2])
		
		if grado == 7 and inversion == 2 :
			return []

		return triada
		
	def reglas_filter( self, tonalidad, acorde_anterior, combinacion ) :
		"""
		Metodo que determina que reglas deben aplicarse de acuerdo a los 
		acordes que componen el enlace
		recibe el acorde anterior y una triada que corresponde a un 
		posible acordes siguiente
		
		Recibe el acorde anterior y algun posible acorde solucion
		
		"""
		
		#instanciamos como acorde la posible solucion
		acorde_sgte = Acorde()
		#copiar los nombres
		acorde_sgte.soprano.nombre = combinacion[0].nombre
		acorde_sgte.contralto.nombre = combinacion[1].nombre
		acorde_sgte.tenor.nombre = combinacion[2].nombre
		acorde_sgte.bajo.nombre = combinacion[3].nombre
		#copiar alteraciones
		acorde_sgte.soprano.alteracion = combinacion[0].alteracion
		acorde_sgte.contralto.alteracion = combinacion[1].alteracion
		acorde_sgte.tenor.alteracion = combinacion[2].alteracion
		acorde_sgte.bajo.alteracion = combinacion[3].alteracion
		#copiar alturas
		acorde_sgte.soprano.altura = combinacion[0].altura
		acorde_sgte.contralto.altura = combinacion[1].altura
		acorde_sgte.tenor.altura = combinacion[2].altura
		acorde_sgte.bajo.altura = combinacion[3].altura
		
		reglas_a_aplicar = []
		
		#incializamos el array booleano que nos permite saber si aplicar
		#o no la regla de acuerdo a la posicion dentro del array
		for index in range(14):
			reglas_a_aplicar.append(True)
		
		escala, alteraciones = tonalidad.crear_escala()
		
		acorde_anterior.get_full_name()
		acorde_sgte.get_full_name()
		
		nombre_1 = acorde_anterior.nombre
		nombre_2 = acorde_sgte.nombre
		
		grado_1 = escala.index( nombre_1 ) + 1
		grado_2 = escala.index( nombre_2 ) + 1
		
		estado_1 = acorde_anterior.estado
		estado_2 = acorde_sgte.estado
		
		#verifica si debe aplicarse la regla 1
		reglas_a_aplicar[0] = self.regla_1_filter( grado_1, grado_2 )

		#la regla 2 siempre se realiza
		reglas_a_aplicar[1] = True
		
		#la regla 3 siempre se realiza
		reglas_a_aplicar[2] = True
		
		#la regla 4 siempre se realiza
		reglas_a_aplicar[3] = True
		
		#PRUEBA
		reglas_a_aplicar[4] = False
		
		#PRUEBA
		reglas_a_aplicar[5] = False
		
		reglas_a_aplicar[6] = self.regla_7_filter( grado_1, estado_1, \
														grado_2, estado_2)
		
		reglas_a_aplicar[8] = self.regla_9_filter( grado_1, estado_1, \
														grado_2, estado_2)
		
		reglas_a_aplicar[9] = self.regla_10_filter( grado_1, estado_1, \
														grado_2, estado_2)
		return reglas_a_aplicar
		
	def regla_1_filter( self, grado_1, grado_2 ) :
		"""
		Metodo que determina si verificar o no la regla 1 
		Esta regla solo se aplica a acordes que tienen notas en comun
		"""
		if grado_2 == (grado_1+2)%7 or grado_2 == (grado_1+3)%7 \
				or grado_2 == (grado_1+4)%7 or grado_2 == (grado_1+5)%7 :
			return True
		
		return False
	
	def regla_5_filter( self, nro_compas ) :
		"""
		Metodo que determina si verificar o no la regla 5 
		Esta regla solo se aplica al ultimo acorde del ejercicio. Debe
		estar en estado fundamental y puede faltarle la 5ta.
		
		ej :
			Fa mayor.
			Notas = Fa, Fa, La (sin el Do)
			
		"""
		if nro_compas == 8 :
			return True
		
		return False

	def regla_6_filter( self, nro_compas_1, nro_compas_2 ) :
		"""
		Metodo que determina si verificar o no la regla 6 
		Esta regla solo se aplica si el acorde anterior y el siguiente
		son distintos. se verifica que no sean el mismo acorde
		
		"""
		if nro_compas_1 != nro_compas_2 :
			return True
		
		return False

	def regla_7_filter( self, grado_1, estado_1, grado_2, estado_2  ) : 
		"""
		Metodo que determina si se comprueba la regla 7 o no.
		Se aplica solo para el enlace IV - V
		
		"""
		#verifica que los grados sean respectivamente IV y V
		if grado_1 == 4 and grado_2 == 5:
			#verifica que esten ambos acordes en estado fundamental
			if estado_1 == '' and estado_2 == '' :
				return True
		
		return False
			
	def regla_9_filter( self, grado_1, estado_1, grado_2, estado_2  ) : 
		"""
		Metodo que determina si se comprueba la regla 9 o no.
		Se aplica solo para el enlace IV - V6 y el enlace IV6 - V
		
		"""
		#verifica que los grados sean respectivamente IV y V
		if grado_1 == 4 and grado_2 == 5:
			
			#verifica que esten ambos acordes en estado fundamental
			if estado_1 == '6' and estado_2 == '' :
				return True
			
			if estado_1 == '' and estado_2 == '6' :
				return True
		
		return False

	def regla_10_filter( self, grado_1, estado_1, grado_2, estado_2  ) : 
		"""
		Metodo que determina si se comprueba la regla 10 o no.
		Se aplica solo para el enlace IV6 - V6 
		
		"""
		#verifica que los grados sean respectivamente IV y V
		if grado_1 == 4 and grado_2 == 5:
			
			#verifica que esten ambos acordes en estado fundamental
			if estado_1 == '6' and estado_2 == '6' :
				return True
		
		return False

#instancia para ser utilizada por el controller
armonizador = Armonizador()
