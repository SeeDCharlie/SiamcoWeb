select a.cod, a.description, u.symbol, select 'cant', a.valueunit 
from activities as a 
inner join measurement_units as u 
on a.unit  = u.id_unid;
