from flask import (render_template, request, Blueprint, url_for, redirect, request, flash, abort)
from administer.usuarios.models import Admin
from administer.usuarios.forms import AdicionarUserForm

usuarios = Blueprint('usuarios', __name__,template_folder='templates')

@usuarios.route("/dashboard", methods=["POST", "GET"])
def dashboard():
	pass

@usuarios.route("/perfil", methods=["POST", "GET"])
def perfil():
	pass

@usuarios.route("/funcionarios", methods=["POST", "GET"])
def funcionarios():
	pass