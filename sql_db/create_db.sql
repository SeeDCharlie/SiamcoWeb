create user admseed password 'admseed777';
alter role admseed with SUPERUSER; 
create database siamco_db 	with owner admseed; 

commit;

grant all privileges on database siamco_db to admseed;
	