BEGIN TRANSACTION;

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

COMMIT;