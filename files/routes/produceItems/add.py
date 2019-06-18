from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.ProduceItems import ProduceItems
from files.gauth import authorized

@app.route("/produceItems/add/", methods=['POST'])
@authorized
def add_new_produce_item(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    data = request.get_json()
    new_p_item = ProduceItems(
        item=data.get('newItem'))
    db.session.add(new_p_item)
    db.session.commit()

    return jsonify({'name': new_p_item.item}), 201