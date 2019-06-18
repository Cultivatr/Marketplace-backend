try:
    from __main__ import global_vars
except:
    from app import global_vars

db = global_vars.db

class Livestock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='RESTRICT', onupdate='CASCADE'),
        nullable=False
    )
    product_name = db.Column(db.Text)
    breed = db.Column(db.Text)
    single_brand = db.Column(db.Text)
    est_birthdate = db.Column(db.Date)
    registration_number = db.Column(db.Float)
    rfid_tag = db.Column(db.Integer)
    starting_weight = db.Column(db.Integer)
    hanging_weight = db.Column(db.Integer)
    chargebacks = db.Column(db.Integer)
    starting_date_of_feed = db.Column(db.Date)
    feed_method = db.Column(db.Text)
    type_of_pasture = db.Column(db.Text)
    type_of_feed = db.Column(db.Text)
    est_completion_date = db.Column(db.Date)
    est_finished_weight = db.Column(db.Integer)
    est_price_to_be_paid = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    comments = db.Column(db.Text)
    price_paid = db.Column(db.Integer)
    created_date = db.Column(db.Date)
    accepted_date = db.Column(db.Date)
    sold_date = db.Column(db.Date)
    delivered_date = db.Column(db.Date)
    delivered_to = db.Column(db.Text)
    status = db.Column(db.Text)