from flask import Flask
from flask_jsonrpc import JSONRPC
from dotenv import load_dotenv
from .models import golovna_md, deliv_md,admin,admin_page,login_manager, endpoint,jsonrpc,admin_page, deliv_md, golovna_md 
from .models.admin_panel import admin, admin_page, login_manager


app = Flask('project')
app.config['SECRET_KEY'] = 'your-secret-key'

load_dotenv()

#Головна сторінка 
app.register_blueprint(golovna_md)

#Сторінка доставки
app.register_blueprint(deliv_md)

#Ендпоїнт для користувачів
app.register_blueprint(endpoint, url_prefix='/profile')
jsonrpc.init_app(app)

#Адмін панель
app.register_blueprint(admin_page)
login_manager.init_app(app)
admin.init_app(app)






