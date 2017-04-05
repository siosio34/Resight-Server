from resightserver import app
from flask_sqlalchemy import SQLAlchemy

# TODO 환경설정 하는것을 배워야한다.

app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db_instance = SQLAlchemy(app)

from models import *
db_instance.create_all()