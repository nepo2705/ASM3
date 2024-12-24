from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import create_app, db
from model import User, Todo
from form import LoginForm, RegistrationForm, AddForm, EditForm

# Tạo app Flask
app = create_app()



# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def regis():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        user = User(email=email, username=username, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('regis.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            
            # Kiểm tra tham số 'next' trong URL
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)  # Chuyển hướng đến trang 'next' nếu có
            else:
                return redirect(url_for('homepage'))  # Nếu không có tham số 'next', chuyển hướng về homepage
        else:
            flash('Invalid email or password!', 'error')
    return render_template('login.html', form=form)
    




@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/homepage')
@login_required
def homepage():
    todos = Todo.query.filter_by(user_email=current_user.email).all()
    return render_template('homepage.html', todos=todos)


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = AddForm()
    if form.validate_on_submit():
        category = form.category.data
        description = form.description.data
        new_todo = Todo(
            category=category,
            description=description,
            status='Pending',
            date_created=int(datetime.timestamp(datetime.now())),
            user_email=current_user.email
        )
        db.session.add(new_todo)
        db.session.commit()
        flash('New task added successfully!', 'success')
        return redirect(url_for('homepage'))
    return render_template('add.html', form=form)

@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
@login_required
def edit(todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_email=current_user.email).first_or_404()
    form = EditForm(obj=todo)
    if form.validate_on_submit():
        todo.category = form.category.data
        todo.status = form.status.data
        todo.description = form.description.data
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('homepage'))
    return render_template('edit.html', form=form)

@app.route('/delete/<int:todo_id>', methods=['POST'])
@login_required
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_email=current_user.email).first_or_404()
    db.session.delete(todo)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('homepage'))

# Thêm bước khởi tạo cơ sở dữ liệu
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Tạo bảng nếu chưa tồn tại
    app.run(debug=True)
