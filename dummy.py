
from flask import Flask, redirect, render_template, request, url_for
from flask.helpers import flash
from flask_sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'aaa'
db = SQLAlchemy(app=app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/allinone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class profile(db.Model):
    username = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100))

    def __str__(self):
        return "name={}".format(self.ename)



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        s = profile(username=username, password=password)
        db.session.add(s)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin':
            return redirect(url_for('func_name'))
    else:
        return render_template('index.html')


@ app.route('/success')
def func_name():
    flash('login succesful')  # flash msg
    return render_template('success.html')


if __name__ == '__main__':
    db.create_all()
    app.run(host='127.0.0.1', port=8000, debug=True)
