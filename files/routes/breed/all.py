from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.LivestockBreed import LivestockBreed
from files.gauth import authorized

@app.route('/breed/all/', methods=['GET'])
@authorized
def get_all_breed(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    breeds = db.session.query(LivestockBreed)
    output = []
    for breed in breeds:
        breed_data = {}
        breed_data[breed.livestock_id] = breed.breed
        output.append(breed_data)

    return jsonify({'breed': output})