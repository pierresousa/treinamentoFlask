from administer import db

class Admin(db.Model):
	"""docstring for Admin"""

	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(120), nullable=False)
	apelido = db.Column(db.String(120), nullable=False)
	data_nasc = db.Column(db.DateTime, nullable=False)
	
	def __init__(self, nome, apelido, data_nasc):
		self.nome = nome
		self.apelido = apelido
		self.data_nasc = data_nasc
