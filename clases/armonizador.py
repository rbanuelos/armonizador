from clases import *
import random

class Armonizador :
	"""
	"""
	
	def enlace (self, tonalidad, acorde_anterior, bajo_dado) :
		
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
