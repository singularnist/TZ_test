import os

from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from flask_jsonrpc import JSONRPC
from db_work import Delivery, session_1
from typing import Dict, Union
from flask_login import LoginManager, login_required, current_user,login_user, logout_user
from dotenv import load_dotenv

endpoint = Blueprint('endpoint', __name__)
jsonrpc = JSONRPC()
login_manager = LoginManager()
load_dotenv()

@jsonrpc.method('delivery.get_order_details', validate=True) 
def get_order_details(order_id: int) -> Dict[str, Union[int, str]]:
    try:
        order = session_1.query(Delivery).get(order_id)
        if order:
            return {
                'id': order.id,
                'product_name': order.tovar.title,
                'quantity': order.quantity,
                'country': order.country.country,
                'city': order.city.city,
                'street': order.street.street,
                'house': order.house,
                'number': order.number,
                'surname': order.surname,
                'user_name': order.user_name,
                'status': order.stat,
                'date': order.date.strftime('%Y-%m-%d %H:%M:%S')
            }
        else:
            return {'error': 'Order not found'}
    except Exception as e:
        return {'error': str(e)}

us_pass,us_name = os.getenv('US_NAME'),os.getenv('US_PASS')
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

@endpoint.route('/')
def index():
    return render_template('aunt.html')

@endpoint.route('/user',  methods=['GET', 'POST'])
def user():
    if 'username' in session:
        if request.method =='POST':
            order_id = int(request.form['order_id'])
            try:
                response = get_order_details(order_id)
                return render_template('user.html', order_details=response)
            except Exception as e:
                return render_template('end.html', order_details={'error': str(e)})
        else:
            return render_template('end.html')
    else:
        return redirect(url_for('profile'))