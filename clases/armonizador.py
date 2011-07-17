from clases import *
import random

class Armonizador :
	"""
	"""
	
	def enlace (self, tonalidad, acorde_anterior, bajo_dado) :
		
		combinaciones, s_dist, c_dist, t_dist = \
						util.posibles_disposiciones(tonalidad, \
											acorde_anterior, bajo_dado)
		
		#Combinaciones que cumplen la primera regla
		comb_regla_1 = util.regla_1 (combinaciones, s_dist, c_dist, \
														t_dist, bajo_dado)
		
		pass_regla_1 = []
		
		#instanciar las combinaciones
		for index in range(len(comb_regla_1)) :
			
			acorde = Acorde()
			#copiar los nombres
			acorde.soprano.nombre = comb_regla_1[index][0].nombre
			acorde.contralto.nombre = comb_regla_1[index][1].nombre
			acorde.tenor.nombre = comb_regla_1[index][2].nombre
			acorde.bajo.nombre = bajo_dado.nombre
			#copiar alteraciones
			acorde.soprano.alteracion = comb_regla_1[index][0].alteracion
			acorde.contralto.alteracion = comb_regla_1[index][1].alteracion
			acorde.tenor.alteracion = comb_regla_1[index][2].alteracion
			acorde.bajo.alteracion = bajo_dado.alteracion
			#copiar alturas
			acorde.soprano.altura = comb_regla_1[index][0].altura
			acorde.contralto.altura = comb_regla_1[index][1].altura
			acorde.tenor.altura = comb_regla_1[index][2].altura
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
													pass_regla_1[index]) :
				pass_regla_3.append (pass_regla_2[index])
		
		return pass_regla_3
		
