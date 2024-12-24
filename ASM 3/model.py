# set up de chua nguoi dung trong database

from __init__ import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from __init__ import db



#cho phep Flask_login tai nguoi dung hien tai va id cua ho
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model,UserMixin):
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())
    username = db.Column(db.String())
    password = db.Column(db.String())
    todos = relationship('Todo', back_populates = 'user')

    def __init__(self,email,username,password):
        
        self.email = email
        self.username = username
        self.password = password
        
    def check_password(self, password):
        return check_password_hash(self.password, password)

class Todo(db.Model): #usermixin co tat ca cac tinh nang quan ly dang nhap cho nguoi dung va cap quyen cho user
    
    __tablename__ = 'Todos'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String())
    description = db.Column(db.String())
    status = db.Column(db.String())
    date_created = db.Column(db.Integer())
    user_email = db.Column(db.String(120), db.ForeignKey('users.email'))
    user = relationship("User", back_populates="todos")
    
    
     
    def __init__(self,category,description,status,date_created, user_email):
        
        self.category = category
        self.description = description
        self.status = status
        self.date_created = date_created
        self.user_email = user_email
        

        

        
        