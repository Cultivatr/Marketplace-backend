try:
    from __main__ import global_vars
except:
    from app import global_vars

db = global_vars.db

from sqlalchemy.schema import UniqueConstraint

class LivestockBreed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    livestock_id = db.Column(db.Integer, db.ForeignKey('livestock_items.id'))
    breed = db.Column(db.String(50))
    UniqueConstraint('breed', 'livestock_id', name='breed_id_constraint')