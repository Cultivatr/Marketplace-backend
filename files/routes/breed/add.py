from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.LivestockBreed import LivestockBreed
from files.gauth import authorized

@app.route("/breed/add/", methods=['POST'])
@authorized
def add_new_breed(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    data = request.get_json()
    new_breed = LivestockBreed(
        livestock_id=data.get('livestockId'),
        breed=data.get('breed'))
    db.session.add(new_breed)
    db.session.commit()
    return jsonify({new_breed.livestock_id: new_breed.breed}), 201