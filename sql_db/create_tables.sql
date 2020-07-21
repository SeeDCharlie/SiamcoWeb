--create all tables

create table if not exists activities(
	cod					varchar(4),
	description			varchar(500),
	unit				varchar(6),
	valueUnit			numeric,
	primary key (cod)
);

create table if not exists users(
	id_user					serial,
	fName					varchar(50),
	lName					varchar(50),
	userName				varchar(25) unique not null,
	userPass				varchar(25),
	primary key (id_user)	
);

commit;
