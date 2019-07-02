from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.Users import Users
from files.gauth import authorized

@app.route("/login/", methods=["POST"])
@authorized
def authenticate_login_user(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    data = request.get_json()
    loginEmail = data.get('email')
    user = db.session.query(Users).filter(
        Users.email == loginEmail.lower()).first()
    if user:
        user_data = {}
        user_data['id'] = user.id
        user_data['firstName'] = user.first_name
        user_data['lastName'] = user.last_name
        user_data['email'] = user.email
        user_data['farmName'] = user.farm_name
        user_data['isAdmin'] = user.is_admin
        return jsonify({'user': user_data})
    else:
        return 'Fail', 400