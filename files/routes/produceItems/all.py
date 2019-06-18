from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.ProduceItems import ProduceItems
from files.gauth import authorized

@app.route('/produceItems/all/', methods=['GET'])
@authorized
def get_indiv_produce_items(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    p_items = db.session.query(ProduceItems)
    output = []
    for p_item in p_items:
        p_item_data = {}
        p_item_data['newItem'] = p_item.item
        output.append(p_item_data)

    return jsonify({'produce_items': output})