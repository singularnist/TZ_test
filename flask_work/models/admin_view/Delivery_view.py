from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.filters import BaseSQLAFilter

from db_work import City, Country, Street, session_1


class AddressModelView(ModelView):
    column_list = ['id', 'tovar.title', 'quantity', 'country_id', 'city_id', 'street_id',
                   'house', 'number', 'surname', 'user_name', 'stat', 'date']
    column_formatters = {
        'country_id': lambda v, c, m, p: m.country.country,
        'city_id': lambda v, c, m, p: m.city.city,
        'street_id': lambda v, c, m, p: m.street.street,
    }
    column_labels = {
        'country_id': 'Країна',
        'city_id': 'Місто',
        'street_id': 'Вулиця',
    }
    class FilterByCountry(BaseSQLAFilter):
        def apply(self, query, value, alias=None):
            return query.join(Country).filter(Country.id == value)
        def operation(self):
            return u'equals'
        def get_options(self, view):
            return [(country.id, country.country) for country in session_1.query(Country).order_by(Country.id)]

    class FilterByCity(BaseSQLAFilter):
        def apply(self, query, value, alias=None):
            return query.join(City).filter(City.id == value)
        def operation(self):
            return u'equals'
        def get_options(self, view):
            return [(city.id, city.city) for city in session_1.query(City).order_by(City.id)]

    class FilterByStreet(BaseSQLAFilter):
        def apply(self, query, value, alias=None):
            return query.join(Street).filter(Street.id == value)
        def operation(self):
            return u'equals'
        def get_options(self, view):
            return [(street.id, street.street) for street in session_1.query(Street).order_by(Street.id)]

    column_filters = [FilterByCountry(column='Країна', name='Країна'),
        FilterByCity(column='Місто', name='Місто'),
        FilterByStreet(column='Вулиця', name='Вулиця')]

    def on_model_change(self, form, model, is_created):
        super(AddressModelView, self).on_model_change(form, model, is_created)

        if is_created:
            # Якщо запис створюється, виводимо повідомлення
            message = f"Створено замовлення id {model.id}, статус {model.stat}"
            print(message)


    def on_model_delete(self, model):

        super(AddressModelView, self).on_model_delete(model)
        message = f"Замовлення id {model.id} видалено"
        print(message)
    
    
class TestView(BaseView):
    @expose('/')
    def deliv_page(self):
        countrys = session_1.query(Country).all()
        citys = session_1.query(City).all()
        streets = session_1.query(Street).all()
        return self.render('admin/delivery_admin.html',countrys=countrys, citys=citys,streets=streets)
