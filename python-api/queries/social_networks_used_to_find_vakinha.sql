--Seleciona uma Tupla sendo (count de quanto aparece, nome do tipo), procurando quais as "redes sociais" 
--que foram usadas para informar a vakinha
select count(tipo)cnt, 
case 
    when tipo is null then 'TOTAL' 
    else tipo 
end 
TIPO from( 
    SELECT case when utm_campaign in('whatsapp','facebook','twitter','mail') 
    then utm_campaign 
    else 'Outros' 
end tipo 
FROM contributions
WHERE utm_campaign is not null)x 
GROUP BY rollup(x.tipo) 
ORDER BY cnt DESC

