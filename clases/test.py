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


"""
Prueba de reconocer distancia entre notas
"""

n_1 = Nota()
n_1.nombre = 'Do'
n_1.alteracion = ''
n_2 = Nota()
n_2.nombre = 'Re'
n_2.alteracion = ''
 
print util.menor_distancia(n_1, n_2)



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
