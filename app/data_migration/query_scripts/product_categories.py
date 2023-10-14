from app import app
from app.controllers.create import create_product_category
app.app_context().push()

create_product_category(**{'category_name': 'Chicken Products'})
create_product_category(**{'category_name': 'Fish'})
create_product_category(**{'category_name': 'Vegetables'})
create_product_category(**{'category_name': 'Meat'})
create_product_category(**{'category_name': 'Packaging'})
create_product_category(**{'category_name': 'Fruits'})
create_product_category(**{'category_name': 'Cooked Food'})
create_product_category(**{'category_name': 'Flour'})
create_product_category(**{'category_name': 'Spices'})
