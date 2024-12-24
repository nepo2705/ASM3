# set up de chua nguoi dung trong database

from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


#cho phep Flask_login tai nguoi dung hien tai va id cua ho
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)




class User(db.Model,UserMixin): #usermixin co tat ca cac tinh nang quan ly dang nhap cho nguoi dung va cap quyen cho user
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(64),unique = True,index = True) #gioi han do dai chuoi, dat unique de tranh viec hai user khac nhau co cung email
    username = db.Column(db.String(64),unique = True,index = True) 
    
    #luu phien ban bam cua mat khau
    password_hash = db.Column(db.String(128))
     
    def __init__(self,email,username,password):
        self.email = email
        self.username = username 
        self.password_hash = generate_password_hash(password) # vi khong muon luu chuoi pass ma user nhap nen se luu ban bam cua no
        
    #kiem tra thoi diem nguoi dung dang nhap, xac minh nguoi dung
    
    def check_password(self,password):
        return check_password_hash(self.password_hash,password) #su dung ham chec_password_hash de kiem tra xem password nhap vao co khop voi hash duoc luu hay khong