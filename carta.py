from cgitb import grey
import random

from pywebio.input  import *
from pywebio.output import *

import joc
import repetir

def mesCarta():
    joc.cartes.append(random.randint(2, 11))
    with use_scope('cartes', clear=True):
        for i in joc.cartes: 
            put_text(i," ", inline=True)
        put_text("= ", sum(joc.cartes))

        if sum(joc.cartes) > 21:
            with use_scope("hit", clear=True):
                put_text("T'has passat...!")
                put_button("Tornar a jugar", onclick=repetir.repetir).style('display: inline;')
