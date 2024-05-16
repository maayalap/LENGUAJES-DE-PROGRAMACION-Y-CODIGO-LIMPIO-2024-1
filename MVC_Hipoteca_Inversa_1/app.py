from flask import Flask, redirect, request, url_for, render_template
from datetime import datetime
from model.model_user import Usuario
import routes

app = Flask(__name__, template_folder='view')
wsgi_app = app.wsgi_app
app.secret_key = 'root'


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
