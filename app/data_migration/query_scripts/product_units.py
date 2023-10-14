from app import app
from app.controllers.create import create_product_unit
app.app_context().push()


create_product_unit(**{'unit_name': 'None'})
create_product_unit(**{'unit_name': 'Litre(s)'})
create_product_unit(**{'unit_name': 'Packs'})
create_product_unit(**{'unit_name': 'Packets'})
create_product_unit(**{'unit_name': 'Dozen'})
create_product_unit(**{'unit_name': 'Box'})
create_product_unit(**{'unit_name': 'Sachets'})
create_product_unit(**{'unit_name': 'Tins'})
create_product_unit(**{'unit_name': 'Containers'})
create_product_unit(**{'unit_name': 'Kilogram(s)', 'measurement_mode': 'weight'})
create_product_unit(**{'unit_name': 'Bags'})
create_product_unit(**{'unit_name': 'Rolls'})
create_product_unit(**{'unit_name': 'Pieces'})
create_product_unit(**{'unit_name': 'Bundles'})
create_product_unit(**{'unit_name': 'Trays'})
create_product_unit(**{'unit_name': 'Eggs'})
create_product_unit(**{'unit_name': 'Bunches'})
create_product_unit(**{'unit_name': 'Punnet(s)'})
create_product_unit(**{'unit_name': 'Jar(s)'})
