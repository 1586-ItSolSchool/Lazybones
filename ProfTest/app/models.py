from ProfTest import db

class admin(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	login = db.Column(db.String(20), index=True, unique=True)
	password = db.Column(db.String(30))
	first_name = db.Column(db.String(15), index=True, unique=True) 
	surname = db.Column(db.String(15), index=True, unique=True)
	second_name = db.Column(db.String(15), index=True, unique=True)

	def 


class student(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(15), index=True, unique=True)
	surname = db.Column(db.String(15), index=True, unique=True)
	second_name = db.Column(db.String(15), index=True, unique=True)
	klass = db.Column(db.String(3))
	birth_date = db.Column(db.Date)
	phone_number = db.Column(db.String(12))

	def


class result(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	student_id = db.Column(db.Integer)
	test_id = db.Column(db.Integer)

	def


class test(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	result_type = db.Column(db.Integer)

	def


class question(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	test_id = db.Column(db.Integer)
	text = db.Column(db.String(1000000))

	def


class student_answer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	answer_id = db.Column(db.Integer)
	test_id = db.Column(db.Integer)
	student_id = db.Column(db.Integer)
	result_id = db.Column(db.Integer)

	def


class answer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	question_id = db.Column(db.Integer)
	text = db.Column(db.String(1000000))
	points = db.Column(db.Integer)

	def


class result_type


class characters 