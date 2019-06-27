--Seleciona todos os valores das vakinhas por purpose(tipo de vakinha),
--e pode ser usado para fazer o gráfico da mediana dos valores

SELECT ct.value as valor from contributions ct
INNER JOIN vakinhas vk ON ct.vakinha_id = vk.id
WHERE vk.purpose = (
    SELECT purpose FROM vakinhas WHERE id = "id da vakinha selecionada");
