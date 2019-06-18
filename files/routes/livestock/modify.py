from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.Livestock import Livestock
from files.gauth import authorized

@app.route("/livestock/modify/", methods=['POST'])
@authorized
def modify_lifestock(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    data = request.get_json()
    filterId = data.get('id')
    livestock_to_update = db.session.query(
        Livestock).filter(Livestock.id == filterId).first()
    livestock_to_update.product_name = data.get('type'),
    livestock_to_update.breed = data.get('breed'),
    if(not data.get('singleBrand')):
        livestock_to_update.single_brand = 0
    if(data.get('singleBrand')):
        livestock_to_update.single_brand = 1,
    livestock_to_update.est_birthdate = data.get('birthdate'),
    livestock_to_update.registration_number = data.get('regNumber'),
    livestock_to_update.rfid_tag = data.get('rfid'),
    livestock_to_update.starting_weight = data.get('estStartingWeight'),
    livestock_to_update.hanging_weight = data.get('hangingWeight'),
    livestock_to_update.chargebacks = data.get('chargebacks'),
    livestock_to_update.starting_date_of_feed = data.get('dateOnFeed'),
    livestock_to_update.feed_method = data.get('feedMethod'),
    livestock_to_update.type_of_pasture = data.get('typeOfPasture'),
    livestock_to_update.type_of_feed = data.get('typeOfFeed'),
    livestock_to_update.est_completion_date = data.get('estCompletionDate'),
    livestock_to_update.est_finished_weight = data.get('estFinishedWeight'),
    livestock_to_update.est_price_to_be_paid = data.get('estFinalPrice'),
    livestock_to_update.quantity = data.get('quantity'),
    livestock_to_update.comments = data.get('comments'),
    livestock_to_update.price_paid = data.get('finalPrice'),
    livestock_to_update.delivered_date = data.get('deliveredDate'),
    livestock_to_update.delivered_to = data.get('deliveredTo'),
    db.session.commit()
    return jsonify({"Success": True})