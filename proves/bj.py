from pywebio        import start_server
from pywebio.input  import *
from pywebio.output import *

import joc

def blackjack():
    with use_scope('scope1'):  # open and enter a new output: 'scope1'
        put_html("<h1>BENVINGUT AL BLACKJACK</h1>").style('text-align: center;')
        put_button("Començar a jugar", onclick=click).style('text-align: center;')

def click():
    with use_scope('scope1', clear=True):
        put_html('<h1>BLACKJACK</h1>').style('text-align: center;'),
        joc.joc()

start_server(blackjack, port=8080, debug=True)