from flask import Flask, render_template, url_for, request, redirect, session, flash
from db_work import session_1,Delivery, Product, Country, City,Street, AdminUser
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, login_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, AdminIndexView, expose
from cel import compare_values
from pr_con import us_name, us_pass
from flask_jsonrpc import JSONRPC


app = Flask('project')
login_manager = LoginManager(app)
app.config['SECRET_KEY'] = 'your-secret-key'
jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)
#Каталог
@app.route('/')
def katalog():
    articles = session_1.query(Product).order_by(Product.date.desc()).all()
    return render_template('index.html', articles=articles)

def authenticate(username: str, password: str) -> bool:
    if username == us_name and password == us_pass: 
        return True
    return False

# Декоратор для JSON-RPC методу авторизації
def authenticate(username: str, password: str) -> bool:
    if username == us_name and password == us_pass: 
        return True
    return False

# Декоратор для JSON-RPC методу авторизації
@jsonrpc.method('login')
def login(username: str, password: str) -> bool:
    if authenticate(username, password):
        session['username'] = username
        return True
    else:
        return False

# Маршрут для сторінки авторизації
@app.route('/profile')
def index():
    return render_template('aunt.html')

# Маршрут для сторінки користувача
@app.route('/user',  methods=['GET', 'POST'])
def user():
    if 'username' in session:
        if request.method =='POST':
            id_del = request.form['order_id']
            delivery = session_1.query(Delivery).get(id_del)
            return render_template('user.html', delivery=delivery)
        else:
            return render_template('user.html')
    else:
        return redirect(url_for('profile'))

#Сторінка оформелення замовлення
@app.route('/delivery/<int:id>',  methods=['POST', 'GET'])
def delivery(id):
    article = session_1.query(Product).get(id)
    countrys = session_1.query(Country).all()
    citys = session_1.query(City).all()
    streets = session_1.query(Street).all()
    if request.method =='POST':
        quantity = request.form['quantity']
        country = int(request.form['country'])
        city = int(request.form['city'])
        street = int(request.form['street'])
        house = request.form['house']
        number1=request.form['number']
        surname = request.form['surname']
        user_name=request.form['user_name']
        title= article.title
        color= article.color
        weight= article.weight
        price = article.price
        deliv=Delivery(quantity=quantity,country_id=country,city_id=city,street_id=street,house=house,number=number1,surname=surname,user_name=user_name, title=title,color=color,weight=weight,price=price,stat='Обробляється')
        try:
            session_1.add(deliv)
            session_1.commit()
            compare_values.delay(deliv.id, deliv.stat)
            return f'Ваше замовлення {deliv.id}'
            
        except Exception as e:
            print(str(e))
            return 'При виконанні сталась помилка'
    else:
        article = session_1.query(Product).get(id)
        return render_template('delivery.html', article=article, countrys=countrys,citys=citys,streets=streets)

#Адмін панель
@login_manager.user_loader
def load_user(user_id):
    return session_1.query(AdminUser).get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
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

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    @login_required
    def index(self):
        return super(MyAdminIndexView, self).index()

models = [Product, AdminUser, Country, City, Street]
admin = Admin(app, name='Admin Panel', template_mode='bootstrap3', index_view=MyAdminIndexView())
for model in models:
    admin.add_view(ModelView(model, session_1))

class YourModelView(ModelView):
    column_filters = ('country', 'city', 'street')
admin.add_view(YourModelView(Delivery, session_1))
