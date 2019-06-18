try:
    from __main__ import global_vars
except:
    from app import global_vars

db = global_vars.db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text, nullable=False)
    primary_phone = db.Column(db.Text, nullable=False)
    secondary_phone = db.Column(db.Text)
    email = db.Column(db.Text, nullable=False)
    farm_name = db.Column(db.Text, nullable=False)
    farm_location = db.Column(db.Text)
    area = db.Column(db.Text)
    # is_producer & is_other are no longer being used.
    is_producer = db.Column(db.Boolean)
    is_admin = db.Column(db.Boolean)
    is_other = db.Column(db.Boolean)
    member_since = db.Column(db.Date)
    farm_type = db.Column(db.Text)
    rating = db.Column(db.Integer)
    mailing_street = db.Column(db.Text)
    mailing_city = db.Column(db.Text)
    mailing_province = db.Column(db.Text)
    mailing_country = db.Column(db.Text)
    mailing_postal_code = db.Column(db.Text)
    billing_street = db.Column(db.Text)
    billing_city = db.Column(db.Text)
    billing_province = db.Column(db.Text)
    billing_country = db.Column(db.Text)
    billing_postal_code = db.Column(db.Text)
    user_comments = db.Column(db.Text)