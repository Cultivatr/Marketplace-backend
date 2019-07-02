from flask import current_app as app, request, jsonify
from files.gauth import authorized
import files.email_system as email
from files.db_models.Users import Users

try:
    from __main__ import global_vars
except:
    from app import global_vars

db = global_vars.db

@app.route("/email/new_item/", methods=['POST'])
@authorized
def send_email_new_item(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    data = request.get_json()
    user_email = data.get('email')
    farmer = db.session.query(Users).filter(Users.email == user_email).first()
    email.send_email_new_item(farmer.farm_name)
    return jsonify({"Success": True})