DROP TABLE Users;

CREATE TABLE Users
(
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
///////////////////
Mailing_street,
  Mailing_city,
  Mailing_province,
  Mailing_country,
  Mailing_postal_code,
  Farm_name,
  Farm_location,
  Billing_street,
  Billing_city,
  Billing_province,
  Billing_country,
  Billing_postal_code,
  Area,
  Is_producer,
  Is_admin,
  Is_other,
  Member_since,
  Farm_type,
  Rating,
  User_comments










  "Test Pigs"
                     "Priddis", "Southern Alberta", "1",
                     "0", "0", "2019-01-31",
                     "Ranch", "5", "123 test street",
                     "Calgary", "AB", "Canada", "W3R4T6",
                     "123 test street"
                     "Lethbridge", "AB", "Canada",
                     "J8I9L5",
                     "anything could be here"