from app import db


def create_delivery_staff_view():
    """create_delivery_staff_view
    Once you call this function and create the table on the db,
    you create the Model
    """
    selectable = db.select(
        db.Table('staff').c.id,
        db.Table('deliveries').c.order_id).select_from(
            db.Table('deliveries').join(db.Table('staff'))
    )
    db.session.execute(db.text(
        # (mysql) "CREATE VIEW IF NOT EXISTS delivery_staff_view AS " + str(selectable)
        "CREATE OR REPLACE VIEW delivery_staff_view AS " + str(selectable)
    ))
    db.session.commit()


def delete_delivery_staff_view():
    """delete_delivery_staff_view
    Used to clear the db when doing a reset
    for Postgresql:
    DROP VIEW IF EXISTS customer_info;
    """
    db.session.execute(db.text("DROP VIEW IF EXISTS delivery_staff_view"))
    db.session.commit()
