from pywebio.input  import *
from pywebio.output import *

import joc
import aposta

def doblar():
    joc.quantitat *= 2
    with use_scope('aposta', clear=True):
        put_text(joc.quantitat)