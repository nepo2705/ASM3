# thiet lap bieu mau de nguoi dung dang nhap va dang ky website

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo  #data required la khong the de truong cu the trong 1 bieu mau trong, 
                                                            #email check de dam bao rang ban dang thuc su dung email
                                                            #equal to dung de xac nhan mat khau
from wtforms import ValidationError

# tao bieu mau dang ky

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()]) #kiem tra xem dung dinh dang email ko
    password = PasswordField("password",validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    
    email = StringField('Email',validators = [DataRequired(),Email()]) #email xac thuc se kiem tra xem do co phai la email thuc hay khong
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm', message = 'Passwords must match')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register!')
    
    def check_email(self,field): #kiem tra xem email cua user co ton tai hay khong
        if User.query.filter_by(email = field.data).first(): #kiem tra xem email do da duoc kich hoat va dang ki chua
            raise ValidationError('Your email has been already registered!')
        
    def check_username(self,field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('Username is taken')
            
    