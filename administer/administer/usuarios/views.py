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
	print(form.submit.data)
	print("Adicionar")
	if form.validate_on_submit(): 
		bcript = Bcrypt()

		nome = form.nome.data
		username = form.username.data
		email = form.email.data
		data_nasc = form.data_nascimento.data

		hhash = bcript.generate_password_hash(form.senha.data)

		avatar = adicionar_avatar(form.foto.data, username) 
		
		novo_user = Admin(nome, email, username, data_nasc, hhash, avatar)
		print(novo_user)
		db.session.add(novo_user)
		db.session.commit()

		return redirect(url_for('principal.index'))

	return redirect(url_for('principal.index'))

@login_required()
@usuarios.route("/perfil", methods=["POST", "GET"])
def perfil():
	
	pass

@login_required()
@usuarios.route("/funcionarios", methods=["POST", "GET"])
def funcionarios():
	
	pass