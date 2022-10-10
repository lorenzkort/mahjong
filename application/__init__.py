from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '04059ffd6ab2a3ab32f5d2a09b950242'

from application import routes