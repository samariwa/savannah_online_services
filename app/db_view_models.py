from app import db

class DeliveryStaffView(db.Model):
    """DeliveryStaffView
    This is a view indicative of a delivery staff and their various orders
    it is called like any other  model only that it's a view.

    The best approach is to create these views when creating the db
    i.e in the makefile using the methods in the db_view_fxns.py file

    this file will hold all the methods of creating views so that we can
     use the db views without worrying about how they are created.

    The difficult part is getting rid of the views
    """
    __tablename__ = 'delivery_staff_view'
    id = db.Column(db.Integer)
    order_id = db.Column(db.Integer, nullable=False, primary_key=True)
