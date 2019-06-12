-- Deploy fresh database tables

\i '/docker-entrypoint-initdb.d/tables/users.sql'
\i '/docker-entrypoint-initdb.d/tables/offered_items_livestock.sql'
\i '/docker-entrypoint-initdb.d/tables/offered_items_produce.sql'

-- \i '/docker-entrypoint-initdb.d/seed/seed.sql'