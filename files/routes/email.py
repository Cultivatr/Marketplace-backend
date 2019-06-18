from flask import current_app as app
from files.gauth import authorized
import files.email_system

@app.route("/email/", methods=['POST'])
@authorized
def send_email_alert(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    data = request.get_json()
    farm_name = data.get('farmName')
    user_email = data.get('email')

    email_system.send_email(farm_name, user_email)
    return jsonify({"Success": True})