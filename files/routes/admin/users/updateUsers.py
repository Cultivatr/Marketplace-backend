from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.Users import Users
from files.gauth import authorized

@app.route("/admin/updateUsers/", methods=['POST'])
@authorized
def modify_user(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    data = request.get_json()
    filterId = data.get('id')
    userToUpdate = db.session.query(Users).filter(Users.id == filterId).first()
    userToUpdate.first_name = data.get('firstName'),
    userToUpdate.last_name = data.get('lastName'),
    userToUpdate.primary_phone = data.get('primaryNumber'),
    userToUpdate.secondary_phone = data.get('secondaryNumber'),
    userToUpdate.email = data.get('email'),
    userToUpdate.farm_name = data.get('farmName'),
    userToUpdate.farm_location = data.get('farmLocation'),
    userToUpdate.area = data.get('area'),
    userToUpdate.is_admin = data.get('isAdmin')
    if(not data.get('isAdmin')):
        userToUpdate.is_admin = 0
    if(data.get('isAdmin')):
        userToUpdate.is_admin = 1
    # userToUpdate.is_admin=data.get('isAdmin'),
    # userToUpdate.is_producer=bool(data.get('isProducer')),
    # userToUpdate.is_other=bool(data.get('isOther')),
    userToUpdate.farm_type = data.get('farmType'),
    userToUpdate.rating = data.get('rating'),
    userToUpdate.mailing_street = data.get('mailingAddressStreet'),
    userToUpdate.mailing_city = data.get('mailingAddressCity'),
    userToUpdate.mailing_province = data.get('mailingAddressProvince'),
    userToUpdate.mailing_country = data.get('mailingAddressCountry'),
    userToUpdate.mailing_postal_code = data.get('mailingAddressPostalCode'),
    userToUpdate.billing_street = data.get('billingAddressStreet'),
    userToUpdate.billing_city = data.get('billingAddressCity'),
    userToUpdate.billing_province = data.get('billingAddressProvince'),
    userToUpdate.billing_country = data.get('billingAddressCountry'),
    userToUpdate.billing_postal_code = data.get('billingAddressPostalCode'),
    userToUpdate.user_comments = data.get('comments')
    db.session.commit()
    return jsonify({"Success": True})