select v.id, v.title, sum(value) valor from vakinhas v
inner join contributions c on c.vakinha_id = v.id
where cast(ending_date as date) >= cast(now() as date)
group by v.id, v.title
order by valor asc limit (4);
