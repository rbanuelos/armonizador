
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
	soprano = Nota()
	contralto = Nota()
	tenor = Nota()
	bajo = Nota()
	
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
		pass

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

"""
Metodos utiles
"""
class Util :
	
	def distancia (self, nota_1, nota_2) :
		"""
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
		"""
		
		cambiar_altura = False
		
		inicio = posibles_notas.index (nota_1.nombre)
		fin = posibles_notas.index (nota_2.nombre)
		
		distancia = abs(fin - inicio)
		 
		if distancia > 3 :
			cambiar_altura = True
			return 7 - distancia, cambiar_altura
		
		return distancia, cambiar_altura

	def enlace (self, tonalidad, acorde_anterior, bajo_dado) :
		
		#lista de posibles acordes a retornar
		acordes_siguientes = []
		
		#auxiliares para guardar los distintas posiciones de los acordes
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
			
			print str(acorde_anterior.soprano.nombre)+' a ' + str(nota.nombre)
			distancia, ajustar_altura = \
				self.menor_distancia(acorde_anterior.soprano, nota) 
				
			if ajustar_altura :
				nueva_nota.altura = acorde_anterior.soprano.altura - 1
			else :
				nueva_nota.altura = acorde_anterior.soprano.altura
			
			nueva_nota.nombre = nota.nombre 
			nueva_nota.alteracion = nota.alteracion
			
			print nueva_nota.nombre
			 
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

util = Util()

class Tonalidad :
	
	nota = Nota()
	modo = None
	
	escala_nombres = []
	escala_alteraciones = ['','','','','','','','']
	
	def __init__ (self, nombre, alteracion, modo) :
		self.nota.nombre = nombre
		self.nota.alteracion = alteracion
		self.modo = modo
		
	def crear_escala (self) :

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

