from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.Users import Users
from files.gauth import authorized

@app.route("/admin/", methods=['POST'])
@authorized
def add_new_user(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    data = request.get_json()
    new_user = Users(
        first_name=data.get('firstName'),
        last_name=data.get('lastName'),
        primary_phone=data.get('primaryNumber'),
        secondary_phone=data.get('secondaryNumber'),
        email=data.get('email'),
        farm_name=data.get('farmName'),
        farm_location=data.get('farmLocation'),
        area=data.get('area'),
        is_admin=data.get('isAdmin'),
        is_producer=data.get('isProducer'),
        is_other=data.get('isOther'),
        member_since=datetime.today(),
        farm_type=data.get('farmType'),
        rating=data.get('rating'),
        mailing_street=data.get('mailingAddressStreet'),
        mailing_city=data.get('mailingAddressCity'),
        mailing_province=data.get('mailingAddressProvince'),
        mailing_country=data.get('mailingAddressCountry'),
        mailing_postal_code=data.get('mailingAddressPostalCode'),
        billing_street=data.get('billingAddressStreet'),
        billing_city=data.get('billingAddressCity'),
        billing_province=data.get('billingAddressProvince'),
        billing_country=data.get('billingAddressCountry'),
        billing_postal_code=data.get('billingAddressPostalCode'),
        user_comments=data.get('comments'),
    )
    # if not new_user.first_name: return jsonify('Error: You must provide a first name'), 400
    # if not new_user.last_name: return jsonify('Error: You must provide a last name'), 400
    # if not new_user.primary_phone: return jsonify('Error: You must provide a phone number'), 400
    # if not new_user.email: return jsonify('Error: You must provide an email'), 400
    error_message = []

    db.session.add(new_user)
    db.session.commit()
    return jsonify({'id': new_user.id}), 201