import os
from flask import Flask, render_template, url_for
from forms import CadastroForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Aluno

app = Flask(__name__)

#Codificação para formularios
app.config['SECRET_KEY'] = 'senha para forms'

#Banco de dados
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sobre")
def sobre():
    return render_template('sobre.html')

@app.route("/listar")
def listar():

    return render_template('listar.html')

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    cadastrado = False
    form = CadastroForm()
    nome = ""
    if form.validate_on_submit():
        cadastrado = True
        nome = form.nome.data
        idade = form.idade.data
        curso = form.curso.data
        email = form.email.data
        telefone = form.telefone.data

        novo_aluno = Aluno(nome,idade,curso,email,telefone)
        db.session.add(novo_aluno)
        db.session.commit()

    return render_template('cadastro.html', form=form, cadastrado=cadastrado, nome=nome)

if __name__ == '__main__':
    app.run(debug=True)
