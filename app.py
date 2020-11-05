from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mess = db.Column(db.String(400), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/add')
def add():
    return render_template('file.html')




@app.route('/uploads', methods=['POST', 'GET'])
def insert():
    if request.method == 'POST':
        user_name = request.form['username']
        user_email = request.form['email']
        user_mess = request.form['mess']
        admin = User(username = user_name, email = user_email, mess = user_mess)
        messeg = User()
        db.session.add(admin)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/')
def index():
    user_date = User.query.all()
    return render_template('complete.html', user_date=user_date)


if __name__ == "__main__":
    app.run(debug=True)

    # 89505594691 андрей стойки для плуга  3*25