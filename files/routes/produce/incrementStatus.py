from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.Produce import Produce
from files.gauth import authorized

@app.route("/produce/incrementStatus/", methods=['POST'])
@authorized
def update_produce_items(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    data = request.get_json()
    filterId = data.get('id')
    prodToUpdate = db.session.query(Produce).filter(
        Produce.id == filterId).first()
    prodToUpdate.status = data.get('nextStatus')
    db.session.commit()
    return jsonify({"Success": True})