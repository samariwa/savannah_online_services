from app.controllers.create import create_department
create_department(**{'id': 1, 'department': 'ICT', 'db_status': 'active', 'created_at': '2023-07-28 06:40:09', 'updated_at': None})
create_department(**{'id': 2, 'department': 'sales', 'db_status': 'active', 'created_at': '2023-07-28 06:40:09', 'updated_at': None})
create_department(**{'id': 3, 'department': 'logistics', 'db_status': 'active', 'created_at': '2023-07-28 06:40:09', 'updated_at': None})
create_department(**{'id': 4, 'department': 'administration', 'db_status': 'active', 'created_at': '2023-07-28 06:40:09', 'updated_at': None})
from app.controllers.create import create_staff_role
create_staff_role(**{'id': 1, 'department_id': 1, 'role': 'SuperUser', 'db_status': 'active', 'created_at': '2023-07-28 06:40:09', 'updated_at': None})
create_staff_role(**{'id': 2, 'department_id': 2, 'role': 'Admin', 'db_status': 'active', 'created_at': '2023-07-28 06:40:09', 'updated_at': None})
create_staff_role(**{'id': 3, 'department_id': 3, 'role': 'Delivery', 'db_status': 'active', 'created_at': '2023-07-28 06:40:09', 'updated_at': None})
create_staff_role(**{'id': 4, 'department_id': 4, 'role': 'Cashier', 'db_status': 'active', 'created_at': '2023-07-28 06:40:09', 'updated_at': None})
from app.controllers.create import create_staff
create_staff(**{'id': 1, 'role_id': 1, 'first_name': 'Sympha', 'last_name': 'Fresh', 'id_number': '00000000', 'yob': 2022, 'gender': 'male', 'nssf_number': '00000000', 'nhif_number': '00000000', 'db_status': 'active', 'created_at': '2023-07-28 06:40:09', 'updated_at': None})
create_staff(**{'id': 2, 'role_id': 2, 'first_name': 'Mariwa', 'last_name': 'Administrators', 'id_number': '100237', 'yob': 1994, 'gender': 'male', 'nssf_number': '254125100', 'nhif_number': '254100', 'db_status': 'active', 'created_at': '2023-07-28 06:40:09', 'updated_at': None})
create_staff(**{'id': 3, 'role_id': 3, 'first_name': 'Hodari', 'last_name': 'Deliveries', 'id_number': '125126', 'yob': 1995, 'gender': 'male', 'nssf_number': '254125126', 'nhif_number': '254125', 'db_status': 'active', 'created_at': '2023-07-28 06:40:09', 'updated_at': None})
from app.controllers.create import create_customer
create_customer(**{'id': 0, 'first_name': 'Unregistered', 'last_name': 'Customer', 'location': 'N/A', 'phone_no': 'N/A', 'customer_type': 'online', 'note': 'Add Note...', 'customer_status': 'active', 'credit_customer': 0, 'db_status': 'active', 'created_at': '2023-07-28 06:40:09', 'updated_at': None})
create_customer(**{'id': 1, 'first_name': 'John', 'last_name': 'Kimani', 'location': 'Around', 'phone_no': '0798989898', 'customer_type': 'online', 'note': 'Add Note...', 'customer_status': 'active', 'credit_customer': 0, 'db_status': 'active', 'created_at': '2023-07-28 06:40:09', 'updated_at': None})
create_customer(**{'id': 2, 'first_name': 'Mrs', 'last_name': 'Kimani', 'location': 'Around2', 'phone_no': '0798989333', 'customer_type': 'online', 'note': 'Add Note...', 'customer_status': 'active', 'credit_customer': 1, 'db_status': 'active', 'created_at': '2023-07-28 06:40:09', 'updated_at': None})
create_customer(**{'id': 3, 'first_name': 'Mr', 'last_name': 'Beanzzzzz', 'location': 'Around4', 'phone_no': '0798989533', 'customer_type': 'online', 'note': 'Add Note...', 'customer_status': 'active', 'credit_customer': 1, 'db_status': 'active', 'created_at': '2023-07-28 06:40:09', 'updated_at': None})
from app.controllers.create import create_user
create_user(**{'id': 1, 'customer_id': None, 'staff_id': 1, 'user_status': 'active', 'email_address': 'superuser@symphafresh.com', 'login_status': 0, 'last_activity': '2023-07-28 06:40:10', 'login_attempts': 0, 'db_status': 'active', 'created_at': '2023-07-28 06:40:10', 'updated_at': None})
create_user(**{'id': 2, 'customer_id': None, 'staff_id': 2, 'user_status': 'inactive', 'email_address': 'mariwa@sympha.com', 'login_status': 0, 'last_activity': '2023-07-28 06:40:10', 'login_attempts': 0, 'db_status': 'active', 'created_at': '2023-07-28 06:40:10', 'updated_at': None})
create_user(**{'id': 3, 'customer_id': None, 'staff_id': 3, 'user_status': 'inactive', 'email_address': 'hodari@sympha.com', 'login_status': 0, 'last_activity': '2023-07-28 06:40:10', 'login_attempts': 0, 'db_status': 'active', 'created_at': '2023-07-28 06:40:10', 'updated_at': None})
