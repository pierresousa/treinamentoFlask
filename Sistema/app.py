import os
from flask import Flask, render_template, url_for, redirect
from forms import CadastroForm, Editar
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
#Codificação para formularios
app.config['SECRET_KEY'] = 'senha para forms'

#Banco de dados
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

class Aluno(db.Model):
    __tablename__ = 'alunos'
    id =  db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    idade = db.Column(db.Integer)
    curso = db.Column(db.String)
    email = db.Column(db.String, unique = True)
    telefone = db.Column(db.Integer, unique = True)

    def __init__ (self, nome, idade, curso, email, telefone):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.email = email
        self.telefone = telefone

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sobre")
def sobre():
    return render_template('sobre.html')

@app.route('/listar/<int:id>', methods=['POST', 'GET'])
@app.route("/listar", defaults={"id":None}, methods=['POST', 'GET'])
def listar(id):
    editar = Editar()
    if not id:
        alunos = Aluno.query.order_by(Aluno.nome.asc())
        id=None
    
    else:
        aluno = Aluno.query.get(id)
        db.session.delete(aluno)
        db.session.commit()
        alunos = Aluno.query.order_by(Aluno.nome.asc())

    if editar.validate_on_submit():
        aluno = Aluno.query.get_or_404(editar.id.data)
        aluno.nome = editar.nome.data
        aluno.idade = editar.idade.data
        aluno.curso = editar.curso.data
        aluno.email = editar.email.data
        aluno.telefone = editar.telefone.data
        db.session.commit()

    return render_template('listar.html', alunos=alunos, editar=editar)

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
