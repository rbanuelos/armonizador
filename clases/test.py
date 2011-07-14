#!/bin/python

from clases import *

"""
Prueba de reconocer acordes


mi_acorde = Acorde()
mi_acorde.soprano.nombre = 'Mi'
mi_acorde.soprano.altura = 4
mi_acorde.contralto.nombre = 'Sol'
mi_acorde.contralto.altura = 3
mi_acorde.tenor.nombre = 'Mi'
mi_acorde.tenor.altura = 3
mi_acorde.bajo.nombre = 'Mi'
mi_acorde.bajo.altura = 2

print mi_acorde.get_nombre()
"""

"""
Prueba de reconocer distancia entre notas
"""

n_1 = Nota()
n_1.nombre = 'Do'
n_1.alteracion = 'b'
n_2 = Nota()
n_2.nombre = 'Do'
n_2.alteracion = '#'

escala = Escala()
 
print escala.distancia(n_1, n_2)
