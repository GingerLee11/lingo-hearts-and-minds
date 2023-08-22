from flask import render_template
from myapp import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about-me')
def about_me():
    return render_template('about_me.html')

@app.route('/charlemos_charlotte')
def charlemos_charlotte():
    return render_template('charlemos_charlotte.html')

@app.route('/living_archives')
def living_archives():
    return render_template('living_archives.html')

@app.route('/conexiones_que_cuentan')
def conexiones_que_cuentan():
    return render_template('conexiones_que_cuentan.html')

@app.route('/southend_spanish')
def southend_spanish():
    return render_template('southend_spanish.html')

@app.route('/lhcc')
def lhcc():
    return render_template('lhcc.html')
