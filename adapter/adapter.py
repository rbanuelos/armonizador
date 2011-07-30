import os
import sys

path = os.path.join(os.path.abspath(__file__))

path = os.path.abspath(os.path.join(path, '..'))

root_directory = os.path.abspath(os.path.join(path, '..'))

clase_directory = os.path.abspath(os.path.join(root_directory, 'clases'))

gui_directory = os.path.abspath(os.path.join(root_directory, 'GUI'))

sys.path.append(clase_directory)
sys.path.append(gui_directory)

print sys.path

from clases import *

class Adapter :
	"""
	Clase que adapta los resultados del armonizador a la interfaz 
	grafica y viceversa.
	
	La parte grafica envia un arreglo que corresponde a los bajos dados
	del ejercicio. 
	
	El armonizador debe recibir esos datos en forma de notas y acordes
	
	El armonizador retorna acordes solucion que deben ser mapeados a 
	figuras y dibujos dentro del pentagrama.
	"""

	def acordes_a_grafico( self, acorde, pos_grilla ) :
		"""
		Metodo que recibe un acorde y una posicion donde dibujar
		"""
		
		#el armonizador retorna None al no encontrar solucion
		if acorde == None :
			return 'No tiene solucion'
		
		soprano = str(acorde.soprano.nombre.lower()) \
											+str(acorde.soprano.altura)
		
		contralto = str(acorde.contralto.nombre.lower()) \
											+str(acorde.contralto.altura)
		
		
