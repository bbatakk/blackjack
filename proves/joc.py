from pickle import INT
import random

from pywebio.input  import *
from pywebio.output import *

import aposta
import doblar
import carta


quantitat = 100
cartes = []

cartes.append(random.randint(2, 11))
cartes.append(random.randint(2, 11))
Sum = sum(cartes)

def joc():
    aposta.aposta()
    with use_scope('quantitat', clear=True):
        put_text(quantitat)
        
    with use_scope('cartes', clear=True):
        for i in cartes: 
            put_text(i," ", inline=True)

    with use_scope('doblar', clear=True):
        put_button("Doblar", onclick=doblar.doblar).style('display: inline;')

    with use_scope("hit", clear=True):
            put_button("Hit", onclick=carta.mesCarta).style('display: inline;')