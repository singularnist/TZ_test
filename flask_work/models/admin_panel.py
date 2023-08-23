from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user, login_required, login_user, logout_user

from db_work import AdminUser, City, Country, Delivery, Product, Street,session_1
from .admin_view import AddressModelView, TestView

admin_page = Blueprint('login', __name__)
login_manager = LoginManager(admin_page)

@login_manager.user_loader
def load_user(user_id):
    return session_1.query(AdminUser).get(int(user_id))

@admin_page.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = session_1.query(AdminUser).filter_by(username=username).first()
        if user and user.verify_password(password):
            login_user(user)
            return redirect(url_for('admin.index'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')
@admin_page.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    @login_required
    def index(self):
        return super(MyAdminIndexView, self).index()


models = [Product, AdminUser,Country ,City, Street]
admin = Admin(admin_page, name='Adminka', template_mode='bootstrap3', index_view=MyAdminIndexView())
for model in models:
    admin.add_view(ModelView(model, session_1))
admin.add_view(TestView(name='DEV PAGE'))
admin.add_view(AddressModelView(Delivery, session_1))



