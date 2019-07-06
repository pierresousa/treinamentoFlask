from flask import (render_template, request, Blueprint, url_for, redirect, request, flash, abort,
					make_response, jsonify)
from administer.funcionarios.forms import funcionario_form
from administer.funcionarios.models import Funcionario
from flask_login import LoginManager, current_user
from administer import login_required, db

funcionarios = Blueprint('funcionarios', __name__, template_folder='templates')

def valida_formulario(data):

	if (len(data["nome"]) <= 3 or len(data["nome"]) >= 120):
		return False


	try:

		len_email1 = len(data["email"].split("@"))
		len_email2 = len(data["email"].split("@")[-1].split('.'))

		if (len_email1 <= 0 or len_email1 > 2):
			return False
		if (len_email2 <= 0):
			return False

		if (int(data["idade"]) < 14 or int(data["idade"]) >= 180):
			return False

		if (int(data["setor"]) > 6 or int(data["setor"]) < 0):
			return False

	except:

		return False

	return True



@login_required()
@funcionarios.route("/adicionar", methods=["POST", "GET"])
def adicionar():
	
	add_funcionario = funcionario_form()
	
	if add_funcionario.validate_on_submit():
		print("Errado, to aqui")

		new_employer = Funcionario(add_funcionario)

		new_employer.admin_id = current_user.id

		db.session.add(new_employer)
		db.session.commit()
		flash("Adicionado", "danger")
		
		return redirect(url_for('funcionarios.exibe_all'))

	
	flash("Deu Ruim", "danger")

	return redirect(url_for('funcionarios.dashboard'))


@login_required()
@funcionarios.route("/excluir/<int:id>", methods=["POST", "GET"])
def excluir(id):
	
	del_employer = Funcionario.query.get_or_404(id)

	if del_employer.admin.id != current_user.id:
		abort(403)

	db.session.delete(del_employer)
	db.session.commit()

	return redirect(url_for('funcionarios.meus_funcionarios'))

@login_required()
@funcionarios.route("/editar/<int:id>", methods=["POST", "GET"])
def editar(id):
	
	edit_employer = Funcionario.query.get_or_404(id)

	if edit_employer.admin.id != current_user.id:

		res = make_response(jsonify({"message": "Aqui não FDP"}), 403)
		return res

	data = request.get_json()

	edit_employer.nome = data["nome"]
	edit_employer.idade = data["idade"]
	edit_employer.email = data["email"]
	edit_employer.setor = data["setor"]

	res = make_response(jsonify({"message": "JSON recebido"}), 200)

	if not valida_formulario(data):
		
		res = make_response(jsonify({"message": "JSON crashado"}), 500)
		return res

	db.session.commit()

	return res

@login_required()
@funcionarios.route("/exibe_all")
def exibe_all():

	add_funcionario = funcionario_form()

	titulo = "Todos funcionários"
	setor = [("0", "Equipe administrativo"), ("1", "Desenvolvedor"), ("2", "Equipe projetos"), ("3", "Equipe RH"), ("4", "Equipe marketing"), ("5", "Equipe presidencia"), ("6", "Equipe Negocios")]
	setor = dict(setor)

	page = request.args.get('page', 1, type=int)
	funcionarios = Funcionario.query.paginate(page=page, per_page=12)
	return render_template("todos_funcionarios.html", setor=setor, titulo=titulo, funcionarios=funcionarios, add_funcionario=add_funcionario)

@login_required()
@funcionarios.route("/meus_funcionarios")
def meus_funcionarios():

	add_funcionario = funcionario_form()

	titulo = "Meus funcionários"
	setor = [("0", "Equipe administrativo"), ("1", "Desenvolvedor"), ("2", "Equipe projetos"), ("3", "Equipe RH"), ("4", "Equipe marketing"), ("5", "Equipe presidencia"), ("6", "Equipe Negocios")]
	setor = dict(setor)

	page = request.args.get('page', 1, type=int)
	funcionarios = Funcionario.query.filter_by(admin_id=current_user.id).paginate(page=page, per_page=12)
	
	return render_template("todos_funcionarios.html", setor=setor, titulo=titulo, funcionarios=funcionarios, add_funcionario=add_funcionario)

@login_required()
@funcionarios.route("/exibe/<int:id>")
def exibe(id):
	
	add_funcionario = funcionario_form()
	funcionario = Funcionario.query.get_or_404(id)

	return render_template("funcionario.html", add_funcionario=add_funcionario, funcionario=funcionario)