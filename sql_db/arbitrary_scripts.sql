SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'siamco_db' -- ← change this to your DB
  AND pid <> pg_backend_pid();db);
  
 
insert into cotizaciones (customerName,email,workplace,workAddress,
projectName,proNumber,durationWork,unitDuration,id_user,dateCreate,pdfTemplate,downloaded)
values ('Unidad Global','asas','asasas','asdasd','asdasd','asas', );

delete from cotizaciones 
where id_cot = 3;
commit;
select cod from activities where cod =(select max(cod) from activities);

delete from activities where cod = '182';