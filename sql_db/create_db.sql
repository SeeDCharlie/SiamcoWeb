/*create user admseed password 'admseed777';
alter role admseed with SUPERUSER; 
create database siamco_db 	with owner admseed; 

commit;

grant all privileges on database siamco_db to admseed;
postgres://zalnvxcuafnhoc:7cd1ad755ed001f66f9b3243a17c5e45535dca43a1e691dc3879093eaacec7ab@ec2-52-72-34-184.compute-1.amazonaws.com:5432/d59dn3h3410eb4
PGUSER=admseed PGPASSWORD=admseed777 heroku pg:push siamco_db 7cd1ad755ed001f66f9b3243a17c5e45535dca43a1e691dc3879093eaacec7ab --app siamcoapp
	
*/
CREATE ROLE admseed;
ALTER ROLE admseed WITH LOGIN PASSWORD 'admseed777' NOSUPERUSER NOCREATEDB NOCREATEROLE;
CREATE DATABASE siamco_db OWNER admseed;
REVOKE ALL ON DATABASE siamco_db FROM PUBLIC;
GRANT CONNECT ON DATABASE siamco_db TO admseed;
GRANT ALL ON DATABASE siamco_db TO admseed;