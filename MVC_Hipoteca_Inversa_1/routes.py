from app import app
from flask import render_template
from datetime import datetime

    
@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/session_home')
def session_home():
    return render_template(
        'index_login.html',
        title='Home Page Login',
        year=datetime.now().year,
    )