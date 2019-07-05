from flask import render_template, Blueprint, url_for, flash, redirect
from administer.usuarios.forms import LoginForm, AdicionarUserForm
from flask_login import current_user

principal = Blueprint('principal', __name__)

@principal.route('/')
def index():
	form_login = LoginForm(prefix="form_login")
	form_add = AdicionarUserForm(prefix="form_add")
	if current_user.is_authenticated:
		return redirect(url_for('usuarios.dashboard'))
	return render_template('home.html', form_login=form_login, form_add=form_add)