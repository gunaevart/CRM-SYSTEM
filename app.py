from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask, request, render_template, url_for

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


def addItem():
    admin = User(username = 'admin', email = 'admin@gmail.com', mess = 'To create the initial database, just import the db object')
    quest = User(username = 'quest', email = 'quest@mail.com', mess = 'SQLAlchemy.create_all() method to create the tables and database:')
    messeg = User()
    db.session.add(admin)
    db.session.add(quest)
    db.session.commit()


@app.route('/')
def index():
    user_date = User.query.all()
    return render_template('complete.html', user_date=user_date)


if __name__ == "__main__":
    app.run(debug=True)

    # 89505594691 андрей стойки для плуга  3*25