from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.Produce import Produce
from files.gauth import authorized

@app.route("/produce/modify/", methods=['POST'])
@authorized
def modify_produce(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    data = request.get_json()
    filterId = data.get('id')
    produce_to_update = db.session.query(
        Produce).filter(Produce.id == filterId).first()
    produce_to_update.product_name = data.get('type'),
    produce_to_update.package_type = data.get('packageType'),
    produce_to_update.package_size = data.get('packageSize'),
    produce_to_update.package_size_unit = data.get('packageSizeUnit'),
    produce_to_update.est_completion_date = data.get('estCompletionDate'),
    produce_to_update.seed_type = data.get('seedType'),
    produce_to_update.modified_seed = data.get('modifiedSeed'),
    produce_to_update.heirloom = data.get('heirloom'),
    produce_to_update.fertilizer_type_used = data.get('fertilizerTypeUsed'),
    produce_to_update.pesticide_type_used = data.get('pesticideTypeUsed'),
    produce_to_update.estimated_qty_planted = data.get('estQuantityPlanted'),
    produce_to_update.certified_organic = data.get('certifiedOrganic'),
    produce_to_update.estimated_finished_qty = data.get('estFinishedQty'),
    produce_to_update.est_price_to_be_paid = data.get('estPrice'),
    produce_to_update.qty_accepted_for_listing = data.get(
        'qtyAcceptedForListing'),
    produce_to_update.qty_accepted_at_delivery = data.get(
        'qtyAcceptedAtDelivery'),
    produce_to_update.chargebacks = data.get('chargebacks'),
    produce_to_update.price_paid = data.get('finalPricePaid'),
    produce_to_update.delivered_date = data.get('deliveredDate'),
    produce_to_update.delivered_to = data.get('deliveredTo'),
    produce_to_update.comments = data.get('comments'),

    db.session.commit()
    return jsonify({"Success": True})