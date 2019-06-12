BEGIN TRANSACTION;

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

COMMIT;