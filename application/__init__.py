from flask import Flask

app = Flask(__name__)

from application import config

from application import routes

from application import tables
