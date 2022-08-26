
from pywebio.input  import *
from pywebio.output import *
from functools import partial

import joc

def numAposta(num):
    joc.quantitat -= num
    return joc.quantitat
    
def aposta():
    put_html("<h1>Quant vols apostar?</h1>")
    put_button(5, onclick=partial(numAposta, num=5))
    print(joc.quantitat)
    with use_scope('quantitat', clear=True):
        put_text("hola")

    put_text("Prova")
