#!/bin/python

from armonizador import *
import random
#~ 
"""
Prueba de reconocer acordes
"""
#~ 
#~ pepito = Acorde()
#~ pepito.soprano.nombre = 'si'
#~ pepito.soprano.altura = 3
#~ pepito.soprano.alteracion = ''
#~ pepito.contralto.nombre = 'sol'
#~ pepito.contralto.altura = 3
#~ pepito.contralto.alteracion = '#'
#~ pepito.tenor.nombre = 'mi'
#~ pepito.tenor.altura = 3
#~ pepito.tenor.alteracion = ''
#~ pepito.bajo.nombre = 'si'
#~ pepito.bajo.altura = 1
#~ pepito.bajo.alteracion = ''
#~ 
#~ print pepito.get_full_name()
#~ print pepito.modo
#~ print pepito.estado

#~ 
#~ """
#~ Prueba de reconocer distancia entre notas
#~ """
#~ 
#~ n_1 = Nota()
#~ n_1.nombre = 'Re'
#~ n_1.alteracion = ''
#~ n_2 = Nota()
#~ n_2.nombre = 'Do'
#~ n_2.alteracion = ''
 #~ 
#~ print util.menor_distancia(n_1, n_2)



#~ """
#~ Prueba de creacion de escala
#~ """
#~ 
#~ modo = ''
#~ tonalidad = Tonalidad ('mi', 'b', modo) 
#~ 
#~ lista1, lista2 = tonalidad.crear_escala() 
#~ 
#~ print lista1
#~ print  lista2
#~ 
#~ """
#~ Prueba para enlazar acordes
#~ """


bajo = Nota ()
bajo.nombre = 'la'
bajo.alteracion = ''
bajo.altura = 1

tonalidad = Tonalidad ('la', '', '')


acorde_anterior = Acorde()
acorde_anterior.soprano.nombre = 'si'
acorde_anterior.soprano.altura = 3
acorde_anterior.soprano.alteracion = ''
acorde_anterior.contralto.nombre = 'sol'
acorde_anterior.contralto.altura = 3
acorde_anterior.contralto.alteracion = '#'
acorde_anterior.tenor.nombre = 'mi'
acorde_anterior.tenor.altura = 3
acorde_anterior.tenor.alteracion = ''
acorde_anterior.bajo.nombre = 'mi'
acorde_anterior.bajo.altura = 2
acorde_anterior.bajo.alteracion = ''

armonizador = Armonizador()


#~ 
#~ acordes = armonizador.get_posibles_acordes(tonalidad, bajo)
#~ 
#~ for i in range (len(acordes)) :
	#~ for j in range (len(acordes[i])) :
		#~ print acordes[i][j]
	#~ print '--------------------------------------'
	
acordes = armonizador.enlace( tonalidad, acorde_anterior, bajo )




print 'Acorde Anterior : ' + str(acorde_anterior.get_full_name())

print 'soprano : ' + str(acorde_anterior.soprano.nombre) \
	+ str(acorde_anterior.soprano.alteracion)+ str(acorde_anterior.soprano.altura)
print 'contralto : ' + str(acorde_anterior.contralto.nombre) \
	+ str(acorde_anterior.contralto.alteracion)+ str(acorde_anterior.contralto.altura)
print 'tenor : ' + str(acorde_anterior.tenor.nombre) \
	+ str(acorde_anterior.tenor.alteracion)+ str(acorde_anterior.tenor.altura)
print 'bajo : ' + str(acorde_anterior.bajo.nombre) \
	+ str(acorde_anterior.bajo.alteracion)+ str(acorde_anterior.bajo.altura)
#~ 
print '----------------------------------------------------------------'
#~ if len(acordes) > 0 :
	#~ 
	#~ for pos in range (len (acordes)) :
		#~ #pos = random.randint (0, len(acordes)-1)  
	#~ 
		#~ print 'Una posible solucion : ' + str (acordes[pos].get_full_name()) 
		#~ print  'soprano : ' + str(acordes[pos].soprano.nombre) \
			#~ +str(acordes[pos].soprano.alteracion) + str(acordes[pos].soprano.altura)
		#~ print  'contralto : ' + str(acordes[pos].contralto.nombre) \
			#~ +str(acordes[pos].contralto.alteracion) + str(acordes[pos].contralto.altura)
		#~ print  'tenor : ' + str(acordes[pos].tenor.nombre) \
			#~ +str(acordes[pos].tenor.alteracion) + str(acordes[pos].tenor.altura)
		#~ print  'bajo : ' + str(acordes[pos].bajo.nombre) \
			#~ +str(acordes[pos].bajo.alteracion) + str(acordes[pos].bajo.altura)
#~ 
#~ else :
	#~ print 'No existe solucion que cumpla las reglas'
print 'Una posible solucion : ' + str (acordes.get_full_name()) 
print  'soprano : ' + str(acordes.soprano.nombre) \
	+str(acordes.soprano.alteracion) + str(acordes.soprano.altura)
print  'contralto : ' + str(acordes.contralto.nombre) \
	+str(acordes.contralto.alteracion) + str(acordes.contralto.altura)
print  'tenor : ' + str(acordes.tenor.nombre) \
	+str(acordes.tenor.alteracion) + str(acordes.tenor.altura)
print  'bajo : ' + str(acordes.bajo.nombre) \
	+str(acordes.bajo.alteracion) + str(acordes.bajo.altura)
