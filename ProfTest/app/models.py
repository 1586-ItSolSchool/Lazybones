from ProfTest import db

class admin(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	login = db.Column(db.String(20), index=True, unique=True)
	password = db.Column(db.String(30))
	first_name = db.Column(db.String(15), index=True) 
	surname = db.Column(db.String(15), index=True)
	second_name = db.Column(db.String(15), index=True)

	def __repr__(self):
        return '<admin {}>'.format(self.first_name) 


class student(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(15), index=True)
	surname = db.Column(db.String(15), index=True, unique=True)
	second_name = db.Column(db.String(15), index=True)
	klass = db.Column(db.String(3))
	birth_date = db.Column(db.Date)
	phone_number = db.Column(db.String(12))

	def __repr__(self):
        return '<student {}>'.format(self.surname) 


class result(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	student_id = db.Column(db.Integer, primary_key=True)
	test_id = db.Column(db.Integer, primary_key=True)

	def count(result_type)
		

class test(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	result_type = db.Column(db.Integer)

	def __repr__(self):
        return '<test {}>'.format(self.title) 


class question(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	test_id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(1000000))

	def __repr__(self):
        return '<question {}>'.format(self.text) 


class student_answer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	answer_id = db.Column(db.Integer, primary_key=True)
	test_id = db.Column(db.Integer, primary_key=True)
	student_id = db.Column(db.Integer, primary_key=True)
	result_id = db.Column(db.Integer, primary_key=True)


class answer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	question_id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(1000000))
	points = db.Column(db.Integer) 

	def __repr__(self):
        return '<answer {}>'.format(self.text) 


class result_type:
	pass


class characters:
	pass
