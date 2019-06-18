from flask import current_app as app, request, jsonify
from app import global_vars
db = global_vars.db
from files.db_models.Produce import Produce
from files.gauth import authorized

@app.route('/produce/all/', methods=['GET'])
@authorized
def produce_get_all(idinfo):
    if idinfo == 'unauthorized':
        return 'unauthorized', 401
    produce = db.session.query(Produce)
    output = []
    for item_produce in produce:
        item_produce_data = {}
        x = item_produce.id
        item_produce_data['id'] = "P-%s" % (x)
        item_produce_data['userId'] = item_produce.user_id
        item_produce_data['type'] = item_produce.product_name
        item_produce_data['packageType'] = item_produce.package_type
        item_produce_data['packageSize'] = item_produce.package_size
        item_produce_data['packageSizeUnit'] = item_produce.package_size_unit
        item_produce_data['estCompletionDate'] = item_produce.est_completion_date
        item_produce_data['seedType'] = item_produce.seed_type
        item_produce_data['modifiedSeed'] = item_produce.modified_seed
        item_produce_data['heirloom'] = item_produce.heirloom
        item_produce_data['fertilizerTypeUsed'] = item_produce.fertilizer_type_used
        item_produce_data['pesticideTypeUsed'] = item_produce.pesticide_type_used
        item_produce_data['estQuantityPlanted'] = item_produce.estimated_qty_planted
        item_produce_data['certifiedOrganic'] = item_produce.certified_organic
        item_produce_data['estFinishedQty'] = item_produce.estimated_finished_qty
        item_produce_data['estPrice'] = item_produce.est_price_to_be_paid
        item_produce_data['qtyAcceptedForListing'] = item_produce.qty_accepted_for_listing
        item_produce_data['qtyAcceptedAtDelivery'] = item_produce.qty_accepted_at_delivery
        item_produce_data['chargebacks'] = item_produce.chargebacks
        item_produce_data['finalPricePaid'] = item_produce.price_paid
        item_produce_data['deliveredDate'] = item_produce.delivered_date
        item_produce_data['deliveredTo'] = item_produce.delivered_to
        item_produce_data['comments'] = item_produce.comments
        item_produce_data['status'] = item_produce.status
        output.append(item_produce_data)

    return jsonify({'produce': output})