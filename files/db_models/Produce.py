try:
    from __main__ import global_vars
except:
    from app import global_vars

db = global_vars.db

class Produce(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='RESTRICT', onupdate='CASCADE'),
        nullable=False
    )
    product_name = db.Column(db.Text)
    package_type = db.Column(db.Text)
    package_size = db.Column(db.Integer)
    package_size_unit = db.Column(db.Text)
    est_completion_date = db.Column(db.Date)
    seed_type = db.Column(db.Text)
    modified_seed = db.Column(db.Text)
    heirloom = db.Column(db.Text)
    fertilizer_type_used = db.Column(db.Text)
    pesticide_type_used = db.Column(db.Text)
    estimated_qty_planted = db.Column(db.Integer)
    certified_organic = db.Column(db.Text)
    estimated_finished_qty = db.Column(db.Integer)
    est_price_to_be_paid = db.Column(db.Float)
    qty_accepted_for_listing = db.Column(db.Integer)
    qty_accepted_at_delivery = db.Column(db.Integer)
    chargebacks = db.Column(db.Integer)
    price_paid = db.Column(db.Float)
    created_date = db.Column(db.Date)
    accepted_date = db.Column(db.Date)
    sold_date = db.Column(db.Date)
    delivered_date = db.Column(db.Date)
    delivered_to = db.Column(db.Text)
    comments = db.Column(db.Text)
    status = db.Column(db.Text)