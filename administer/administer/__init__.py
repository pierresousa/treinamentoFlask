import os
from flask import Flask, render_template, redirect, flash, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

############################################################
################## BANCO DE DADOS ##########################
############################################################



############################################################
################## BLUEPRINTS ##############################
############################################################
from administer.principal.views import principal
from administer.usuarios.views import usuarios
from administer.error_pages.handlers import error_pages

app.register_blueprint(principal)
app.register_blueprint(usuarios,url_prefix='/usuarios')
app.register_blueprint(error_pages)