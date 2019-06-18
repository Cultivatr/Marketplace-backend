from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.Users import Users
from files.gauth import authorized

@app.route('/admin/users/', methods=['GET'])
@authorized
def get_users(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401 
    users = db.session.query(Users)
    output = []
    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['firstName'] = user.first_name
        user_data['lastName'] = user.last_name
        user_data['primaryNumber'] = user.primary_phone
        user_data['secondaryNumber'] = user.secondary_phone
        user_data['email'] = user.email
        user_data['farmName'] = user.farm_name
        user_data['farmLocation'] = user.farm_location
        user_data['area'] = user.area
        user_data['isProducer'] = user.is_producer
        user_data['isAdmin'] = user.is_admin
        user_data['isOther'] = user.is_other
        user_data['member_since'] = user.member_since
        user_data['farmType'] = user.farm_type
        user_data['rating'] = user.rating
        user_data['mailingAddressStreet'] = user.mailing_street
        user_data['mailingAddressCity'] = user.mailing_city
        user_data['mailingAddressProvince'] = user.mailing_province
        user_data['mailingAddressCountry'] = user.mailing_country
        user_data['mailingAddressPostalCode'] = user.mailing_postal_code
        user_data['billingAddressStreet'] = user.billing_street
        user_data['billingAddressCity'] = user.billing_city
        user_data['billingAddressProvince'] = user.billing_province
        user_data['billingAddressCountry'] = user.billing_country
        user_data['billingAddressPostalCode'] = user.billing_postal_code
        user_data['comments'] = user.user_comments
        output.append(user_data)

    return jsonify({'users': output})