from flask import current_app as app, request, jsonify
from files.gauth import authorized
import files.email_system as email

@app.route("/email/item_status/", methods=['POST'])
@authorized
def send_email_item_status(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    data = request.get_json()
    farm_name = data.get('farmName')
    user_email = data.get('email')

    email.send_email_item_status(farm_name, user_email)
    return jsonify({"Success": True})