from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.Produce import Produce
from files.db_models.Livestock import Livestock
from files.db_models.Users import Users
from files.gauth import authorized

@app.route("/admin/users/delete/", methods=['POST'])
@authorized
def delete_user(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    data = request.get_json()
    filterId = data.get('id')
    db.session.query(Produce).filter(Produce.user_id == filterId).delete()
    db.session.query(Livestock).filter(Livestock.user_id == filterId).delete()
    db.session.query(Users).filter(Users.id == filterId).delete()
    db.session.commit()
    return jsonify({"Success": True})