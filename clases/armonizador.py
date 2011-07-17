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

		random_pos = random.randint(0, len(pass_regla_1)-1)
		
		combinacion = pass_regla_1[random_pos]
		#return combinacion
		
		if combinacion != None :
			
			acorde = Acorde()
			#copiar los nombres
			acorde.soprano.nombre = combinacion[0].nombre
			acorde.contralto.nombre = combinacion[1].nombre
			acorde.tenor.nombre = combinacion[2].nombre
			acorde.bajo.nombre = bajo_dado.nombre
			#copiar alteraciones
			acorde.soprano.alteracion = combinacion[0].alteracion
			acorde.contralto.alteracion = combinacion[1].alteracion
			acorde.tenor.alteracion = combinacion[2].alteracion
			acorde.bajo.alteracion = bajo_dado.alteracion
			#copiar alturas
			acorde.soprano.altura = combinacion[0].altura
			acorde.contralto.altura = combinacion[1].altura
			acorde.tenor.altura = combinacion[2].altura
			acorde.bajo.altura = bajo_dado.altura
			
			#el resultado del enlace es uno de los posibles acordes
			return acorde
