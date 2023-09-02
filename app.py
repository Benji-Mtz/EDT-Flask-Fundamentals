from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return """
    <h1 style="font-size: 64px; color:blue;"> Hola Mundo!</h1>
    """


@app.route('/contacto')
def contact():
    return """
    <h1 style="font-size: 64px; color:blue;"> Contact</h1>
    """


@app.route('/nosotros')
def our():
    return """
    <h1 style="font-size: 64px; color:blue;"> Nosotros</h1>
    """


@app.route('/login/<name>')
@app.route('/login/')
def login(name=None):
    if name is not None:
        return redirect(url_for("dashboard", name=name))
    else:
        return f'<h1 style="font-size: 32px; color:blue;">Ingresa tu nombre en la Url...</h1>'


@app.route('/profile/<name>')
@app.route('/profile/')
def dashboard(name=None):
    if name is not None:
        return f'<h1 style="font-size: 16px; color:green;">Bienvenido (a) { name } al dashboard</h1>'
    return redirect(url_for("login"))


"""
@app.route('/saludo/<name>/<int:sueldo>')
@app.route('/saludo/<name>')
@app.route('/saludo/')
def greeting(name=None, sueldo=None):
    if name is not None:
        if sueldo is not None:
            return f'<h1 style="font-size: 64px; color:blue;">Hola: { name }, tu sueldo es: { sueldo * 2 }</h1>'
        return f'<h1 style="font-size: 64px; color:blue;">Hola: { name }</h1>'
    else:
        return f'<h1 style="font-size: 64px; color:blue;">Hola desconocido</h1>'
"""
