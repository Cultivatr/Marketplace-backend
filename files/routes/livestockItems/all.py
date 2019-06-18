from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.LivestockItems import LivestockItems
from files.gauth import authorized

@app.route('/livestockItems/all/', methods=['GET'])
@authorized
def get_indiv_livestock_items(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    p_items = db.session.query(LivestockItems)
    output = []
    for p_item in p_items:
        print(p_item)
        p_item_data = {}
        p_item_data[p_item.id] = p_item.item
        output.append(p_item_data)

    return jsonify({'livestock_items': output})