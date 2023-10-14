#!/usr/bin/python3

from app.controllers import create
from app import app, db
app.app_context().push()


db.drop_all()


db.create_all()

#create department
department_kwargs = {
    'department': 'ICT',
}
create.create_department(**department_kwargs)

department_kwargs = {
    'department': 'administration',
}
create.create_department(**department_kwargs)

# create staff role
staff_role_kwargs = {
    'department_id': 1,
    'role': "SuperUser",
}
create.create_staff_role(**staff_role_kwargs)

staff_role_kwargs = {
    'department_id': 2,
    'role': "Admin",
}
create.create_staff_role(**staff_role_kwargs)


# then create staff
staff_kwargs = {
    'role_id': 1, # superuser
    'first_name': "CIFOR",
    'last_name': "ICRAF",
    'id_number': "00000000",
    'yob': 2022,
    'gender': 'male',
    'nssf_number': '00000000',
    'nhif_number': '00000000',
}
create.create_staff(**staff_kwargs)

# then create staff
staff_kwargs = {
    'role_id': 2, # admin
    'first_name': "Mariwa",
    'last_name': "Administrators",
    'id_number': "100237",
    'yob': 1994,
    'gender': 'male',
    'nssf_number': '254125100',
    'nhif_number': '254100',
}

create.create_staff(**staff_kwargs)


create.create_user(staff_id=1, user_status='active', email_address='superuser@cifor-icraf.org', password='3opf@mAxuU$eCujQRZQXGk#8S')
create.create_user(staff_id=2, user_status='inactive', email_address='mariwa@cifor-icraf.org', password='abc123')

