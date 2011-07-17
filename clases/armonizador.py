from clases import *
import random

class Armonizador :
	"""
	"""
	
	def enlace (self, tonalidad, acorde_anterior, bajo_dado) :
		
		combinaciones, s_dist, c_dist, t_dist = \
						util.posibles_disposiciones(tonalidad, \
											acorde_anterior, bajo_dado)
		
		pass_regla_1 = util.regla_1 (combinaciones, s_dist, c_dist, \
														t_dist, bajo_dado)
		
		acordes = []
		
		for index in range(len(pass_regla_1)) :
			
			acorde = Acorde()
			#copiar los nombres
			acorde.soprano.nombre = pass_regla_1[index][0].nombre
			acorde.contralto.nombre = pass_regla_1[index][1].nombre
			acorde.tenor.nombre = pass_regla_1[index][2].nombre
			acorde.bajo.nombre = bajo_dado.nombre
			#copiar alteraciones
			acorde.soprano.alteracion = pass_regla_1[index][0].alteracion
			acorde.contralto.alteracion = pass_regla_1[index][1].alteracion
			acorde.tenor.alteracion = pass_regla_1[index][2].alteracion
			acorde.bajo.alteracion = bajo_dado.alteracion
			#copiar alturas
			acorde.soprano.altura = pass_regla_1[index][0].altura
			acorde.contralto.altura = pass_regla_1[index][1].altura
			acorde.tenor.altura = pass_regla_1[index][2].altura
			acorde.bajo.altura = bajo_dado.altura
			
			if not util.regla_2( acorde_anterior, acorde) :
				acordes.append(acorde)
		
		return len(acordes)
		
