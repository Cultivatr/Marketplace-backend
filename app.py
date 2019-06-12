import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from flask_migrate import Migrate


##################################################
###THE FOLLOWING IS FOR HEROKU POSTGRES SERVER####
##################################################

app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db=SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

##################################################
####THE FOLLOWING IS FOR LOCAL POSTGRES SERVER####
##################################################

# app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost/cultivatr'
# db=SQLAlchemy(app)
# migrate = Migrate(app, db)
# CORS(app, supports_credentials=True)


class Users(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.Text)
    last_name=db.Column(db.Text, nullable=False)
    primary_phone=db.Column(db.Text, nullable=False)
    secondary_phone=db.Column(db.Text)
    email=db.Column(db.Text, nullable=False)
    farm_name=db.Column(db.Text, nullable=False)
    farm_location=db.Column(db.Text)
    area=db.Column(db.Text)
    ## is_producer & is_other are no longer being used.
    is_producer=db.Column(db.Boolean)
    is_admin=db.Column(db.Boolean)
    is_other=db.Column(db.Boolean)
    member_since=db.Column(db.Date)
    farm_type=db.Column(db.Text)
    rating=db.Column(db.Integer)
    mailing_street=db.Column(db.Text)
    mailing_city=db.Column(db.Text)
    mailing_province=db.Column(db.Text)
    mailing_country=db.Column(db.Text)
    mailing_postal_code=db.Column(db.Text)
    billing_street=db.Column(db.Text)
    billing_city=db.Column(db.Text)
    billing_province=db.Column(db.Text)
    billing_country=db.Column(db.Text)
    billing_postal_code=db.Column(db.Text)
    user_comments=db.Column(db.Text)


class Produce(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='RESTRICT', onupdate='CASCADE'),
        nullable=False
    )
    product_name=db.Column(db.Text)
    package_type=db.Column(db.Text)
    package_size=db.Column(db.Integer)
    package_size_unit=db.Column(db.Text)
    est_completion_date=db.Column(db.Date)
    seed_type=db.Column(db.Text)
    modified_seed=db.Column(db.Text)
    heirloom=db.Column(db.Text)
    fertilizer_type_used=db.Column(db.Text)
    pesticide_type_used=db.Column(db.Text)
    estimated_qty_planted=db.Column(db.Integer)
    certified_organic=db.Column(db.Text)
    estimated_finished_qty=db.Column(db.Integer)
    est_price_to_be_paid=db.Column(db.Float)
    qty_accepted_for_listing=db.Column(db.Integer)
    qty_accepted_at_delivery=db.Column(db.Integer)
    chargebacks=db.Column(db.Integer)
    price_paid=db.Column(db.Float)
    created_date=db.Column(db.Date)
    accepted_date=db.Column(db.Date)
    sold_date=db.Column(db.Date)
    delivered_date=db.Column(db.Date)
    delivered_to=db.Column(db.Text)
    comments=db.Column(db.Text)
    status=db.Column(db.Text)


class Livestock(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='RESTRICT', onupdate='CASCADE'),
        nullable=False
    )
    product_name=db.Column(db.Text)
    breed=db.Column(db.Text)
    single_brand=db.Column(db.Text)
    est_birthdate=db.Column(db.Date)
    registration_number=db.Column(db.Float)
    rfid_tag=db.Column(db.Integer)
    starting_weight=db.Column(db.Integer)
    hanging_weight=db.Column(db.Integer)
    chargebacks=db.Column(db.Integer)
    starting_date_of_feed=db.Column(db.Date)
    feed_method=db.Column(db.Text)
    type_of_pasture=db.Column(db.Text)
    type_of_feed=db.Column(db.Text)
    est_completion_date=db.Column(db.Date)
    est_finished_weight=db.Column(db.Integer)
    est_price_to_be_paid=db.Column(db.Integer)
    quantity=db.Column(db.Integer)
    comments=db.Column(db.Text)
    price_paid=db.Column(db.Integer)
    created_date=db.Column(db.Date)
    accepted_date=db.Column(db.Date)
    sold_date=db.Column(db.Date)
    delivered_date=db.Column(db.Date)
    delivered_to=db.Column(db.Text)
    status=db.Column(db.Text)


class ProduceItems(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    item=db.Column(db.String(50),unique=True )


@app.route('/produceItems/all/', methods=['GET'])
def get_indiv_produce_items():
    p_items=db.session.query(ProduceItems)
    output=[]
    for p_item in p_items:
        p_item_data={}
        p_item_data['newItem']=p_item.item
        output.append(p_item_data)

    return jsonify({ 'produce_items': output })



@app.route("/produceItems/add/", methods=['POST'])
def add_new_produce_item():
    data=request.get_json()
    new_p_item=ProduceItems(
    item=data.get('newItem'))
    db.session.add(new_p_item)
    db.session.commit()
    
    return jsonify({'name': new_p_item.item}), 201

@app.route("/produceItems/delete/", methods=['POST'])
def delete_produce_selection_item():
    data=request.get_json()
    filterId=data.get('itemToDelete')
    db.session.query(ProduceItems).filter(ProduceItems.item == filterId).delete()
    db.session.commit()
    return 'Success', 201

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'


@app.route('/admin/users/', methods=['GET'])
def get_users():
    users=db.session.query(Users)
    output=[]
    for user in users:
        user_data={}
        user_data['id']=user.id
        user_data['firstName']=user.first_name
        user_data['lastName']=user.last_name
        user_data['primaryNumber']=user.primary_phone
        user_data['secondaryNumber']=user.secondary_phone
        user_data['email']=user.email
        user_data['farmName']=user.farm_name
        user_data['farmLocation']=user.farm_location
        user_data['area']=user.area
        user_data['isProducer']=user.is_producer
        user_data['isAdmin']=user.is_admin
        user_data['isOther']=user.is_other
        user_data['member_since']=user.member_since
        user_data['farmType']=user.farm_type
        user_data['rating']=user.rating
        user_data['mailingAddressStreet']=user.mailing_street
        user_data['mailingAddressCity']=user.mailing_city
        user_data['mailingAddressProvince']=user.mailing_province
        user_data['mailingAddressCountry']=user.mailing_country
        user_data['mailingAddressPostalCode']=user.mailing_postal_code
        user_data['billingAddressStreet']=user.billing_street
        user_data['billingAddressCity']=user.billing_city
        user_data['billingAddressProvince']=user.billing_province
        user_data['billingAddressCountry']=user.billing_country
        user_data['billingAddressPostalCode']=user.billing_postal_code
        user_data['comments']=user.user_comments
        output.append(user_data)

    return jsonify({ 'users': output })


@app.route("/admin/", methods=['POST'])
def add_new_user():
    data=request.get_json()
    new_user=Users(
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
    error_message  = []
 

    db.session.add(new_user)
    db.session.commit()
    return jsonify({'id': new_user.id}), 201

@app.route("/admin/users/delete/", methods=['POST'])
def delete_user():
    data=request.get_json()
    filterId=data.get('id')
    db.session.query(Produce).filter(Produce.user_id == filterId).delete()
    db.session.query(Livestock).filter(Livestock.user_id == filterId).delete()
    db.session.query(Users).filter(Users.id == filterId).delete()
    db.session.commit()
    return jsonify({ "Success": True })

@app.route("/admin/updateUsers/", methods=['POST'])
def modify_user():
    data=request.get_json()
    filterId=data.get('id')
    userToUpdate= db.session.query(Users).filter(Users.id == filterId).first()
    userToUpdate.first_name=data.get('firstName'),
    userToUpdate.last_name=data.get('lastName'),
    userToUpdate.primary_phone=data.get('primaryNumber'),
    userToUpdate.secondary_phone=data.get('secondaryNumber'),
    userToUpdate.email=data.get('email'),
    userToUpdate.farm_name=data.get('farmName'),
    userToUpdate.farm_location=data.get('farmLocation'),
    userToUpdate.area=data.get('area'),
    userToUpdate.is_admin=data.get('isAdmin')
    if(not data.get('isAdmin')):
        userToUpdate.is_admin=0   
    if(data.get('isAdmin')):
        userToUpdate.is_admin=1 
    # userToUpdate.is_admin=data.get('isAdmin'),
    # userToUpdate.is_producer=bool(data.get('isProducer')),
    # userToUpdate.is_other=bool(data.get('isOther')),
    userToUpdate.farm_type=data.get('farmType'),
    userToUpdate.rating=data.get('rating'),
    userToUpdate.mailing_street=data.get('mailingAddressStreet'),
    userToUpdate.mailing_city=data.get('mailingAddressCity'),
    userToUpdate.mailing_province=data.get('mailingAddressProvince'),
    userToUpdate.mailing_country=data.get('mailingAddressCountry'),
    userToUpdate.mailing_postal_code=data.get('mailingAddressPostalCode'),
    userToUpdate.billing_street=data.get('billingAddressStreet'),
    userToUpdate.billing_city=data.get('billingAddressCity'),
    userToUpdate.billing_province=data.get('billingAddressProvince'),
    userToUpdate.billing_country=data.get('billingAddressCountry'),
    userToUpdate.billing_postal_code=data.get('billingAddressPostalCode'),
    userToUpdate.user_comments=data.get('comments')
    db.session.commit()
    return jsonify({ "Success": True })



@app.route("/livestock/", methods=['POST'])
def add_livestock_items():
    data=request.get_json()
    new_livestock=Livestock(
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
    return jsonify({ "Success": True })


@app.route('/livestock/all/', methods=['GET'])
def livestock_get_all():
    livestock=db.session.query(Livestock)
    output=[]
    for item_livestock in livestock:
        item_livestock_data={}
        x=item_livestock.id
        item_livestock_data['id']="L-%s"%(x) 
        item_livestock_data['userId']=item_livestock.user_id
        item_livestock_data['type']=item_livestock.product_name
        item_livestock_data['breed']=item_livestock.breed
        item_livestock_data['singleBrand']=item_livestock.single_brand
        item_livestock_data['birthdate']=item_livestock.est_birthdate
        item_livestock_data['regNumber']=item_livestock.registration_number
        item_livestock_data['rfid']=item_livestock.rfid_tag
        item_livestock_data['estStartingWeight']=item_livestock.starting_weight
        item_livestock_data['hangingWeight']=item_livestock.hanging_weight
        item_livestock_data['chargebacks']=item_livestock.chargebacks
        item_livestock_data['dateOnFeed']=item_livestock.starting_date_of_feed
        item_livestock_data['feedMethod']=item_livestock.feed_method
        item_livestock_data['typeOfPasture']=item_livestock.type_of_pasture
        item_livestock_data['typeOfFeed']=item_livestock.type_of_feed
        item_livestock_data['estCompletionDate']=item_livestock.est_completion_date
        item_livestock_data['estFinishedWeight']=item_livestock.est_finished_weight
        item_livestock_data['estFinalPrice']=item_livestock.est_price_to_be_paid
        item_livestock_data['quantity']=item_livestock.quantity
        item_livestock_data['comments']=item_livestock.comments
        item_livestock_data['finalPrice']=item_livestock.price_paid
        item_livestock_data['deliveredDate']=item_livestock.delivered_date
        item_livestock_data['deliveredTo']=item_livestock.delivered_to
        item_livestock_data['status']=item_livestock.status
        output.append(item_livestock_data)

    return jsonify({ 'livestock': output })

@app.route('/livestock/<user1>/', methods=['GET'])
def livestock_get_user(user1):
    user_id=user1

    livestock=db.session.query(Livestock).filter(Livestock.user_id==user_id).all()
    output=[]
    for item_livestock in livestock:
        item_livestock_data={}
        x=item_livestock.id
        item_livestock_data['id']="L-%s"%(x) 
        item_livestock_data['userId']=item_livestock.user_id
        item_livestock_data['type']=item_livestock.product_name
        item_livestock_data['breed']=item_livestock.breed
        item_livestock_data['singleBrand']=item_livestock.single_brand
        item_livestock_data['birthdate']=item_livestock.est_birthdate
        item_livestock_data['regNumber']=item_livestock.registration_number
        item_livestock_data['rfid']=item_livestock.rfid_tag
        item_livestock_data['estStartingWeight']=item_livestock.starting_weight
        item_livestock_data['hangingWeight']=item_livestock.hanging_weight
        item_livestock_data['chargebacks']=item_livestock.chargebacks
        item_livestock_data['dateOnFeed']=item_livestock.starting_date_of_feed
        item_livestock_data['feedMethod']=item_livestock.feed_method
        item_livestock_data['typeOfPasture']=item_livestock.type_of_pasture
        item_livestock_data['typeOfFeed']=item_livestock.type_of_feed
        item_livestock_data['estCompletionDate']=item_livestock.est_completion_date
        item_livestock_data['estFinishedWeight']=item_livestock.est_finished_weight
        item_livestock_data['estFinalPrice']=item_livestock.est_price_to_be_paid
        item_livestock_data['quantity']=item_livestock.quantity
        item_livestock_data['comments']=item_livestock.comments
        item_livestock_data['finalPrice']=item_livestock.price_paid
        item_livestock_data['deliveredDate']=item_livestock.delivered_date
        item_livestock_data['deliveredTo']=item_livestock.delivered_to
        item_livestock_data['status']=item_livestock.status
        output.append(item_livestock_data)

    return jsonify({ 'livestock': output })


@app.route("/livestock/modify/", methods=['POST'])
def modify_lifestock():
    data=request.get_json()
    filterId=data.get('id')
    livestock_to_update= db.session.query(Livestock).filter(Livestock.id == filterId).first()
    livestock_to_update.product_name=data.get('type'),
    livestock_to_update.breed=data.get('breed'),
    if(not data.get('singleBrand')):
            livestock_to_update.single_brand=0   
    if(data.get('singleBrand')):
            livestock_to_update.single_brand=1 ,
    livestock_to_update.est_birthdate=data.get('birthdate'),
    livestock_to_update.registration_number=data.get('regNumber'),
    livestock_to_update.rfid_tag=data.get('rfid'),
    livestock_to_update.starting_weight=data.get('estStartingWeight'),
    livestock_to_update.hanging_weight=data.get('hangingWeight'),
    livestock_to_update.chargebacks=data.get('chargebacks'),
    livestock_to_update.starting_date_of_feed=data.get('dateOnFeed'),
    livestock_to_update.feed_method=data.get('feedMethod'),
    livestock_to_update.type_of_pasture=data.get('typeOfPasture'),
    livestock_to_update.type_of_feed=data.get('typeOfFeed'),
    livestock_to_update.est_completion_date=data.get('estCompletionDate'),
    livestock_to_update.est_finished_weight=data.get('estFinishedWeight'),
    livestock_to_update.est_price_to_be_paid=data.get('estFinalPrice'),
    livestock_to_update.quantity=data.get('quantity'),
    livestock_to_update.comments=data.get('comments'),
    livestock_to_update.price_paid=data.get('finalPrice'),
    livestock_to_update.delivered_date=data.get('deliveredDate'),
    livestock_to_update.delivered_to=data.get('deliveredTo'),
    db.session.commit()
    return jsonify({ "Success": True })
 


@app.route('/produce/all/', methods=['GET'])
def produce_get_all():
    produce=db.session.query(Produce)
    output=[]
    for item_produce in produce:
        item_produce_data={}
        x=item_produce.id
        item_produce_data['id']="P-%s"%(x)
        item_produce_data['userId']=item_produce.user_id
        item_produce_data['type']=item_produce.product_name
        item_produce_data['packageType']=item_produce.package_type
        item_produce_data['packageSize']=item_produce.package_size
        item_produce_data['packageSizeUnit']=item_produce.package_size_unit
        item_produce_data['estCompletionDate']=item_produce.est_completion_date
        item_produce_data['seedType']=item_produce.seed_type
        item_produce_data['modifiedSeed']=item_produce.modified_seed
        item_produce_data['heirloom']=item_produce.heirloom
        item_produce_data['fertilizerTypeUsed']=item_produce.fertilizer_type_used
        item_produce_data['pesticideTypeUsed']=item_produce.pesticide_type_used
        item_produce_data['estQuantityPlanted']=item_produce.estimated_qty_planted
        item_produce_data['certifiedOrganic']=item_produce.certified_organic
        item_produce_data['estFinishedQty']=item_produce.estimated_finished_qty
        item_produce_data['estPrice']=item_produce.est_price_to_be_paid
        item_produce_data['qtyAcceptedForListing']=item_produce.qty_accepted_for_listing
        item_produce_data['qtyAcceptedAtDelivery']=item_produce.qty_accepted_at_delivery
        item_produce_data['chargebacks']=item_produce.chargebacks
        item_produce_data['finalPricePaid']=item_produce.price_paid
        item_produce_data['deliveredDate']=item_produce.delivered_date
        item_produce_data['deliveredTo']=item_produce.delivered_to
        item_produce_data['comments']=item_produce.comments
        item_produce_data['status']=item_produce.status
        output.append(item_produce_data)

    return jsonify({ 'produce': output })


@app.route('/produce/<user1>/', methods=['GET'])
def produce_get_user(user1):
    user_id=user1
    produce=db.session.query(Produce).filter(Produce.user_id == user_id).all()
    output=[]
    for item_produce in produce:
        item_produce_data={}
        x=item_produce.id
        item_produce_data['id']="P-%s"%(x)
        item_produce_data['userId']=item_produce.user_id
        item_produce_data['type']=item_produce.product_name
        item_produce_data['packageType']=item_produce.package_type
        item_produce_data['packageSize']=item_produce.package_size
        item_produce_data['packageSizeUnit']=item_produce.package_size_unit
        item_produce_data['estCompletionDate']=item_produce.est_completion_date
        item_produce_data['seedType']=item_produce.seed_type
        item_produce_data['modifiedSeed']=item_produce.modified_seed
        item_produce_data['heirloom']=item_produce.heirloom
        item_produce_data['fertilizerTypeUsed']=item_produce.fertilizer_type_used
        item_produce_data['pesticideTypeUsed']=item_produce.pesticide_type_used
        item_produce_data['estQuantityPlanted']=item_produce.estimated_qty_planted
        item_produce_data['certifiedOrganic']=item_produce.certified_organic
        item_produce_data['estFinishedQty']=item_produce.estimated_finished_qty
        item_produce_data['estPrice']=item_produce.est_price_to_be_paid
        item_produce_data['qtyAcceptedForListing']=item_produce.qty_accepted_for_listing
        item_produce_data['qtyAcceptedAtDelivery']=item_produce.qty_accepted_at_delivery
        item_produce_data['chargebacks']=item_produce.chargebacks
        item_produce_data['finalPricePaid']=item_produce.price_paid
        item_produce_data['deliveredDate']=item_produce.delivered_date
        item_produce_data['deliveredTo']=item_produce.delivered_to
        item_produce_data['comments']=item_produce.comments
        item_produce_data['status']=item_produce.status
        output.append(item_produce_data)

    return jsonify({ 'produce': output })
    
@app.route("/produce/", methods=['POST'])
def add_produce_items():
    data=request.get_json()

    new_produce=Produce(
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
    return jsonify({ "Success": True })

@app.route("/produce/modify/", methods=['POST'])
def modify_produce():
    data=request.get_json()
    filterId=data.get('id')
    produce_to_update = db.session.query(Produce).filter(Produce.id == filterId).first()
    produce_to_update.product_name=data.get('type'),
    produce_to_update.package_type=data.get('packageType'),
    produce_to_update.package_size=data.get('packageSize'),
    produce_to_update.package_size_unit=data.get('packageSizeUnit'),
    produce_to_update.est_completion_date=data.get('estCompletionDate'),
    produce_to_update.seed_type=data.get('seedType'),
    produce_to_update.modified_seed=data.get('modifiedSeed'),
    produce_to_update.heirloom=data.get('heirloom'),
    produce_to_update.fertilizer_type_used=data.get('fertilizerTypeUsed'),
    produce_to_update.pesticide_type_used=data.get('pesticideTypeUsed'),
    produce_to_update.estimated_qty_planted=data.get('estQuantityPlanted'),
    produce_to_update.certified_organic=data.get('certifiedOrganic'),
    produce_to_update.estimated_finished_qty=data.get('estFinishedQty'),
    produce_to_update.est_price_to_be_paid=data.get('estPrice'),
    produce_to_update.qty_accepted_for_listing=data.get('qtyAcceptedForListing'),
    produce_to_update.qty_accepted_at_delivery=data.get('qtyAcceptedAtDelivery'),
    produce_to_update.chargebacks=data.get('chargebacks'),
    produce_to_update.price_paid=data.get('finalPricePaid'),
    produce_to_update.delivered_date=data.get('deliveredDate'),
    produce_to_update.delivered_to=data.get('deliveredTo'),
    produce_to_update.comments=data.get('comments'),
    
  
    db.session.commit()
    return jsonify({ "Success": True })


@app.route("/produce/incrementStatus/", methods=['POST'])
def update_produce_items():
    data=request.get_json()
    filterId=data.get('id')
    prodToUpdate=db.session.query(Produce).filter(Produce.id == filterId).first()
    prodToUpdate.status=data.get('nextStatus')
    db.session.commit()
    return jsonify({ "Success": True })



@app.route("/livestock/incrementStatus/", methods=['POST'])   
def update_livestock_items():
    data=request.get_json()
    filterId=data.get('id')
    liveToUpdate=db.session.query(Livestock).filter(Livestock.id==filterId).first()
    liveToUpdate.status=data.get('nextStatus')

    db.session.commit()
    return jsonify({ "Success": True })


@app.route("/login/", methods = ["POST"])
def authenticate_login_user():
    data=request.get_json()
    loginEmail=data.get('email')
    user=db.session.query(Users).filter(Users.email==loginEmail.lower()).first()
    if user:
        user_data={}
        user_data['id']=user.id
        user_data['firstName']=user.first_name
        user_data['lastName']=user.last_name
        user_data['email']=user.email
        user_data['farmName']=user.farm_name
        user_data['isAdmin']=user.is_admin
        return jsonify({ 'user': user_data })
    else:
        return 'Fail', 400

@app.route("/email/", methods=['POST'])   
def send_email_alert():
    data=request.get_json()
    farm_name=data.get('farmName')
    user_email=data.get('email')

    email_system.send_email(farm_name,user_email)
    return jsonify({ "Success": True })



def test_print_function():
    return "hello my friend"


if __name__ == '__main__':
    app.debug = True
    app.run()
