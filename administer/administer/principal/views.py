from flask import render_template, Blueprint, url_for, flash
from administer.usuarios.forms import LoginForm, AdicionarUserForm

principal = Blueprint('principal', __name__)

@principal.route('/')
def index():
	form_login = LoginForm(prefix="form_login")
	form_add = AdicionarUserForm(prefix="form_add")
	return render_template('home.html', form_login=form_login, form_add=form_add)