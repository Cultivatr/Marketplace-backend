

\copy r_facility (facility_name, type_of_facility) FROM 'sample_files/r_facilities.tsv' WITH NULL ''

\copy r_product (name, type, qty_unit) FROM 'sample_files/r_product.tsv' WITH NULL ''

\copy r_status (status_name) FROM 'sample_files/r_status.tsv' WITH NULL ''

\copy users (first_name,last_name,primary_phone,secondary_phone,email,farm_name,farm_location,area,is_producer,is_admin,is_other,member_since,farm_type,rating,mailing_street,mailing_city,mailing_province,mailing_country,mailing_postal_code,billing_street,billing_city,billing_province,billing_country,billing_postal_code,user_comments) from 'sample_files/user.tsv' with null ''

\copy Offered_Item (user_id,product_id,quantity,price_paid,est_birthdate,registration_number,rfid_tag,breed,single_brand,starting_date_of_feed,type_of_feed,est_completion_date,starting_weight,est_finished_weight,hanging_weight,est_price_to_be_paid,date_planted,seed_type,heirloom,gmo,fertilizer_type_used,pesticide_type_used,estimated_qty_planted,estimated_finished_qty,qty_accepted_for_listing,qty_accepted_at_delivery,chargebacks,delivered_date,delivered_to) FROM 'sample_files/offered_item.tsv' WITH NULL ''

\copy status_tracker (status_id,start_date,end_date,offer_id)FROM 'sample_files/status_tracker.tsv' WITH NULL ''

