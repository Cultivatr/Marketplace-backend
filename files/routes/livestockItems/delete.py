from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.LivestockItems import LivestockItems
from files.db_models.LivestockBreed import LivestockBreed
from files.gauth import authorized

# deletes all livestock and breeds
@app.route("/livestockItems/delete/", methods=['POST'])
@authorized
def delete_livestock_selection_item(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    data = request.get_json()
    filterId = data.get('itemToDelete')
    livestockId = db.session.query(LivestockItems.id).filter(
        LivestockItems.item == filterId).one()[0]
    db.session.query(LivestockBreed).filter(
        LivestockBreed.livestock_id == livestockId).delete()
    db.session.query(LivestockItems).filter(
        LivestockItems.item == filterId).delete()
    db.session.commit()
    return 'Success', 201