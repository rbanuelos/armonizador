#!/bin/python

from armonizador import *


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
bajo.altura = 2


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

armonizador = Armonizador()

acordes_len = armonizador.enlace (tonalidad, acorde_anterior, bajo)

print acordes_len

print 'Acorde anterior'
print  str(acorde_anterior.soprano.nombre) + str(acorde_anterior.soprano.altura)
print  str(acorde_anterior.contralto.nombre) + str(acorde_anterior.contralto.altura)
print  str(acorde_anterior.tenor.nombre) + str(acorde_anterior.tenor.altura)
print  str(acorde_anterior.bajo.nombre) + str(acorde_anterior.bajo.altura)
#~ 
#~ print 'Una posible solucion'
#~ print  str(acorde_sgte.soprano.nombre) + str(acorde_sgte.soprano.altura)
#~ print  str(acorde_sgte.contralto.nombre) + str(acorde_sgte.contralto.altura)
#~ print  str(acorde_sgte.tenor.nombre) + str(acorde_sgte.tenor.altura)
#~ print  str(acorde_sgte.bajo.nombre) + str(acorde_sgte.bajo.altura)

