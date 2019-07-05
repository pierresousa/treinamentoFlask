from flask import (render_template, request, Blueprint, url_for, redirect, request, flash, abort)
from administer.usuarios.models import Admin
from administer.usuarios.forms import AdicionarUserForm
from flask_login import LoginManager, current_user, login_user,login_required,logout_user
from administer import login_required
from administer.usuarios.avatar import adicionar_avatar
from flask_bcrypt import Bcrypt

usuarios = Blueprint('usuarios', __name__,template_folder='templates')

@login_required()
@usuarios.route("/dashboard", methods=["POST", "GET"])
def dashboard():
	
	return render_template("dashboard.html")

@usuarios.route('/cadastro', methods=['POST', 'GET'])
def adicionar():

	form = AdicionarUserForm()

	if form.validate_on_submit() and not Admin.query.filter_by(username=form.username.data).first() and not Admin.query.filter_by(email=form.email.data).first(): 
		bcript = Bcrypt()

		nome = form.nome.data
		username = form.username.data
		email = form.email.data
		data_nasc = form.data_nascimento.data

		hhash = bcript.generate_password_hash(form.senha.data)

		avatar = adicionar_avatar(form.foto.data, username) 
		
		novo_user = Admin(nome, email, username, data_nasc, hhash, avatar)

		db.session.add(novo_user)
		db.session.commit()

		return redirect(url_for('principal.index'))

	if Admin.query.filter_by(username=form.username.data).first():
		flash(f"Esse nome de usuário já existe.", "warning")

	if Admin.query.filter_by(email=form.email.data).first():
		flash(f"Esse e-mail já está em uso.", "warning")

	return redirect(url_for('principal.index'))

@login_required()
@usuarios.route("/perfil", methods=["POST", "GET"])
def perfil():
	
	pass

@login_required()
@usuarios.route("/funcionarios", methods=["POST", "GET"])
def funcionarios():
	
	pass