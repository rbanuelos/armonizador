
posibles_notas = ['Do','Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']
posibles_alturas = [1, 2, 3, 4, 5]
posibles_alteraciones = ['#', 'b', 'n']

class Nota :
	"""
	Clase Nota
	Representa un sonido con cierta altura.
	Dentro de la teoria de armonia es un componente de un acorde 
	(clase Acorde)
	
	el nombre que identifica a la nota
	acotado por los diferentes nombres posibles: 
	Do, Re, Mi, Fa, Sol, La, Si
	
	la altura determina la altura de la nota, que tan aguda o grave es 
	la nota. Ver grafico posibles_notas.jpg
	Una nota Do puede ser de altura:
	1 (do mas grave contemplado), 2, 3, 4, 5 (do mas agudo contemplado)
	
	la alteracion se refiere si la nota tiene un "#" (sostenido) o un 
	"b" (bemol) o "n" (natural)
	"""
	nombre = None
	altura = None
	alteracion = ''


class Acorde :
	"""
	Clase Acorde.
	Se compone de 4 notas, 3 diferentes y una repetida.
	Un acorde representa la emision de 4 notas en simultaneo por 4 voces
	humanas; la soprano, la contralto, el tenor, el bajo.
	
	ej: Acorde de Fa Mayor. Tiene las notas Fa, La, Do. 
	En este ejemplo se duplica la nota Fa. no puede duplicarse otra mas
	o que falte alguna que forma parte del acorde
	
	>>>mi_acorde = Acorde()
	>>>mi_acorde.soprano.nombre = 'Fa'
	>>>mi_acorde.soprano.altura = 4
	>>>mi_acorde.contralto.nombre = 'La'
	>>>mi_acorde.contralto.altura = 3
	>>>mi_acorde.tenor.nombre = 'Do'
	>>>mi_acorde.tenor.altura = 3
	>>>mi_acorde.bajo.nombre = 'Fa'
	>>>mi_acorde.bajo.altura = 2

	>>>print mi_acorde.get_nombre()
	>>>Fa
	"""
	soprano = None
	contralto = None
	tenor = None
	bajo = None
	
	notas = []
	
	alteraciones = []
	
	"""
	El nombre se refiere a si es Fa o Fa# o Fab
	El modo se refiere a si es Mayor o menor
	El estado define si esta en estado fundamental 
	(la fundamental esta en el bajo), primera inversion (la tercera esta
	en el bajo) o segunda inversion (la quinta esta en el bajo)
	""" 
	nombre = None
	modo = None
	estado = None
	
	def __init__(self) :
		"""
		"""
		self.soprano = Nota()
		self.contralto = Nota()
		self.tenor = Nota()
		self.bajo = Nota()

		
	def get_nombre (self) :
		"""
		"""
		self.notas = []
		#se guardan los nombres de las notas en una lista
		self.notas.append(self.soprano.nombre)
		self.notas.append(self.contralto.nombre)
		self.notas.append(self.tenor.nombre)
		self.notas.append(self.bajo.nombre)
		
		self.alteraciones = []
		#se guardan los nombres de las notas en una lista
		self.alteraciones.append(self.soprano.alteracion)
		self.alteraciones.append(self.contralto.alteracion)
		self.alteraciones.append(self.tenor.alteracion)
		self.alteraciones.append(self.bajo.alteracion)
		
		#si algun nombre no esta dentro de los nombres posibles no existe
		#el acorde
		for index in range(4) :
			if not self.notas[index] in posibles_notas:
				return 'Existe uno o mas nombres incorrectos'
		
		#si no tiene una nota repetida esta incorrecto
		duplicado = self.get_duplicado(self.notas, self.alteraciones)
		
		if duplicado == None :
			return 'No tiene nota duplicada'
		
		#se toma como fundamental algunas de las notas para verificar
		#si el acorde esta completo
		#se necesita una fundamental, una 3era, y una 5ta.
		#ej: Do_mayor
		#fundamental : do
		#3era : mi
		#5ta : sol
		
		acorde_valido = False
		
		for index in range(4):
			
			pos_fund = posibles_notas.index(self.notas[index])
			pos_tercera = (pos_fund + 2)%7
			
			if posibles_notas[pos_tercera] in self.notas:
				pos_quinta = (pos_tercera + 2)%7
				if posibles_notas[pos_quinta] in self.notas:
					acorde_valido = True
					break
		
		print 'Acorde Valido: ' + str(acorde_valido)
		
		if acorde_valido :
			
			self.nombre = posibles_notas[pos_fund]
			
			#sumarle la alteracion al nombre una vez
			for i in range(4) :
				if posibles_notas[pos_fund] == self.notas[i] :
					self.nombre += self.alteraciones[i]
					break
					
			mod = self.get_modo(pos_fund)
			
			print 'Es de modo: ' + str(mod)  
			
			if mod != None :
				self.nombre += mod
			
			posicion = self.get_estado(pos_fund)
			
			print 'Estado: ' + str(posicion)
			
			if mod != None :
				self.nombre += posicion
				return self.nombre
			
		return None

	def get_modo (self, pos_fund) :
		"""
		Casos Validos
		*	si la distancia entre la fundamental y la tercera es de 2 
		tonos y la distancia entre la tercera y la quinta es 1,5 tonos 
		entonces es un acorde mayor.
		
		*	si la distancia entre la fundamental y la tercera es de 1.5 
		tonos y la distancia entre la tercera y la quinta es 2 tonos 
		entonces es un acorde menor.
		"""
		
		nombre_1 = posibles_notas[pos_fund]
		nombre_3 = posibles_notas[(pos_fund + 2)%7]
		nombre_5 = posibles_notas[(pos_fund + 4)%7]
		
		for index in range (4) :
			
			if nombre_1 == self.notas[index] :
				nota_1 = Nota()
				nota_1.nombre = self.notas[index]
				nota_1.alteracion = self.alteraciones[index]
			
			if nombre_3 == self.notas[index] :
				nota_3 = Nota()
				nota_3.nombre = self.notas[index]
				nota_3.alteracion = self.alteraciones[index]
		
			if nombre_5 == self.notas[index] :
				nota_5 = Nota()
				nota_5.nombre = self.notas[index]
				nota_5.alteracion = self.alteraciones[index]
		
		#distancia_1 es la distancia entre la fundamental y la 3era 
		#y la distancia_2 es entre la 3era y la quinta
		distancia_1 = util.distancia (nota_1, nota_3)
		distancia_2 = util.distancia (nota_3, nota_5)
		
		if distancia_1 == 2 and distancia_2 == 1.5 :
			self.modo = ''
			return self.modo
		elif distancia_1 == 1.5 and distancia_2 == 2 :
			self.modo = 'm'
			return self.modo
		
		return None

	def get_duplicado (self, notas, alteraciones) :
		"""
		"""
		
		#si solo hay una sola nota repetida el len de la lista sin 
		#repetidos debe ser 3
		if len(set(notas)) != 3 :
			return None
		
		#concatenar las notas con alteraciones para verificar repetidos
		aux = []
		
		for i in range (4) : 
			aux.append(str(notas[i]) + str(alteraciones[i]))
		
		
		for i in range (4) : 
			
			index = i
			
			nota_aux = aux[i]
			aux[i] = ''
			
			if nota_aux in aux :
				return notas[i]
			else :
				aux[i] = nota_aux
		
		return None

	def get_estado (self, pos_fund) :
		"""
		"""
		nombre_1 = posibles_notas[pos_fund]
		nombre_3 = posibles_notas[(pos_fund + 2)%7]
		nombre_5 = posibles_notas[(pos_fund + 4)%7]
		
		if nombre_1 == self.bajo.nombre :
			return ''
		elif nombre_3 == self.bajo.nombre :
			return '6'
		elif nombre_5 == self.bajo.nombre :
			return '6-4'


class Util :
	"""
	Metodos utiles
	"""
	def distancia (self, nota_1, nota_2) :
		"""
		Metodo para hallar las distancias entre las notas
		Utilizado para generar las escalas de las tonalidades
		"""
		dist_count = 0

		if nota_1.alteracion == '#' :
			dist_count -= 0.5
		elif nota_1.alteracion == 'b' : 
			dist_count += 0.5
		if nota_2.alteracion == '#' :
			dist_count += 0.5
		elif nota_2.alteracion == 'b' : 
			dist_count -= 0.5
		
		nota_actual = Nota()
		nota_actual.nombre = nota_1.nombre
		nota_actual.alteracion = nota_1.alteracion
		
		#si no son la misma nota se itera el vector de notas posibles 
		#hasta llegar al destino
		while nota_actual.nombre != nota_2.nombre : 
			
			#las distancias entre notas mi-fa y si-do son 1/2 de tono
			#el resto son de 1 tono
			if nota_actual.nombre == 'Mi' : 
				dist_count += 0.5
			elif nota_actual.nombre == 'Si' :
				dist_count += 0.5 
			else :
				dist_count += 1
			
			pos_sgte = (posibles_notas.index(nota_actual.nombre)+1)%7
			
			nota_actual.nombre = posibles_notas[pos_sgte]
		
		return dist_count
	
	def menor_distancia (self, nota_1, nota_2) :
		"""
		Metodo para hallar el camino mas corto entre una nota y otra
		
		Ej:
		Dado 2 notas; Do y Si
		el camino mas corto dentro del array de notas posibles es igual
		a 1.
		
		Recorriendo el array hacia adelante la distancia es igual a 6, 
		en cambio recorriendo hacia atras es 1 
		
		['Do','Re', 'Mi', 'Fa', 'Sol', 'La', 'Si'] 
		"""
		
		cambiar_altura = False
		
		inicio = posibles_notas.index (nota_1.nombre)
		fin = posibles_notas.index (nota_2.nombre)
		
		distancia = abs(fin - inicio)
		 
		if distancia > 3 :
			cambiar_altura = True
			return 7 - distancia, cambiar_altura
		
		return distancia, cambiar_altura

	def get_movimientos (self, tonalidad, acorde_anterior, bajo_dado) :
		"""
		Metodo para obtener los movimientos posibles de cada voz
		Una voz puede ir a cualquiera de las 3 notas del siguiente 
		acorde y cada una de esas posibilidades tiene una distancia 
		asociada
		"""
		
		#auxiliares para guardar los distintas variantes
		sopranos = []
		sopranos_dist = []
		contraltos = [] 
		contraltos_dist = [] 
		tenores = []
		tenores_dist = []
		
		#se obtiene la escala de la tonalidad. Esto se debe hacer una 
		#sola vez
		escala, alteraciones = tonalidad.crear_escala()
		
		#terminar el grado de la nota del bajo dentro del acorde
		pos_dentro_de_escala = escala.index(bajo_dado.nombre)
		
		#VALIDACION: en el caso de que la nota del bajo sea distinta a las
		#notas de la escala
		if bajo_dado.alteracion != alteraciones[pos_dentro_de_escala] :
			return None
		  
		notas_de_acorde = []
		
		"""
		TODO
		Metodo para generar acordes
		"""
		#se anhaden como notas del acorde; la fundamental, la 3era y 
		#la 5ta
		for index in [0, 2, 4] :
			nota = Nota()
			pos = (pos_dentro_de_escala + index)%7
			nota.nombre = escala[pos]
			nota.alteracion = alteraciones [pos]
			notas_de_acorde.append (nota)
		
		#elegir opciones validas para la soprano, contralto y tenor
		for nota in notas_de_acorde :
			#nueva nota para la soprano
			nueva_nota = Nota()
			
			distancia, ajustar_altura = \
				self.menor_distancia(acorde_anterior.soprano, nota) 
				
			if ajustar_altura :
				nueva_nota.altura = acorde_anterior.soprano.altura - 1
			else :
				nueva_nota.altura = acorde_anterior.soprano.altura
			
			nueva_nota.nombre = nota.nombre 
			nueva_nota.alteracion = nota.alteracion
			 
			sopranos.append (nueva_nota)
			sopranos_dist.append(distancia)
			
			#nueva nota para la contralto
			nueva_nota = Nota()
				
			distancia, ajustar_altura = \
				self.menor_distancia(acorde_anterior.contralto, nota) 
		
			if ajustar_altura :
				nueva_nota.altura = acorde_anterior.contralto.altura - 1
			else :
				nueva_nota.altura = acorde_anterior.contralto.altura
			
			nueva_nota.nombre = nota.nombre 
			nueva_nota.alteracion = nota.alteracion
			
			 
			contraltos.append (nueva_nota)
			contraltos_dist.append(distancia)
			
			#nueva nota para el tenor
			nueva_nota = Nota()
				
			distancia, ajustar_altura = \
				self.menor_distancia(acorde_anterior.tenor, nota) 
		
			if ajustar_altura :
				nueva_nota.altura = acorde_anterior.tenor.altura - 1
			else :
				nueva_nota.altura = acorde_anterior.tenor.altura
			
			nueva_nota.nombre = nota.nombre 
			nueva_nota.alteracion = nota.alteracion
			 
			tenores.append (nueva_nota)
			tenores_dist.append(distancia)
			
		return sopranos, sopranos_dist, contraltos, contraltos_dist, \
			tenores, tenores_dist

	def posibles_disposiciones (self, tonalidad, acorde_anterior, bajo_dado) :
		"""
		Determina la combinacion de notas para el siguiente acorde
		"""
		#lista de posibles movimientos de la soprano, contralto y
		#tenor y sus respectivas distancias
		list_s, s_dist, list_c, c_dist, list_t, t_dist = \
			self.get_movimientos (tonalidad, acorde_anterior, \
															bajo_dado)
		
		combinaciones = []
		
		#sirve para verificar si es un acorde valido. cuenta los repetidos
		contador = [0, 0, 0]
		
		acorde = []
		for index in range (3) :
			acorde.append(list_s[index])
		
		#i, j, k iteradores sobre las 3 listas 
		for i in range (3) :
			nota_1 = list_s[i]
			
			contador[i] += 1
			
			for j in range (3) :
				
				nota_2 = list_c[j]
				
				if contador[j] == 1 :
					continue
				
				contador[j] += 1
				
				for k in range (3) :
					
					nota_3 = list_t[k]
					
					if contador[k] == 1 :
						continue
					
					contador[k] += 1
					
					combinacion = [nota_1, nota_2, nota_3, bajo_dado]
					combinaciones.append(combinacion)
					
					contador[k] -= 1
				
				contador[j] -= 1
			
			contador[i] -= 1
		
		return combinaciones, s_dist, c_dist, t_dist

	##################### REGLA 1 - ENLACE ARMONICO#################
	def regla_1 (self, combinaciones, s_dist, c_dist, t_dist, bajo_dado) :
		"""
		Primera regla de la armonia tradicional.
		Define que si existe una nota comun entre un acorde y su acorde 
		siguiente, dicha nota debe mantenerse en la misma voz y a la 
		misma altura
		
		se retorna solo las combinaciones que cumplen con la regla.
		puede tener excepciones
		"""
		
		pass_regla_1 = []
		
		#NO SIEMPRE EL BAJO VA A SER LA FUNDAMENTAL
		pos = posibles_notas.index(bajo_dado.nombre)
		_notas = [posibles_notas[pos], posibles_notas[(pos+2)%7], \
											posibles_notas[(pos+4)%7]]
		
		for index in range(3) :
			
			#se verifica si exista una distancia que sea 0 en algun 
			#movimiento de la soprano
			if s_dist[index] == 0 :
				
				for i in range(len(combinaciones)) :					
					
					if combinaciones[i][0].nombre == _notas[index] :
						pass_regla_1.append(combinaciones[i])
			
			#se verifica si exista una distancia que sea 0 en algun 
			#movimiento de la contralto
			if c_dist[index] == 0 :
				
				for i in range(len(combinaciones)) :					
					
					if combinaciones[i][1].nombre == _notas[index] :
						pass_regla_1.append(combinaciones[i])
			
			#se verifica si exista una distancia que sea 0 en algun 
			#movimiento del tenor
			if t_dist[index] == 0 :
				
				for i in range(len(combinaciones)) :					
					
					if combinaciones[i][2].nombre == _notas[index] :
						pass_regla_1.append(combinaciones[i])
		
		return pass_regla_1

	#~ ############# REGLA 2 - PROHIBIDO EL CRUCE DE VOCES##############
	#~ def regla_2 (self, tonalidad, acorde_anterior, bajo_dado) :
	
util = Util()

class Tonalidad :
	"""
	Clase que define la tonalidad del ejercicio de armonia a resolver
	Contiene metodos necesarios para la generacion de acordes
	"""
	nota = None
	modo = None
	
	escala_nombres = []
	escala_alteraciones = ['','','','','','','','']
	
	def __init__ (self, nombre, alteracion, modo) :
		self.nota = Nota()
		self.nota.nombre = nombre
		self.nota.alteracion = alteracion
		self.modo = modo
		
	def crear_escala (self) :
		"""
		Metodo para generar una escala dado un nombre de una tonalidad
		Se retorna un array con los nombres de las notas de la escala y
		otro con las alteraciones de las notas
		"""
		inicio = self.nota.nombre  
		index = posibles_notas.index(inicio)
		
		for i in range(index, index+8) :
			self.escala_nombres.append(posibles_notas [i%7]) 
		
		self.escala_alteraciones[0] = self.nota.alteracion
		
		n1 = Nota() 
		n2 = Nota()
		
		#FALTA COMPROBAR PARA EL MODO MENOR
		dist_modo_mayor = [1, 1, 0.5, 1, 1, 1, 0.5]
		
		for i in range (7) :
			
			n1.nombre = self.escala_nombres[i]
			n1.alteracion = self.escala_alteraciones[i]
			
			n2.nombre = self.escala_nombres[i+1]
			n2.alteracion = self.escala_alteraciones[i+1]
			
			dist = util.distancia (n1, n2) 
			
			if dist > dist_modo_mayor[i] :
				self.escala_alteraciones[i+1] = 'b'
			elif dist < dist_modo_mayor[i] :
				self.escala_alteraciones[i+1] = '#'
		
		
		return self.escala_nombres, self.escala_alteraciones


