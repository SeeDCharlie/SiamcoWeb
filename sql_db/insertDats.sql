--create users
insert into users(fname, lname, username, userpass, email, active ) values('Carlos', 'Castillo', 'seed', 'seed777', 'hellocarloscastillo@gmail.com', false);
insert into users(fname, lname, username, userpass, email, active ) values('Rufino Jose', 'Castillo Tabares', 'rufinoadmin', 'rufinoadmin', 'rucasta@gmail.com', false);       
insert into users(fname, lname, username, userpass, email, active ) values('Anderson','','admuno', 'admuno','', false);

--create measure unids

insert into measurement_units(description, code_dian, symbol) values('Unidad Global', '94', 'GL');
insert into measurement_units(description, code_dian, symbol) values('Metro Lineal', 'LM', 'm');
insert into measurement_units(description, code_dian, symbol) values('Metro Cuadrado', 'MTK', 'm²');
insert into measurement_units(description, code_dian, symbol) values('Metro Cubico', 'MTQ', 'm³');
insert into measurement_units(description, code_dian, symbol) values('Metro', 'MTR', 'm');
insert into measurement_units(description, code_dian) values('Mes de Trabajo', 'WM', 'Mes');

-----------

commit;	

------------