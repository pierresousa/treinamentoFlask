from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, SubmitField, PasswordField, BooleanField, SelectField, DateField)
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileField, FileAllowed

class LoginForm(FlaskForm):

	email = StringField("Email", validators=[DataRequired(message="Campo Obrigatório"), Email(message="Campo Obrigatório"), Length(min=3, max=120, message="Minimo de 3 caracteres e máximo de 120 por favor!")])
	senha = PasswordField("Senha", validators=[DataRequired(), Length(min=0, max=250, message="Minimo de 3 caracteres e máximo de 250 por favor!")])
	lembrar = BooleanField("Lembrar-me")
	submit = SubmitField("Entrar")

class AdicionarUserForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    apelido = StringField("Apelido", validators=[DataRequired()])
    data_nascimento = DateField("Data de nascimento", format='%Y-%m-%d', validators=[DataRequired()])
    #foto = FileField('Foto', validators=[DataRequired(),FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField("Enviar")