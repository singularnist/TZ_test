from flask import Blueprint, render_template

from db_work import Product, session_1

golovna_md = Blueprint('/', __name__)

@golovna_md.route('/')
def katalog():
    articles = session_1.query(Product).order_by(Product.date.desc()).all()
    return render_template('index.html', articles=articles)