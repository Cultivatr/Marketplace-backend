from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.ProduceItems import ProduceItems
from files.gauth import authorized

@app.route("/produceItems/delete/", methods=['POST'])
@authorized
def delete_produce_selection_item(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    data = request.get_json()
    filterId = data.get('itemToDelete')
    db.session.query(ProduceItems).filter(
        ProduceItems.item == filterId).delete()
    db.session.commit()
    return 'Success', 201