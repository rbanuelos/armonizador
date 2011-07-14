
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
	>>>Fa_mayor
	"""
	soprano = Nota()
	contralto = Nota()
	tenor = Nota()
	bajo = Nota()
	
	notas = []

	nombre = None
	
	def __init__(self):
		pass

	def get_nombre(self):
		
		#se guardan los nombres de las notas en una lista
		self.notas.append(self.soprano.nombre)
		self.notas.append(self.contralto.nombre)
		self.notas.append(self.tenor.nombre)
		self.notas.append(self.bajo.nombre)
		
		#si algun nombre no esta dentro de los nombres posibles no existe
		#el acorde
		for index in range(4):
			if not self.notas[index] in posibles_notas:
				return 'No existe'
		
		#hallar distancias entre voces(notas) 
		pos_soprano = posibles_notas.index(self.soprano.nombre)
		pos_contralto = posibles_notas.index(self.contralto.nombre)
		pos_tenor = posibles_notas.index(self.tenor.nombre)
		pos_bajo = posibles_notas.index(self.bajo.nombre)
		
		#se toma como fundamental algunas de las notas para verificar
		#si el acorde esta completo
		#se necesita una fundamental, una 3era, y una 5ta.
		#ej: Do_mayor
		#fundamental : do
		#3era : mi
		#5ta : sol
		for index in range(4):
			
			pos_fund = posibles_notas.index(self.notas[index])
			pos_tercera = (pos_fund + 2)%7
			
			if posibles_notas[pos_tercera] in self.notas:
				pos_quinta = (pos_tercera + 2)%7
				if posibles_notas[pos_quinta] in self.notas:
					
					if len(set(self.notas)) == 3:
						return 'Acorde de '+ str(posibles_notas[pos_fund])
								
		return "No existe"

class Escala :
	
	def distancia (self, nota_1, nota_2) :
		
		dist_count = 0
		nota_actual = nota_1
		
		while nota_actual.nombre != nota_2.nombre : 
			
			#las distancias entre notas mi-fa y si-do son 1/2 de tono
			#el resto son de 1 tono
			if nota_actual.nombre == 'Mi' or nota_actual.nombre == 'Si':
				dist_count += 0.5
			else :
				dist_count += 1
			
			if nota_actual.alteracion == '#' :
				dist_count -= 0.5
			elif nota_actual.alteracion == 'b' : 
				dist_count += 0.5
			
			#posicion de la siguiente nota en la escala
			pos_sgte = (posibles_notas.index(nota_actual.nombre)+1)%7
			
			#se actualiza los valores del iterador
			nota_actual.nombre = posibles_notas[pos_sgte]
			nota_actual.alteracion = None
		
		if nota_2.alteracion == '#' :
				dist_count += 0.5
		elif nota_2.alteracion == 'b' : 
				dist_count -= 0.5
		
		return dist_count
