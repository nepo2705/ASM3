from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms import ValidationError
from model import User

# Biểu mẫu đăng nhập
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])  # Trường username vẫn được giữ lại
    email = StringField('Email', validators=[DataRequired(), Email()])  # Thêm trường email
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField('Log In')

# Biểu mẫu đăng ký
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])  # Email xác thực
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up!')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been already registered!')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is taken')

# Biểu mẫu thêm công việc mới
class AddForm(FlaskForm):
    category = StringField('Category', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Save')

# Biểu mẫu chỉnh sửa công việc
class EditForm(FlaskForm):
    category = StringField('Category', validators=[DataRequired()])
    status = StringField('Status', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Save')

# Biểu mẫu xóa công việc
class DelForm(FlaskForm):
    category = StringField('Category', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
