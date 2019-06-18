from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.Livestock import Livestock
from files.gauth import authorized
from datetime import datetime

@app.route("/livestock/", methods=['POST'])
@authorized
def add_livestock_items(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    data = request.get_json()
    new_livestock = Livestock(
        user_id=data.get('userId'),
        product_name=data.get('type'),
        breed=data.get('breed'),
        single_brand=data.get('singleBrand'),
        est_birthdate=data.get('birthdate'),
        registration_number=data.get('regNumber'),
        rfid_tag=data.get('rfid'),
        starting_weight=data.get('estStartingWeight'),
        hanging_weight=data.get('hangingWeight'),
        chargebacks=data.get('chargebacks'),
        starting_date_of_feed=data.get('dateOnFeed'),
        feed_method=data.get('feedMethod'),
        type_of_pasture=data.get('typeOfPasture'),
        type_of_feed=data.get('typeOfFeed'),
        est_completion_date=data.get('estCompletionDate'),
        est_finished_weight=data.get('estFinishedWeight'),
        est_price_to_be_paid=data.get('estFinalPrice'),
        quantity=data.get('quantity'),
        comments=data.get('comments'),
        price_paid=data.get('finalPrice'),
        delivered_date=data.get('deliveredDate'),
        delivered_to=data.get('deliveredTo'),
        status="Pending Admin",
        created_date=datetime.today()
    )
    db.session.add(new_livestock)
    db.session.commit()
    return jsonify({"Success": True})