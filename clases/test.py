#!/bin/python

from clases import *

#~ """
#~ Prueba de reconocer acordes
#~ """
#~ 
#~ mi_acorde = Acorde()
#~ mi_acorde.soprano.nombre = 'Si'
#~ mi_acorde.soprano.altura = 4
#~ mi_acorde.soprano.alteracion = ''
#~ mi_acorde.contralto.nombre = 'Sol'
#~ mi_acorde.contralto.altura = 4
#~ mi_acorde.contralto.alteracion = ''
#~ mi_acorde.tenor.nombre = 'Mi'
#~ mi_acorde.tenor.altura = 4
#~ mi_acorde.tenor.alteracion = ''
#~ mi_acorde.bajo.nombre = 'Sol'
#~ mi_acorde.bajo.altura = 4
#~ mi_acorde.bajo.alteracion = ''
#~ 
#~ print mi_acorde.get_nombre()

#~ 
#~ """
#~ Prueba de reconocer distancia entre notas
#~ """
#~ 
#~ n_1 = Nota()
#~ n_1.nombre = 'Do'
#~ n_1.alteracion = ''
#~ n_2 = Nota()
#~ n_2.nombre = 'Re'
#~ n_2.alteracion = ''
 #~ 
#~ print util.menor_distancia(n_1, n_2)



#~ """
#~ Prueba de creacion de escala
#~ """
#~ 
#~ modo = 'm'
#~ tonalidad = Tonalidad ('Mi', '', modo) 
#~ 
#~ lista1, lista2 = tonalidad.crear_escala() 
#~ 
#~ print lista1
#~ print  lista2

"""
Prueba para enlazar acordes
"""

#el bajo dado es un Fa
bajo = Nota ()
bajo.nombre = 'Fa'
bajo.alteracion = ''

#tonalidad Do mayor
tonalidad = Tonalidad ('Do', '', '')

#el acorde anterior es un Do Mayor
acorde_anterior = Acorde()
acorde_anterior.soprano.nombre = 'Do'
acorde_anterior.soprano.altura = 4
acorde_anterior.soprano.alteracion = ''
acorde_anterior.contralto.nombre = 'Mi'
acorde_anterior.contralto.altura = 3
acorde_anterior.contralto.alteracion = ''
acorde_anterior.tenor.nombre = 'Sol'
acorde_anterior.tenor.altura = 2
acorde_anterior.tenor.alteracion = ''
acorde_anterior.bajo.nombre = 'Do'
acorde_anterior.bajo.altura = 2
acorde_anterior.bajo.alteracion = ''

lista, distancias, lista2, distancias2, lista3, distancias3 = \
							util.enlace (tonalidad, acorde_anterior, bajo)

print 'Soprano List'
for index in range (len(lista)) :
	print str(lista[index].nombre)+str(lista[index].altura)+ \
									' distancia ' + str(distancias[index]) 

print 'Contralto List'
for index in range (len(lista2)) :
	print str(lista2[index].nombre)+str(lista2[index].altura)+ \
									' distancia ' + str(distancias2[index]) 

print 'Tenor List'
for index in range (len(lista3)) :
	print str(lista3[index].nombre)+str(lista3[index].altura)+ \
									' distancia ' + str(distancias3[index]) 
