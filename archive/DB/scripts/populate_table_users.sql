
\copy users from 'sample_files/user.tsv' with null ''

-- update sequence after loading, so it doesn't start counting from 1
-- from https://stackoverflow.com/questions/43606189/how-to-alter-sequence-in-postgresql-with-specific-maxid-from-a-table
do $$
declare maxid int;
begin
    select max(id)+1 from users into maxid;
    execute 'alter SEQUENCE users_id_seq RESTART with '|| maxid;
end;
$$ language plpgsql
