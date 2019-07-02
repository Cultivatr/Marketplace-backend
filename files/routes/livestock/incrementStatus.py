from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.Livestock import Livestock
from files.gauth import authorized

@app.route("/livestock/incrementStatus/", methods=['POST'])
@authorized
def update_livestock_items(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    data = request.get_json()
    filterId = data.get('id')
    liveToUpdate = db.session.query(Livestock).filter(
        Livestock.id == filterId).first()
    liveToUpdate.status = data.get('nextStatus')

    db.session.commit()
    return jsonify({"Success": True})