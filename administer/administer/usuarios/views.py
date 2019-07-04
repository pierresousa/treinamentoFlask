from flask import (render_template, request, Blueprint, url_for, redirect, request, flash, abort)
from administer.usuarios.models import Admin
from administer.usuarios.forms import AdicionarUserForm
from flask_login import LoginManager
from administer import login_required

usuarios = Blueprint('usuarios', __name__,template_folder='templates')

@login_required()
@usuarios.route("/dashboard", methods=["POST", "GET"])
def dashboard():
	
	return render_template("dashboard.html")

@login_required()
@usuarios.route("/perfil", methods=["POST", "GET"])
def perfil():
	
	pass

@login_required()
@usuarios.route("/funcionarios", methods=["POST", "GET"])
def funcionarios():
	
	pass