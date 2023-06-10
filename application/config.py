import os
from application import app

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = 'secrfgdgret'

app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://pc2019:86pyLKmc32wq%dsre32@mysql-server-1.macs.hw.ac.uk/pc2019'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
