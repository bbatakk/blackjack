from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def inici():
    data={
        'titol': 'Index',
        'benvinguts': 'Hola!'
    }
    return render_template('index.html', data=data)

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data={
        'titulo' : 'contacto',
        'nombre' : nombre,
        'edad' : edad
    }
    return render_template('contacto.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
