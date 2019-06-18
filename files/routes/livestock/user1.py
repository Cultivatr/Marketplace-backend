from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.Livestock import Livestock
from files.gauth import authorized

@app.route('/livestock/<user1>/', methods=['GET'])
@authorized
def livestock_get_user(user1, idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    user_id = user1

    livestock = db.session.query(Livestock).filter(
        Livestock.user_id == user_id).all()
    output = []
    for item_livestock in livestock:
        item_livestock_data = {}
        x = item_livestock.id
        item_livestock_data['id'] = "L-%s" % (x)
        item_livestock_data['userId'] = item_livestock.user_id
        item_livestock_data['type'] = item_livestock.product_name
        item_livestock_data['breed'] = item_livestock.breed
        item_livestock_data['singleBrand'] = item_livestock.single_brand
        item_livestock_data['birthdate'] = item_livestock.est_birthdate
        item_livestock_data['regNumber'] = item_livestock.registration_number
        item_livestock_data['rfid'] = item_livestock.rfid_tag
        item_livestock_data['estStartingWeight'] = item_livestock.starting_weight
        item_livestock_data['hangingWeight'] = item_livestock.hanging_weight
        item_livestock_data['chargebacks'] = item_livestock.chargebacks
        item_livestock_data['dateOnFeed'] = item_livestock.starting_date_of_feed
        item_livestock_data['feedMethod'] = item_livestock.feed_method
        item_livestock_data['typeOfPasture'] = item_livestock.type_of_pasture
        item_livestock_data['typeOfFeed'] = item_livestock.type_of_feed
        item_livestock_data['estCompletionDate'] = item_livestock.est_completion_date
        item_livestock_data['estFinishedWeight'] = item_livestock.est_finished_weight
        item_livestock_data['estFinalPrice'] = item_livestock.est_price_to_be_paid
        item_livestock_data['quantity'] = item_livestock.quantity
        item_livestock_data['comments'] = item_livestock.comments
        item_livestock_data['finalPrice'] = item_livestock.price_paid
        item_livestock_data['deliveredDate'] = item_livestock.delivered_date
        item_livestock_data['deliveredTo'] = item_livestock.delivered_to
        item_livestock_data['status'] = item_livestock.status
        output.append(item_livestock_data)

    return jsonify({'livestock': output})