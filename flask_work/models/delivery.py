from flask import Blueprint, render_template, request

from db_work import City, Country, Delivery, Product, Street, session_1
from cel import compare_values

deliv_md = Blueprint('delivery_blueprint', __name__)

@deliv_md.route('/delivery/<int:id>',  methods=['POST', 'GET'])
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
        deliv=Delivery(tovar_id=id,quantity=quantity,country_id=country,city_id=city,street_id=street,house=house,number=number1,surname=surname,user_name=user_name,stat='Обробляється')
        try:
            session_1.add(deliv)
            session_1.commit()
            # compare_values.delay(deliv.id, deliv.stat)
            return f'Ваше замовлення {deliv.id}'
            
        except Exception as e:
            print(str(e))
            return 'При виконанні сталась помилка'
    else:
        article = session_1.query(Product).get(id)
        return render_template('delivery.html', article=article, countrys=countrys,citys=citys,streets=streets)