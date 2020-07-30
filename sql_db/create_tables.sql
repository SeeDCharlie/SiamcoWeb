--create all tables
create table if not exists measurement_units(
	id_unid					serial,
	description				varchar(50),
	code_dian				varchar(6),
	symbol					varchar(3),
	primary key (id_unid)
);

create table if not exists activities(
	cod					varchar(4),
	description			varchar(500),
	unit				int,
	valueUnit			numeric,
	primary key (cod),
	CONSTRAINT fk_unit
      FOREIGN KEY(unit)
	  REFERENCES measurement_units(id_unid)
);

create table if not exists users(
	id_user					serial,
	fName					varchar(50),
	lName					varchar(50),
	userName				varchar(25) unique not null,
	userPass				varchar(25) not null,
	email					varchar(300),
	active					boolean,
	primary key (id_user)	
);

commit;
