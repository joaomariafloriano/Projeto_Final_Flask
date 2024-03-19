from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feminino')
def feminino():
    return render_template('feminino.html')

@app.route('/masculino')
def masculino():
    return render_template('masculino.html')

@app.route('/acessorios')
def acessorios():
    return render_template('acessorios.html')

@app.route('/central_atendimento')
def central_atendimento():
    return render_template('central_atendimento.html')

@app.route('/olympikus')
def olympikus():
    return render_template('olympikus.html')

@app.route('/fila')
def fila():
    return render_template('fila.html')

@app.route('/adidas')
def adidas():
    return render_template('adidas.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/nike')
def nike():
    return render_template('nike.html')

@app.route('/puma')
def puma():
    return render_template('puma.html')

@app.route('/reebok')
def reebok():
    return render_template('reebok.html')

@app.route('/recover_password')
def recover_password():
    return render_template('recover_password.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
