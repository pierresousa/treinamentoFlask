from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, SelectField,
					 TextAreaField, RadioField, IntegerField)
from wtforms.validators import DataRequired, Length, Email


class funcionario_form(FlaskForm ):
	
	nome = StringField("Nome", validators=[DataRequired(message="Esse campo é obrigatório"), Length(min=3, max=120, message="Tamanho mínimo de 3 caracteres e maxímo de 120!")])

	idade = IntegerField("Idade", validators=[DataRequired(message="Esse campo é obrigatório"), Length(min=14, max=180, message="Idade mínima de 14!")])

	email = StringField("Email", validators=[DataRequired(message="Esse campo é obrigatório"), Length(min=3, max=120, message="Tamanho mínimo de 3 caracteres e maxímo de 120!"), Email()])

	setor = SelectField("Setor", validators=[DataRequired(message="Esse campo é obrigatório"), Length(min=3, max=120, message="Tamanho mínimo de 3 caracteres e maxímo de 120!")], choices=[("0", "Eqp_Adm_Fin"), ("1", "Dev"), ("2", "Eqp_Proj"), ("3", "Eqp_RH"), ("4", "Eqp_Markt"), ("5", "Eqp_Pres"), ("6", "Eqp_Neg")])

	submit = SubmitField("Novo Funcionário")
