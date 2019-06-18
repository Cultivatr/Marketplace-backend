try:
    from __main__ import global_vars
except:
    from app import global_vars

db = global_vars.db

class ProduceItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(50), unique=True)