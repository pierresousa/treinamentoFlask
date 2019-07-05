from flask import (render_template, request, Blueprint, url_for, redirect, request, flash, abort)
from administer.funcionarios.forms import funcionario_form
from administer.funcionarios.models import Funcionario
from flask_login import LoginManager, current_user
from administer import login_required

funcionarios = Blueprint('funcionarios', __name__,template_folder='templates')

@login_required()
@funcionarios.route("/adicionar", methods=["POST", "GET"])
def adicionar():
	
	add_funcionario = funcionario_form()
	print(add_funcionario)
	"""print(add_funcionario)
	print(add_funcionario.validate())
	
	if add_funcionario.validate_on_submit():

		new_employer = Funcionario(add_funcionario)

		new_employer.admin_id = current_user.id

		db.session.add(new_employer)
		db.session.commit()
		flash("Adicionado", "danger")"""
	
	flash("deu ruim", "danger")


	return redirect(url_for('funcionarios.exibe_all'))

	


@login_required()
@funcionarios.route("/excluir/<int:id>", methods=["POST", "GET"])
def excluir(id):
	
	del_employer = Funcionario.query.get_or_404(id)

	"""
	del_employer = Funcionario.query.get(id)
	
	if not del_employer:
		abort(404)
	"""

	db.session.delete(del_employer)
	db.session.commit()

	return 200

@login_required()
@funcionarios.route("/editar/<int:id>", methods=["POST", "GET"])
def editar(id):
	
	edit_employer = Funcionario.get_or_404(id)

#	data = request.args.json()

	edit_employer.name = data["name"]
	edit_employer.idade = data["idade"]
	edit_employer.email = data["email"]
	edit_employer.setor = data["setor"]

	db.session.commit()

	return 200

@login_required()
@funcionarios.route("/exibe_all")
def exibe_all():

	add_funcionario = funcionario_form()

	page = request.args.get('page', 1, type=int)
	funcionarios = Funcionario.query.all().paginate(page=page, per_page=12)
	return render_template("todos_funcionarios.html", funcionarios=funcionarios, add_funcionario=add_funcionario)

@login_required()
@funcionarios.route("/exibe/<int:id>")
def exibe(id):
	
	add_funcionario = funcionario_form()
	
	edit_funcionario = funcionario_form()

	#funcionario = Funcionario.query.get_or_404(id)

	#return render_template("funcionario.html", funcionario)
	return render_template("funcionario.html", add_funcionario=add_funcionario, 
							edit_funcionario=edit_funcionario)