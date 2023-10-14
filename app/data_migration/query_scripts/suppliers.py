from app import app
from app.controllers.create import create_supplier
app.app_context().push()


create_supplier(**{'supplier_name': 'Sympha Farm', 'supplier_contact': '0721537929'})
create_supplier(**{'supplier_name': 'Victoria Farms', 'supplier_contact': '0725312186'})
create_supplier(**{'supplier_name': 'Masaku Standard Meat Suppliers', 'supplier_contact': '0701322921'})
create_supplier(**{'supplier_name': 'Huho Farm', 'supplier_contact': '0703820170'})
create_supplier(**{'supplier_name': 'Elim Gardens', 'supplier_contact': '0715281430'})
create_supplier(**{'supplier_name': 'Asami Packagers', 'supplier_contact': '0202016568'})
create_supplier(**{'supplier_name': 'Market', 'supplier_contact': '0000000000'})
create_supplier(**{'supplier_name': 'Tupet (Masai)', 'supplier_contact': '0722614904'})
create_supplier(**{'supplier_name': 'Juma Isatu (Goat Supplier)', 'supplier_contact': '0721592223'})
create_supplier(**{'supplier_name': 'Phem Seafood', 'supplier_contact': '0724776973'})
create_supplier(**{'supplier_name': 'Karanja Marikiti', 'supplier_contact': '0721639180'})
create_supplier(**{'supplier_name': 'George Matumbo', 'supplier_contact': '0720676757'})
create_supplier(**{'supplier_name': 'Spice World', 'supplier_contact': '0722895015'})
create_supplier(**{'supplier_name': 'Alpha Foods (Seafood)', 'supplier_contact': '0718549694'})
create_supplier(**{'supplier_name': 'Packaging Deliverer', 'supplier_contact': '0743450483'})
create_supplier(**{'supplier_name': 'Divine Business Minded', 'supplier_contact': '0788127881'})
