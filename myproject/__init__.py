import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#tao ung dung

login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite;///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)


#cau hinh ung dung cua ban de co quyen quan ly nguoi dung dang nhap

login_manager.init_app(app)

#cho nguoi dung biet view ma ho se truy cap khi dang nhap

login_manager.login_view = 'login' #trong file app.py hoac thiet lap view se co mot view duoc goi la 'login'
                                    # lien ket dieu nay voi login_manager



