from flask import render_template
from myapp import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about-me')
def about_me():
    return render_template('about_me.html')
