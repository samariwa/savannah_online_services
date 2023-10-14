from app import app
from app.controllers.create import create_expense_category
app.app_context().push()


create_expense_category(**{'expense_category': 'Transport'})
create_expense_category(**{'expense_category': 'Operational Expense'})
create_expense_category(**{'expense_category': 'Utility Bills'})
create_expense_category(**{'expense_category': 'Salaries'})
create_expense_category(**{'expense_category': 'Supplies'})
create_expense_category(**{'expense_category': 'Operating Licences'})