from Sistema.app import db

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