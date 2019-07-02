from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.Produce import Produce
from files.gauth import authorized
from datetime import datetime

@app.route("/produce/", methods=['POST'])
@authorized
def add_produce_items(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    data = request.get_json()

    new_produce = Produce(
        user_id=data.get('userId'),
        product_name=data.get('type'),
        package_type=data.get('packageType'),
        package_size=data.get('packageSize'),
        package_size_unit=data.get('packageSizeUnit'),
        est_completion_date=data.get('estCompletionDate'),
        seed_type=data.get('seedType'),
        modified_seed=data.get('modifiedSeed'),
        heirloom=data.get('heirloom'),
        fertilizer_type_used=data.get('fertilizerTypeUsed'),
        pesticide_type_used=data.get('pesticideTypeUsed'),
        estimated_qty_planted=data.get('estQuantityPlanted'),
        certified_organic=data.get('certifiedOrganic'),
        estimated_finished_qty=data.get('estFinishedQty'),
        est_price_to_be_paid=data.get('estPrice'),
        qty_accepted_for_listing=data.get('qtyAcceptedForListing'),
        qty_accepted_at_delivery=data.get('qtyAcceptedAtDelivery'),
        chargebacks=data.get('chargebacks'),
        price_paid=data.get('finalPricePaid'),
        delivered_date=data.get('deliveredDate'),
        delivered_to=data.get('deliveredTo'),
        comments=data.get('comments'),
        status="Pending Admin",
        created_date=datetime.today(),
    )
    db.session.add(new_produce)
    db.session.commit()
    return jsonify({"Success": True})