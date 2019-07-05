from administer import db, login_manager
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(user_id)

class Admin(db.Model, UserMixin):
	"""docstring for Admin"""

	__tablename__ = "administradores"

	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(120), nullable=False)
	email = db.Column(db.String(120), nullable=False, unique=True)
	username = db.Column(db.String(120), nullable=False, unique=True)
	data_nasc = db.Column(db.DateTime, nullable=False)
	hhash = db.Column(db.String)

	urole = db.Column(db.String(80), default="Admin")

	avatar = db.Column(db.String(120), default="default_profile.png")

	funcionarios = db.relationship('Funcionario', backref='admin', uselist=True)
	
	def __init__(self, nome, email, username, data_nasc, hhash, avatar):
		self.nome = nome
		self.email = email
		self.username = username
		self.data_nasc = data_nasc
		self.hhash = hhash
		self.avatar = avatar

	def get_urole(self):

		return self.urole

	def check_password(self, pasword):
		bcript = Bcrypt()
		return bcript.check_password_hash(self.hhash, pasword)
