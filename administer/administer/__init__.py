import os
from flask import Flask, render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

############################################################
################## BANCO DE DADOS ##########################
############################################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


#############################################################
################## CONFIGURA LOGIN ##########################
#############################################################






############################################################
################## BLUEPRINTS ##############################
############################################################
from administer.principal.views import principal
from administer.usuarios.views import usuarios
from administer.funcionarios.views import funcionarios
from administer.error_pages.handlers import error_pages

app.register_blueprint(principal)
app.register_blueprint(usuarios,url_prefix='/usuarios')
app.register_blueprint(funcionarios,url_prefix='/funcionarios')
app.register_blueprint(error_pages)