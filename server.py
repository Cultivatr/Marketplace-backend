from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import os
import simplejson as json
from DB.scripts import sql as sql

app = Flask(__name__)
app.secret_key = os.urandom(16)
CORS(app, supports_credentials=True)

# app.config['SECRET_KEY'] = 'secret'

@app.route("/admin", methods=['GET','POST'])
# @cross_origin(supports_credentials=True)
def add_new_user():
    data = request.get_json()
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    p_number = data.get('primaryNumber')
    s_number = data.get('secondaryNumber')
    email = data.get('email')
    f_name = data.get('farmName')
    f_location = data.get('farmLocation')
    area = data.get('area')
    f_type = data.get('farmType')
    rating = data.get('rating')
    m_street = data.get('mailingAddressStreet')
    m_city = data.get('mailingAddressCity')
    m_province = data.get('mailingAddressProvince')
    m_country = data.get('mailingAddressCountry')
    m_postal_code = data.get('mailingAddressPostalCode')
    b_street = data.get('billingAddressStreet')
    b_city = data.get('billingAddressCity')
    b_province = data.get('billingAddressProvince')
    b_country = data.get('billingAddressCountry')
    b_postal_code = data.get('billingAddressPostalCode')
    comments = data.get('comments')
    is_admin = data.get('isAdmin')
    is_producer = data.get('isProducer')
    is_other = data.get('isOther')
    member_since = datetime.today()
    
    query = sql.add_user(first_name,last_name,p_number,s_number,email,f_name,f_location,area,is_producer,is_admin,is_other,member_since,f_type,rating,m_street,m_city,m_province,m_country,m_postal_code,b_street,b_city,b_province,b_country,b_postal_code,comments)
    return jsonify(query)

@app.route("/admin/updateUsers", methods=['POST'])
def update_users():
    data = request.get_json()
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    p_number = data.get('primaryNumber')
    s_number = data.get('secondaryNumber')
    email = data.get('email')
    f_name = data.get('farmName')
    f_location = data.get('farmLocation')
    area = data.get('area')
    f_type = data.get('farmType')
    rating = data.get('rating')
    m_street = data.get('mailingAddressStreet')
    m_city = data.get('mailingAddressCity')
    m_province = data.get('mailingAddressProvince')
    m_country = data.get('mailingAddressCountry')
    m_postal_code = data.get('mailingAddressPostalCode')
    b_street = data.get('billingAddressStreet')
    b_city = data.get('billingAddressCity')
    b_province = data.get('billingAddressProvince')
    b_country = data.get('billingAddressCountry')
    b_postal_code = data.get('billingAddressPostalCode')
    comments = data.get('comments')
    is_admin = data.get('isAdmin')
    is_producer = data.get('isProducer')
    is_other = data.get('isOther')
    userID = data.get("id")
    member_since = datetime.today()
    
    query = sql.update_user(first_name,last_name,p_number,s_number,email,f_name,f_location,area,is_producer,is_admin,is_other,member_since,f_type,rating,m_street,m_city,m_province,m_country,m_postal_code,b_street,b_city,b_province,b_country,b_postal_code,comments,userID)
    return jsonify(query)

@app.route('/admin/users', methods=['GET'])
def get_users():
    users = sql.get_users()
    output = []
    # print(users)
    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['firstName'] = user.first_name
        user_data['lastName'] = user.last_name
        user_data['primaryNumber'] = user.p_number
        user_data['secondaryNumber'] = user.s_number
        user_data['email'] = user.email
        user_data['farmName'] = user.f_name
        user_data['farmLocation'] = user.f_location
        user_data['area'] = user.area
        user_data['isProducer'] = user.is_producer
        user_data['isAdmin'] = user.is_admin
        user_data['isOther'] = user.is_other
        user_data['member_since'] = user.member_since
        user_data['farmType'] = user.f_type
        user_data['rating'] = user.rating
        user_data['mailingAddressStreet'] = user.m_street
        user_data['mailingAddressCity'] = user.m_city
        user_data['mailingAddressProvince'] = user.m_province
        user_data['mailingAddressCountry'] = user.m_country
        user_data['mailingAddressPostalCode'] = user.m_postal_code
        user_data['billingAddressStreet'] = user.b_street
        user_data['billingAddressCity'] = user.b_city
        user_data['billingAddressProvince'] = user.b_province
        user_data['billingAddressCountry'] = user.b_country
        user_data['billingAddressPostalCode'] = user.b_postal_code
        user_data['comments'] = user.comments
        output.append(user_data)
    return jsonify({ 'users': output })

@app.route('/admin/user/<int:id>')
def get_user(id):
    user = sql.get_user(id)
    
    if not user:
        return jsonify({'message': 'No client found!'})
    
    user_data = {}
    user_data['id'] = user.id
    user_data['firstName'] = user.first_name
    user_data['lastName'] = user.last_name
    user_data['primaryNumber'] = user.p_number
    user_data['secondaryNumber'] = user.s_number
    user_data['email'] = user.email
    user_data['farmName'] = user.f_name
    user_data['farmLocation'] = user.f_location
    user_data['area'] = user.area
    user_data['isProducer'] = user.is_producer
    user_data['isAdmin'] = user.is_admin
    user_data['isOther'] = user.is_other
    user_data['member_since'] = user.member_since
    user_data['farmType'] = user.f_type
    user_data['rating'] = user.rating
    user_data['mailingAddressStreet'] = user.m_street
    user_data['mailingAddressCity'] = user.m_city
    user_data['mailingAddressProvince'] = user.m_province
    user_data['mailingAddressCountry'] = user.m_country
    user_data['mailingAddressPostalCode'] = user.m_postal_code
    user_data['billingAddressStreet'] = user.b_street
    user_data['billingAddressCity'] = user.b_city
    user_data['billingAddressProvince'] = user.b_province
    user_data['billingAddressCountry'] = user.b_country
    user_data['billingAddressPostalCode'] = user.b_postal_code
    user_data['comments'] = user.comments

    return jsonify({ 'user': user_data })

@app.route("/add_items/livestock/<user_id>", methods=['POST', 'GET'])
def add_livestock_items(user_id):
    data = request.get_json('')
    user_id = data.get('userId')
    name = data.get('type')
    breed = data.get('breed')
    singleBrand = data.get('singleBrand')
    birthdate = data.get('birthdate')
    regNumber = data.get('regNumber')
    rfid = data.get('rfid')
    estStartingWeight = data.get('estStartingWeight')
    hangingWeight = data.get('hangingWeight')
    chargebacks = data.get('chargebacks')
    dateOnFeed = data.get('dateOnFeed')
    feedMethod = data.get('feedMethod')
    typeOfPasture = data.get('typeOfPasture')
    typeOfFeed = data.get('typeOfFeed')
    estCompletionDate = data.get('estCompletionDate')
    estFinishedWeight = data.get('estFinishedWeight')
    estFinalPrice = data.get('estFinalPrice')
    quantity = data.get('quantity')
    comments = data.get('comments')
    finalPrice = data.get('finalPrice')
    deliveredDate = data.get('deliveredDate')
    deliveredTo = data.get('deliveredTo')
    status = "Pending Approval"

    newItem = sql.add_livestock_item_by_user_id(user_id, name,breed,singleBrand,birthdate,regNumber,rfid,estStartingWeight,hangingWeight,chargebacks,dateOnFeed,feedMethod,typeOfPasture,typeOfFeed,estCompletionDate,estFinishedWeight,estFinalPrice,quantity,comments,finalPrice,deliveredDate, deliveredTo,status)
    return jsonify(newItem)

@app.route('/items_livestock', methods=['GET'])
def get_items_livestock():
    items_livestock = sql.get_all_offered_items_livestock()
    output = []
    # print(users)
    for item_livestock in items_livestock:
        item_livestock_data = {}
        x = item_livestock.id
        item_livestock_data['id'] = "L-%s"%(x) 
        item_livestock_data['userId'] = item_livestock.Users_id
        item_livestock_data['type'] = item_livestock.Product_name
        item_livestock_data['breed'] = item_livestock.Breed
        item_livestock_data['singleBrand'] = item_livestock.Single_brand
        item_livestock_data['birthdate'] = item_livestock.Est_birthdate
        item_livestock_data['regNumber'] = item_livestock.Registration_number
        item_livestock_data['rfid'] = item_livestock.RFID_tag
        item_livestock_data['estStartingWeight'] = item_livestock.Starting_weight
        item_livestock_data['hangingWeight'] = item_livestock.Hanging_weight
        item_livestock_data['chargebacks'] = item_livestock.Chargebacks
        item_livestock_data['dateOnFeed'] = item_livestock.Starting_date_of_feed
        item_livestock_data['feedMethod'] = item_livestock.Feed_method
        item_livestock_data['typeOfPasture'] = item_livestock.Type_of_pasture
        item_livestock_data['typeOfFeed'] = item_livestock.Type_of_feed
        item_livestock_data['estCompletionDate'] = item_livestock.Est_completion_date
        item_livestock_data['estFinishedWeight'] = item_livestock.Est_finished_weight
        item_livestock_data['estFinalPrice'] = item_livestock.Est_price_to_be_paid
        item_livestock_data['quantity'] = item_livestock.Quantity
        item_livestock_data['comments'] = item_livestock.Comments
        item_livestock_data['finalPrice'] = item_livestock.Price_paid
        item_livestock_data['deliveredDate'] = item_livestock.Delivered_date
        item_livestock_data['deliveredTo'] = item_livestock.Delivered_to
        item_livestock_data['status'] = item_livestock.Status

        output.append(item_livestock_data)
    return jsonify({ 'items_livestock': output })

@app.route("/add_items/produce/<user_id>", methods=['POST', 'GET'])
def add_produce_items(user_id):
    data = request.get_json('')
    user_id = data.get('userId')
    name = data.get('type')
    packageType = data.get('packageType')
    datePlanted = data.get('datePlanted')
    seedType = data.get('seedType')
    modifiedSeed = data.get('modifiedSeed')
    heirloom = data.get('heirloom')
    fertilizerTypeUsed = data.get('fertilizerTypeUsed')
    pesticideTypeUsed = data.get('pesticideTypeUsed')
    deliveredDate = data.get('deliveredDate')
    comments = data.get('comments')
    estQuantityPlanted = data.get('estQuantityPlanted')
    gmo = data.get('gmo')
    estFinishedQty = data.get('estFinishedQty')
    estPrice = data.get('estPrice')
    qtyAcceptedForListing = data.get('qtyAcceptedForListing')
    qtyAcceptedAtDelivery = data.get('qtyAcceptedAtDelivery')
    chargebacks = data.get('chargebacks')
    finalPricePaid = data.get('finalPricePaid')
    deliveredTo = data.get('deliveredTo')
    status = "Pending Approval"

    newItem = sql.add_produce_item_by_user_id(user_id,name, packageType,datePlanted,seedType,modifiedSeed,heirloom,fertilizerTypeUsed,pesticideTypeUsed,estQuantityPlanted,gmo,estFinishedQty,estPrice,qtyAcceptedForListing,qtyAcceptedAtDelivery,chargebacks,finalPricePaid,deliveredDate,deliveredTo,comments,status)
    return jsonify(newItem)

@app.route('/items_produce', methods=['GET'])
def get_items_produce():
    items_produce = sql.get_all_offered_items_produce()
    output = []
    # print(users)
    for item_produce in items_produce:
        item_produce_data = {}
        x = item_produce.id
        item_produce_data['id'] = "P-%s"%(x)
        item_produce_data['userId'] = item_produce.Users_id
        item_produce_data['type'] = item_produce.Product_name
        item_produce_data['packageType'] = item_produce.Package_type
        item_produce_data['datePlanted'] = item_produce.Date_planted
        item_produce_data['seedType'] = item_produce.Seed_type
        item_produce_data['modifiedSeed'] = item_produce.Modified_seed
        item_produce_data['heirloom'] = item_produce.Heirloom
        item_produce_data['fertilizerTypeUsed'] = item_produce.Fertilizer_type_used
        item_produce_data['pesticideTypeUsed'] = item_produce.Pesticide_type_used
        item_produce_data['deliveredDate'] = item_produce.Delivered_date
        item_produce_data['comments'] = item_produce.Comments
        item_produce_data['estQuantityPlanted'] = item_produce.Estimated_qty_planted
        item_produce_data['gmo'] = item_produce.GMO
        item_produce_data['estFinishedQty'] = item_produce.Estimated_finished_qty
        item_produce_data['estPrice'] = item_produce.Est_price_to_be_paid
        item_produce_data['qtyAcceptedForListing'] = item_produce.Qty_accepted_for_listing
        item_produce_data['qtyAcceptedAtDelivery'] = item_produce.Qty_accepted_at_delivery
        item_produce_data['chargebacks'] = item_produce.Chargebacks
        item_produce_data['finalPricePaid'] = item_produce.Price_paid
        item_produce_data['deliveredTo'] = item_produce.Delivered_to
        item_produce_data['status'] = item_produce.Status

        output.append(item_produce_data)
    return jsonify({ 'items_produce': output })

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(degug=True, use_reload=True)



