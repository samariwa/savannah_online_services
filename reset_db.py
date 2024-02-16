#!/usr/bin/python3

from app.controllers import create
from app.general_functions import get_uuid, generate_random_string
from app import app, db
app.app_context().push()


db.drop_all()
db.create_all()


create.create_user(first_name='John', last_name= 'Kimani', user_status='active', email_address='superuser@savannah.com', password='3opf@mAxuU$eCujQRZQXGk#8S')
create.create_user(first_name='John', last_name= 'Beanzzzzz', email_address='samuelmariwa@gmail.com', password='abc123')

# create customer since orders need customers
customer_kw1 = {
    'customer_code': get_uuid(),
    'first_name': 'John',
    'last_name': 'Kimani',
    'phone_no': '+254798989898',
}
create.create_customer(**customer_kw1)
# create credit_customers
customer_kw2 = {
    'customer_code': get_uuid(),
    'first_name': 'Mrs',
    'last_name': 'Kimani',
    'phone_no': '+254798989333',
}
create.create_customer(**customer_kw2)

customer_kw3 = {
    'customer_code': get_uuid(),
    'first_name': 'Mr',
    'last_name': 'Beanzzzzz',
    'phone_no': '+254798989533',
}
create.create_customer(**customer_kw3)

# create orders
order_kw = {
    'customer_id': 2,
    'order_ref':generate_random_string(8),
    'amount': 50,
    'time': "12:00",
}

create.create_order(**order_kw)