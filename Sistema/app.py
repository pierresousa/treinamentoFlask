import os
from flask import Flask, render_template, url_for
from forms import CadastroForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'senha para forms'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sobre")
def sobre():
    return render_template('sobre.html')

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    cadastrado = False
    nome = " "
    form = CadastroForm()
    if form.validate_on_submit():
        nome = form.nome.data
    return render_template('cadastro.html', form=form, cadastrado=cadastrado, nome=nome)

if __name__ == '__main__':
    app.run(debug=True)
