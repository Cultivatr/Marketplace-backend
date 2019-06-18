from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.LivestockBreed import LivestockBreed
from files.gauth import authorized

@app.route('/breed/<livestockId>/', methods=['GET'])
@authorized
def get_breeds_with_id(livestockId, idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    breeds = db.session.query(LivestockBreed).filter(
        LivestockBreed.livestock_id == livestockId).all()
    output = []
    for breed in breeds:
        output.append(breed.breed)
    return jsonify({livestockId: output})