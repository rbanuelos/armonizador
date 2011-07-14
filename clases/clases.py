
posibles_notas = ['Do','Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']
posibles_alturas = [1, 2, 3, 4, 5]
posibles_alteraciones = ['#', 'b']

class Nota:
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
	
	la alteracion se refiere si la nota tiene un # (sostenido) o un 
	b (bemol)
	"""
	nombre = None
	altura = None
	alteracion = None
	
	
class Acorde:
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

	>>>print acorde.get_nombre()
	>>>Fa_mayor
	"""
	soprano = Nota()
	contralto = Nota()
	tenor = Nota()
	bajo = Nota()
	
	notas = []

	nombre = None
	
	def __init__(self):
		#se guardan las notas en una lista
		self.notas.append(self.soprano)
		self.notas.append(self.contralto)
		self.notas.append(self.tenor)
		self.notas.append(self.bajo)
	
	def get_nombre(self):
		
		#si algun nombre no esta dentro de los nombres posibles no existe
		#el acorde
		for index in range(4):
			if not self.notas[index].nombre in posibles_notas:
				return 'No existe'
		
		#hallar distancias entre voces(notas) 
		pos_soprano = posibles_notas.index(self.soprano.nombre)
		pos_contralto = posibles_notas.index(self.contralto.nombre)
		pos_tenor = posibles_notas.index(self.tenor.nombre)
		pos_bajo = posibles_notas.index(self.bajo.nombre)
		
		"""
		TODO
		analizar todas las posibles disposiciones  de un acorde
		"""
