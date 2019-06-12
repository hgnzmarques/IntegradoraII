select id, title, valor from vakinhas v
outer apply(
    select sum(value) valor 
    from contributions c 
    where c.vakinha_id = v.id)c
where cast(ending_date as date) >= cast(getdate() as date) 
order by valor asc limit 4;