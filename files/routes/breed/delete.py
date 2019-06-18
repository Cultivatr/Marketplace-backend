from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.LivestockBreed import LivestockBreed
from files.gauth import authorized

# deletes the breed from the database
@app.route('/breed/delete/', methods=['POST'])
@authorized
def delete_breed(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    data = request.get_json()
    breed = data.get('breed')
    livestockId = data.get('livestockId')
    db.session.query(LivestockBreed).filter(
        LivestockBreed.livestock_id == livestockId
    ).filter(
        LivestockBreed.breed == breed).delete()
    db.session.commit()
    return 'Success', 201