import psycopg2
import psycopg2.extras
import os
import sys
import traceback
from . import user
from . import offered_item_produce
from . import offered_item_livestock

# STRINGS FOR CREATING THE ENVIRONMENT
default_connect = """
host=localhost dbname=cultivatr user=postgres password=secret
"""
db_env = 'DATABASE_URL'

# STRINGS FOR USERS TABLE
create_table_users_string = """
DROP TABLE IF EXISTS Users CASCADE;

CREATE TABLE Users (
  Id SERIAL PRIMARY KEY,
  First_name TEXT,
  Last_name TEXT,
  Primary_phone TEXT,
  Secondary_phone TEXT,
  Email TEXT,
  Farm_name TEXT,
  Farm_location TEXT,
  Area TEXT,
  Is_producer BOOLEAN,
  Is_admin BOOLEAN,
  Is_other BOOLEAN,
  Member_since DATE,
  Farm_type TEXT,
  Rating INT,
  Mailing_street TEXT,
  Mailing_city TEXT,
  Mailing_province TEXT,
  Mailing_country TEXT,
  Mailing_postal_code TEXT,
  Billing_street TEXT,
  Billing_city TEXT,
  Billing_province TEXT,
  Billing_country TEXT,
  Billing_postal_code TEXT,
  User_comments TEXT
);
"""

insert_users_string = """
INSERT INTO Users (
First_name,
Last_name,
Primary_phone,
Secondary_phone,
Email,
Farm_name,
Farm_location,
Area,
Is_producer,
Is_admin,
Is_other,
Member_since,
Farm_type,
Rating,
Mailing_street,
Mailing_city,
Mailing_province,
Mailing_country,
Mailing_postal_code,
Billing_street,
Billing_city,
Billing_province,
Billing_country,
Billing_postal_code,
User_comments
)
VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
  """

update_users_string = """
UPDATE Users
SET
First_name = %s,
Last_name = %s,
Primary_phone = %s,
Secondary_phone = %s,
Email = %s,
Farm_name = %s,
Farm_location = %s,
Area = %s,
Is_producer = %s,
Is_admin = %s,
Is_other = %s,
Member_since = %s,
Farm_type = %s,
Rating = %s,
Mailing_street = %s,
Mailing_city = %s,
Mailing_province = %s,
Mailing_country = %s,
Mailing_postal_code = %s,
Billing_street = %s,
Billing_city = %s,
Billing_province = %s,
Billing_country = %s,
Billing_postal_code = %s,
User_comments = %s
WHERE ID = %s;
"""

drop_users_string = """
DROP TABLE Users;
  """

get_all_users_string = """
SELECT * FROM Users;
"""

get_user_by_id_string = """
SELECT * FROM Users WHERE ID = %s;
"""

# STRINGS FOR OFFERED ITEMS PRODUCE TABLE
create_table_offered_items_produce_string = """
DROP TABLE IF EXISTS Offered_items_produce CASCADE;

CREATE TABLE Offered_items_produce (
Id SERIAL PRIMARY KEY,
Users_id INT REFERENCES Users ON DELETE RESTRICT,
Product_name TEXT,
Package_type TEXT,
Date_planted DATE,
Seed_type TEXT,
Modified_seed BOOLEAN,
Heirloom BOOLEAN,
Fertilizer_type_used TEXT,
Pesticide_type_used TEXT,
Estimated_qty_planted NUMERIC,
GMO BOOLEAN,
Estimated_finished_qty NUMERIC,
Est_price_to_be_paid NUMERIC,
Qty_accepted_for_listing NUMERIC,
Qty_accepted_at_delivery NUMERIC,
Chargebacks NUMERIC,
Price_paid NUMERIC,
Delivered_date DATE,
Delivered_to TEXT,
Comments TEXT,
Status TEXT
);
"""

drop_offered_items_produce_string = """
DROP TABLE Offered_items_produce;
"""

add_offered_item_produce_string = """
INSERT INTO Offered_items_produce (
Users_id,
Product_name,
Package_type,
Date_planted,
Seed_type,
Modified_seed,
Heirloom,
Fertilizer_type_used,
Pesticide_type_used,
Estimated_qty_planted,
GMO,
Estimated_finished_qty,
Est_price_to_be_paid,
Qty_accepted_for_listing,
Qty_accepted_at_delivery,
Chargebacks,
Price_paid,
Delivered_date,
Delivered_to,
Comments,
Status
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

get_offered_items_produce_by_id_string = """
SELECT * FROM Offered_items_produce WHERE Users_id = %s;
"""

get_offered_items_produce_detail_by_id_string="""
SELECT * FROM Offered_items_produce WHERE ID = %s;
"""

get_all_offered_items_produce_string="""
SELECT * FROM Offered_items_produce
"""

update_offered_items_produce_details_string="""
UPDATE Offered_items_produce
SET
Users_id = %s,
Product_name = %s,
Package_type = %s,
Date_planted = %s,
Seed_type = %s,
Modified_seed = %s,
Heirloom = %s,
Fertilizer_type_used = %s,
Pesticide_type_used = %s,
Estimated_qty_planted = %s,
GMO = %s,
Estimated_finished_qty = %s,
Est_price_to_be_paid = %s,
Qty_accepted_for_listing = %s,
Qty_accepted_at_delivery = %s,
Chargebacks = %s,
Price_paid = %s,
Delivered_date = %s,
Delivered_to = %s,
Comments = %s,
Status = %s
WHERE ID = %s;
"""

# STRINGS FOR OFFERED ITEMS LIVESTOCK TABLE
create_table_offered_items_livestock_string = """
DROP TABLE IF EXISTS Offered_items_livestock CASCADE;

CREATE TABLE Offered_items_livestock (
Id SERIAL PRIMARY KEY,
Users_id INT REFERENCES Users ON DELETE RESTRICT,
Product_name TEXT,
Breed TEXT,
Single_brand BOOLEAN,
Est_birthdate DATE,
Registration_number INT,
RFID_tag INT,
Starting_weight NUMERIC,
Hanging_weight NUMERIC,
Chargebacks NUMERIC,
Starting_date_of_feed DATE,
Feed_method TEXT,
Type_of_pasture TEXT,
Type_of_feed TEXT,
Est_completion_date DATE,
Est_finished_weight NUMERIC,
Est_price_to_be_paid NUMERIC,
Quantity INT,
Comments TEXT,
Price_paid NUMERIC,
Delivered_date DATE,
Delivered_to TEXT,
Status TEXT
);
"""

drop_offered_items_livestock_string = """
DROP TABLE Offered_items_livestock;
"""
add_offered_item_livestock_string = """
INSERT INTO Offered_items_livestock (
Users_id,
Product_name,
Breed,
Single_brand,
Est_birthdate,
Registration_number,
RFID_tag,
Starting_weight,
Hanging_weight,
Chargebacks,
Starting_date_of_feed,
Feed_method,
Type_of_pasture,
Type_of_feed,
Est_completion_date,
Est_finished_weight,
Est_price_to_be_paid,
Quantity,
Comments,
Price_paid,
Delivered_date,
Delivered_to,
Status
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

get_offered_items_livestock_by_id_string = """
SELECT * FROM Offered_items_livestock WHERE Users_id = %s;
"""

get_offered_items_livestock_detail_by_id_string="""
SELECT * FROM Offered_items_livestock WHERE ID = %s;
"""

get_all_offered_items_livestock_string="""
SELECT * FROM Offered_items_livestock
"""

update_offered_items_livestock_details_string="""
UPDATE Offered_items_livestock
SET
Users_id = %s,
Product_name = %s,
Breed = %s,
Single_brand = %s,
Est_birthdate = %s,
Registration_number = %s,
RFID_tag = %s,
Starting_weight = %s,
Hanging_weight = %s,
Chargebacks = %s,
Starting_date_of_feed = %s,
Feed_method = %s,
Type_of_pasture = %s,
Type_of_feed = %s,
Est_completion_date = %s,
Est_finished_weight = %s,
Est_price_to_be_paid = %s,
Quantity = %s,
Comments = %s,
Price_paid = %s,
Delivered_date = %s,
Delivered_to = %s,
Status = %s
WHERE ID = %s;
"""

def hello():
    return 'hello world from SQL'

def get_connect_string():
    print(db_env)
    print(default_connect)
    return os.environ.get(db_env, default_connect)

# FUNCTION FOR USERS
def add_user(first_name, last_name, p_number, s_number, email, f_name, f_location, area, is_producer, is_admin, is_other, member_since, f_type, rating, m_street, m_city, m_province, m_country, m_postal_code, b_street, b_city, b_province, b_country, b_postal_code, comments):
    """
    insert a single user into the users table.
    """
    a = sql_util(insert_users_string, [first_name, last_name, p_number, s_number, email, f_name, f_location, area, is_producer, is_admin, is_other, member_since, f_type, rating, m_street, m_city, m_province, m_country, m_postal_code, b_street, b_city, b_province, b_country, b_postal_code, comments])
    return a

def get_users():
    """
    get all users
    """
    sql_results = select(get_all_users_string, None)
    res = []
    for r in sql_results:
      res.append(user.User(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16], r[17], r[18], r[19], r[20], r[21], r[22], r[23], r[24], r[25]))
    return res

def get_user(userID):
    """
    get a user by id
    """
    sql_results = select(get_user_by_id_string, [userID])
    if sql_results:
      r = sql_results[0]
      return user.User(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16], r[17], r[18], r[19], r[20], r[21], r[22], r[23], r[24], r[25])
    return None

def update_user(first_name, last_name, p_number, s_number, email, f_name, f_location, area, is_producer, is_admin, is_other, member_since, f_type, rating, m_street, m_city, m_province, m_country, m_postal_code, b_street, b_city, b_province, b_country, b_postal_code, comments, userID):
    """
    update a user by id
    """
    sql_results = sql_util(update_users_string, [first_name, last_name, p_number, s_number, email, f_name, f_location, area, is_producer, is_admin, is_other, member_since, f_type, rating, m_street, m_city, m_province, m_country, m_postal_code, b_street, b_city, b_province, b_country, b_postal_code, comments, userID])
    if sql_results:
      r = sql_results[0]
      return user.User(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16], r[17], r[18], r[19], r[20], r[21], r[22], r[23], r[24], r[25])
    return None

# FUNCTIONS FOR OFFERED ITEMS PRODUCE
def add_produce_item_by_user_id(Users_id,Product_name,Package_type,Date_planted,Seed_type,Modified_seed,Heirloom,Fertilizer_type_used,Pesticide_type_used,Estimated_qty_planted,GMO,Estimated_finished_qty,Est_price_to_be_paid,Qty_accepted_for_listing,Qty_accepted_at_delivery,Chargebacks,Price_paid,Delivered_date,Delivered_to,Comments,Status):
    """
    add a item by the user id
    """
    sql_results = sql_util(add_offered_item_produce_string, [Users_id,Product_name,Package_type,Date_planted,Seed_type,Modified_seed,Heirloom,Fertilizer_type_used,Pesticide_type_used,Estimated_qty_planted,GMO,Estimated_finished_qty,Est_price_to_be_paid,Qty_accepted_for_listing,Qty_accepted_at_delivery,Chargebacks,Price_paid,Delivered_date,Delivered_to,Comments,Status])
    return sql_results

def get_offered_items_produce_by_id(userID):
    """
    get a offered items by id
    """
    sql_results = select(get_offered_items_produce_by_id_string, [userID])
    res=[]
    for r in sql_results:
      res.append(offered_item_produce.Offered_item_produce(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16], r[17], r[18], r[19], r[20], r[21]))
    return res

def get_offered_items_produce_details_by_id(itemID):
    """
    get a offered item by offered item id
    """
    sql_results = select(get_offered_items_produce_detail_by_id_string, [itemID])
    if sql_results:
      r = sql_results[0]
      return offered_item_produce.Offered_item_produce(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16], r[17], r[18], r[19], r[20], r[21])
    return None

def get_all_offered_items_produce():
    """
    get all offered items available
    """
    sql_results = select(get_all_offered_items_produce_string, None)
    res = []
    for r in sql_results:
      res.append(offered_item_produce.Offered_item_produce(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16], r[17], r[18], r[19], r[20], r[21]))
    return res

def update_offered_items_produce_detail(Users_id,Product_name,Package_type,Date_planted,Seed_type,Modified_seed,Heirloom,Fertilizer_type_used,Pesticide_type_used,Estimated_qty_planted,GMO,Estimated_finished_qty,Est_price_to_be_paid,Qty_accepted_for_listing,Qty_accepted_at_delivery,Chargebacks,Price_paid,Delivered_date,Delivered_to,Comments,Status,ItemID):
    """
    updating the details for offered items produce
    """
    sql_results = sql_util(update_offered_items_produce_details_string, [Users_id,Product_name,Package_type,Date_planted,Seed_type,Modified_seed,Heirloom,Fertilizer_type_used,Pesticide_type_used,Estimated_qty_planted,GMO,Estimated_finished_qty,Est_price_to_be_paid,Qty_accepted_for_listing,Qty_accepted_at_delivery,Chargebacks,Price_paid,Delivered_date,Delivered_to,Comments,Status, ItemID])
    if sql_results:
      r = sql_results[0]
      return offered_item_produce.Offered_item_produce(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16], r[17], r[18], r[19], r[20], r[21]. r[22])
    return None

# FUNCTIONS FOR OFFERED ITEMS LIVESTOCK
def add_livestock_item_by_user_id(Users_id,Product_name,Breed,Single_brand,Est_birthdate,Registration_number,RFID_tag,Starting_weight,Hanging_weight,Chargebacks,Starting_date_of_feed,Feed_method,Type_of_pasture,Type_of_feed,Est_completion_date,Est_finished_weight,Est_price_to_be_paid,Quantity,Comments,Price_paid,Delivered_date,Delivered_to,Status):
    """
    add a item by the user id
    """
    sql_results = sql_util(add_offered_item_livestock_string, [Users_id,Product_name,Breed,Single_brand,Est_birthdate,Registration_number,RFID_tag,Starting_weight,Hanging_weight,Chargebacks,Starting_date_of_feed,Feed_method,Type_of_pasture,Type_of_feed,Est_completion_date,Est_finished_weight,Est_price_to_be_paid,Quantity,Comments,Price_paid,Delivered_date,Delivered_to,Status])
    return sql_results

def get_offered_items_livestock_by_id(userID):
    """
    get a offered items by id
    """
    sql_results = select(get_offered_items_livestock_by_id_string, [userID])
    res=[]
    for r in sql_results:
      res.append(offered_item_livestock.Offered_item_livestock(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16], r[17], r[18], r[19], r[20], r[21], r[22], r[23]))
    return res

def get_offered_items_livestock_details_by_id(itemID):
    """
    get a offered item by offered item id
    """
    sql_results = select(get_offered_items_livestock_detail_by_id_string, [itemID])
    if sql_results:
      r = sql_results[0]
      return offered_item_livestock.Offered_item_livestock(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16], r[17], r[18], r[19], r[20], r[21], r[22], r[23])
    return None

def get_all_offered_items_livestock():
    """
    get all offered items available
    """
    sql_results = select(get_all_offered_items_livestock_string, None)
    res = []
    for r in sql_results:
      res.append(offered_item_livestock.Offered_item_livestock(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16], r[17], r[18], r[19], r[20], r[21], r[22], r[23]))
    return res

def update_offered_items_livestock_detail(Users_id,Product_name,Breed,Single_brand,Est_birthdate,Registration_number,RFID_tag,Starting_weight,Hanging_weight,Chargebacks,Starting_date_of_feed,Feed_method,Type_of_pasture,Type_of_feed,Est_completion_date,Est_finished_weight,Est_price_to_be_paid,Quantity,Comments,Price_paid,Delivered_date,Delivered_to,Status,ItemID):
    """
    updating the details for offered items produce
    """
    sql_results = sql_util(update_offered_items_livestock_details_string, [Users_id,Product_name,Breed,Single_brand,Est_birthdate,Registration_number,RFID_tag,Starting_weight,Hanging_weight,Chargebacks,Starting_date_of_feed,Feed_method,Type_of_pasture,Type_of_feed,Est_completion_date,Est_finished_weight,Est_price_to_be_paid,Quantity,Comments,Price_paid,Delivered_date,Delivered_to,Status,ItemID])
    if sql_results:
      r = sql_results[0]
      return offered_item_livestock.Offered_item_livestock(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16], r[17], r[18], r[19], r[20], r[21]. r[22], r[23], r[24])
    return None

# HELPER FUNCTIONS
def select(sql, parms):
    """
    Execute standard sql statements.
    """
    results = []
    try:
        conn = psycopg2.connect(get_connect_string())
        cur = conn.cursor()
        res = cur.execute(sql, parms)
        for r in cur:
            results.append(r)
    except:
        print('***We had a problem Houston...', sys.exc_info())
        traceback.print_exception(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2])
        raise
    finally:
        cur.close()
        conn.close()

    return results

def sql_util(sql, parm):
    """
    Run general maintaince statements.
    """
    res = []
    try:
        conn = psycopg2.connect(get_connect_string())
        cur = conn.cursor()
        res = cur.execute(sql, parm)
        conn.commit()
    except:
        print('***We had a problem Houston...', sys.exc_info())
        traceback.print_exception(sys.exc_info()[0], sys.exc_info()[
                                  1], sys.exc_info()[2])
        raise
    finally:
        cur.close()
        conn.close()
    return res

# CREATE AND DELETE TABLES
def create_table_offered_items_livestock():
  """
  creating table offered items livestock
  """
  a = sql_util(create_table_offered_items_livestock_string, [])
  return a

def delete_table_offered_items_livestock():
  """
  delete table offered items livestock
  """
  a = sql_util(drop_offered_items_livestock_string, [])
  return a

def create_table_offered_items_produce():
  """
  creating table offered items produce
  """
  a = sql_util(create_table_offered_items_produce_string, [])
  return a

def delete_table_offered_items_produce():
  """
  deleting the table users
  """
  a = sql_util(drop_offered_items_produce_string, [])
  return a

def create_table_users():
  """
  creating table users
  """
  a = sql_util(create_table_users_string,[])
  return a

def delete_table_users():
  """
  deleting the table users
  """
  a = sql_util(drop_users_string, [])
  return a
