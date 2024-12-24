from myproject import app,db
from flask import render_template,redirect,request,url_for,flash,abort
from flask_login import login_user,login_required,logout_user
from myproject.models import User
from myproject.forms import LoginForm,RegistrationForm


@app.route('/')
def home():
    return render_template('home.html')

# thiet lajp view chao mung nguoi dung sau khi dang nhap

@app.route('/welcome')
@login_required # dam bao rang user xem duoc thi ho phai dang nhap
def welcome_user():
    
    return render_template('welcome.html')

@app.route('/logout')
@login_required
def logout():
    
    logout_user()
    
    return redirect(url_for('home'))



@app.route('/login',methods = ['GET','POST'])
def login():
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first() #lay user dua tren email
        
        if user.check_password(form.password.data) and user is not None: # kiem tra xem user co thuc su duoc cung cap ko va mat khau co chinh xac ko
        
            login_user(user) #luu tru thong tin de nhan dien nguoi dung trong yeu cau tiep
        
            #flash la dung de gui di 1 thong bao cho user
        
            flash('Login success')
        
            next = request.args.get('next') # trang duoc yeu cau boi user, next chi xay ra neu user dang co truy cap vao 1 page ma user phai dang nhap de xem
        
            if next == None or not next[0] == '/': #kiem tra xem dieu do co ton tai hay ko, neu ko di den welcome page
                next = url_for('welcome_user')
            
            return redirect(next)
    return render_template('login.html',form = form)


@app.route('/register',methods = ['GET','POST'])
def register():
    
    form = RegistrationForm()
    
    if form.validate_on_submit():
        
        user = User(email = form.email.data, username = form.username.data, password=form.password.data)
        
        db.session.add(user)
        db.session.commit()
        
        flash("thank for regist")
        
        return redirect(url_for('login'))
    
    return render_template('register.html',form = form)

if __name__ == '__main__':
    app.run(debug=True)