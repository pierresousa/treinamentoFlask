from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email

class CadastroForm(FlaskForm):

    nome = StringField("Nome", validators=[DataRequired()])
    idade = IntegerField("Idade", validators=[DataRequired()])
    curso = StringField("Curso", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    telefone = IntegerField("Telefone", validators=[DataRequired()])

    submit = SubmitField("Cadastrar")

class Editar(FlaskForm):
    id = IntegerField("id", validators=[DataRequired()])
    nome = StringField("Nome", validators=[DataRequired()])
    idade = IntegerField("Idade", validators=[DataRequired()])
    curso = StringField("Curso", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    telefone = IntegerField("Telefone", validators=[DataRequired()])

    submit = SubmitField("Editar")
