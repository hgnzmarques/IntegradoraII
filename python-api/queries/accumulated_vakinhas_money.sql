select id, title, valor from vakinhas v 
left join(select sum(value)valor,vakinha_id from contributions 
group by vakinha_id) as c on c.vakinha_id = v.id 
where cast(ending_date as date) >= cast(now() as date) 
order by valor asc limit(4)