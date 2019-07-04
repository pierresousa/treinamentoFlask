from administer import db

class Admin(db.Model):
	"""docstring for Admin"""

	__tablename__ = "administradores"

	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(120), nullable=False)
	apelido = db.Column(db.String(120), nullable=False)
	data_nasc = db.Column(db.DateTime, nullable=False)
	urole = db.Column(db.String(80), default="Admin")

	funcionarios = db.relationship('Funcionarios', backref='admin', uselist=True)
	
	def __init__(self, nome, apelido, data_nasc):
		self.nome = nome
		self.apelido = apelido
		self.data_nasc = data_nasc

	def get_urole(self):

		return self.urole
