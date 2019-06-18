from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.LivestockItems import LivestockItems
from files.gauth import authorized

@app.route("/livestockItems/add/", methods=['POST'])
@authorized
def add_new_livestock_item(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 40
    data = request.get_json()
    new_p_item = LivestockItems(
        item=data.get('newItem'))
    db.session.add(new_p_item)
    db.session.commit()

    return jsonify({'name': new_p_item.item}), 201