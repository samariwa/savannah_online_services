#!/usr/bin/python3

from app.controllers import create
from app import app, db
app.app_context().push()


db.drop_all()


db.create_all()

#create department
department_kwargs = {
    'department': 'Software',
}
create.create_department(**department_kwargs)

#create department
department_kwargs = {
    'department': 'ICT',
}
create.create_department(**department_kwargs)

department_kwargs = {
    'department': 'PMU',
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
    'first_name': "Super",
    'last_name': "User",
}
create.create_staff(**staff_kwargs)

# then create staff
staff_kwargs = {
    'role_id': 2, # admin
    'first_name': "Samuel",
    'last_name': "Mariwa",
}

create.create_staff(**staff_kwargs)


create.create_user(staff_id=1, user_status='active', email_address='superuser@cifor-icraf.org', password='3opf@mAxuU$eCujQRZQXGk#8S')
create.create_user(staff_id=2, user_status='inactive', email_address='s.mariwa@cifor-icraf.org', password='abc123')

