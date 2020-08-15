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


drop table cotizaciones;
create table if not exists cotizaciones(
	id_cot					serial,
	customerName			varchar(100),
	email					varchar(100),
	workplace				varchar(100),
	workAddress				varchar(400),	
	projectName				varchar(100),
	proNumber				varchar(20),
	durationWork			numeric(5),
	unitDuration			varchar(15),
	id_user					integer,
	dateCreate				date,
	pdfTemplate				text,
	downloaded				bool,
	primary	key(id_cot),
	CONSTRAINT fk_user
      FOREIGN KEY(id_user)
	  REFERENCES users(id_user)
	
);

/*create table if not exists customers(
	id_customer				serial,
	customerName			varchar(100),
	address					varchar(100),
	celphone				numeric(10),

);*/


commit;
