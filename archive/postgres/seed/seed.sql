BEGIN TRANSACTION;

SELECT * FROM users;

INSERT into users (First_name,Last_name,Primary_phone,Secondary_phone,Email,Farm_name,Farm_location,Area,Is_producer,Is_admin,Is_other,Member_since,Farm_type,Rating,Mailing_street,Mailing_city,Mailing_province,Mailing_country,Mailing_postal_code,Billing_street,Billing_city,Billing_province,Billing_country,Billing_postal_code,User_comments)
VALUES("Joe", "Bob", "123-456-7890", "890-123-4567", "test@gmail.com", "jeff's farm", "calgary", "southern alberta", "TRUE", "TRUE", "TRUE", "2018-09-01", "livestock", "5", "none", "none", "none", "none", "none", "none", "none", "none", "none", "none", "hellllooooo");

SELECT * FROM offered_items_produce;

-- INSERT INTO offered_items_produce (
-- Users_id,
-- Product_name,
-- Package_type,
-- Date_planted,
-- Seed_type,
-- Modified_seed,
-- Heirloom,
-- Fertilizer_type_used,
-- Pesticide_type_used,
-- Estimated_qty_planted,
-- GMO,
-- Estimated_finished_qty,
-- Est_price_to_be_paid,
-- Qty_accepted_for_listing,
-- Qty_accepted_at_delivery,
-- Chargebacks,
-- Price_paid,
-- Delivered_date,
-- Delivered_to,
-- Comments,
-- Status
-- )
-- VALUES ("1","Carrots", "Bag","2019-01-01", "Seed","True", "True","Fertilzier","pestocide","90","True","90","100","80","75","0","500","2019-03-01","Calgary","Helllllooooo", "Pending Approval");

SELECT * FROM offered_items_livestock;

COMMIT;