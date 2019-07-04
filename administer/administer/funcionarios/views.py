from flask import (render_template, request, Blueprint, url_for, redirect, request, flash, abort)
from administer.funcionarios.forms import funcionario_form
from administer.funcionarios.models import Funcionario

funcionarios = Blueprint('funcionarios', __name__,template_folder='templates')

@funcionarios.route("/adicionar", methods=["POST", "GET"])
def adicionar():
	
	form = funcionario_form()

	if form.validate_on_submit():

		new_employer = Funcionario(form)

		db.session.add(new_employer)
		db.session.commit()

		return redirect(url_for('funcionarios.exibe'))

	return render_template("adiciona_funcionario.html")


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

@funcionarios.route("/exibe")
def exibe():
	
	funcionarios = Funcionario.query.all()

	return render_template("todos_funcionarios.html", funcionarios)