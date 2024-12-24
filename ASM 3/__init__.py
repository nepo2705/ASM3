from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# Tạo các đối tượng chung
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Cấu hình ứng dụng
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Khởi tạo với app
    db.init_app(app)
    login_manager.init_app(app)

    # Thiết lập login view
    login_manager.login_view = 'login'

    # Đảm bảo User được import sau khi db được khởi tạo
    from model import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app