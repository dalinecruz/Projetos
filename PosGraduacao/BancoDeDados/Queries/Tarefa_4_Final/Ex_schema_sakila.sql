#Exercícios do Schema sakila
#Por Daline da Cruz

use sakila;

#Exercício 1
# Criação de View com junção para identificação da categoria alugada
create or replace view conta_locacao_categoria
as
select year(r.rental_date) as ano, r.inventory_id, i.film_id, fc.category_id, c.`name` from rental as r
left join inventory as i on r.inventory_id = i.inventory_id
left join film_category as fc on i.film_id = fc.film_id
left join category as c on fc.category_id = c.category_id;

#Locações por categoria em 2005
select `name` as Categoria, count(category_id) as 'Total de locações na categoria', ano from
conta_locacao_categoria
where ano = 2005
group by category_id;

#Locações por categoria em 2006
select `name` as Categoria, count(category_id) as 'Total de locações na categoria', ano from
conta_locacao_categoria
where ano = 2006
group by category_id;

#Exercício 2
#Quantidade de filmes por categoria
select category_id, count(film_id) from film_category group by category_id;

#Valor total das locações separado por filme
select f.title as Filme, sum(p.amount) as soma_valor_locacao from payment as p
left join rental as r on r.rental_id = p.rental_id
left join inventory as i on r.inventory_id = i.inventory_id
left join film as f on i.film_id = f.film_id
group by title
order by soma_valor_locacao desc;

#Valor total das locações separado por categoria
select c.`name` as Categoria, sum(p.amount) as soma_valor_locacao from payment as p
left join rental as r on r.rental_id = p.rental_id
left join inventory as i on r.inventory_id = i.inventory_id
left join film_category as fc on i.film_id = fc.film_id
left join category as c on fc.category_id = c.category_id
group by `name`
order by soma_valor_locacao desc;

#Exercício 3
#Cria view com a media de atuações dos atores
create or replace view media_atuacao
as
select actor_id, count(actor_id) as cont_ator from film_actor group by actor_id;

#Atores com quantidade de atuações acima da média geral
select actor_id as 'Ator com número de atuações acima da média geral', cont_ator 'Total de atuações'from media_atuacao where cont_ator > (select round(avg(cont_ator),0) as media_geral from media_atuacao);

#Atores com quantidade de atuações abaixo da média geral
select actor_id as 'Ator com número de atuações abaixo da média geral', cont_ator 'Total de atuações' from media_atuacao where cont_ator < (select round(avg(cont_ator),0) as media_geral from media_atuacao);

#Exercício 4
#Criação de View com valor total das locações separado por categoria para o ano 2005
create or replace view valor_locacao_categoria_2005
as
select c.`name` as Categoria, sum(p.amount) as soma_valor_locacao from payment as p
left join rental as r on r.rental_id = p.rental_id
left join inventory as i on r.inventory_id = i.inventory_id
left join film_category as fc on i.film_id = fc.film_id
left join category as c on fc.category_id = c.category_id
where year(p.payment_date) = 2005
group by `name`
order by soma_valor_locacao desc;

#Criação de View com valor total das locações separado por categoria para o ano 2006
create or replace view valor_locacao_categoria_2006
as
select c.`name` as Categoria, sum(p.amount) as soma_valor_locacao from payment as p
left join rental as r on r.rental_id = p.rental_id
left join inventory as i on r.inventory_id = i.inventory_id
left join film_category as fc on i.film_id = fc.film_id
left join category as c on fc.category_id = c.category_id
where year(p.payment_date) = 2006
group by `name`
order by soma_valor_locacao desc;

#Média geral de valor de locações para os anos de 2005 e 2006
select round(avg(soma_valor_locacao),2) from valor_locacao_categoria_2006;
select round(avg(soma_valor_locacao),2) from valor_locacao_categoria_2005;

#Categorias que atingiram o valor de locação acima da média geral para o ano de 2005
select categoria as 'Categoria com valor de locação acima da média geral', soma_valor_locacao 'Valor total da categoria' from valor_locacao_categoria_2005 where soma_valor_locacao > (select round(avg(soma_valor_locacao),0) as media_geral from valor_locacao_categoria_2005);
#Categorias com que atingiram o valor de locação acima da média geral para o ano de 2006
select categoria as 'Categoria com valor de locação acima da média geral', soma_valor_locacao 'Valor total da categoria' from valor_locacao_categoria_2006 where soma_valor_locacao > (select round(avg(soma_valor_locacao),0) as media_geral from valor_locacao_categoria_2006);

#Categorias que não atingiram o valor de locação e ficaram abaixo da média geral para o ano de 2005
select categoria as 'Categoria com valor de locação acima da média geral', soma_valor_locacao 'Valor total da categoria' from valor_locacao_categoria_2005 where soma_valor_locacao < (select round(avg(soma_valor_locacao),0) as media_geral from valor_locacao_categoria_2005);
#Categorias com que atingiram o valor de locação acima da média geral para o ano de 2006
select categoria as 'Categoria com valor de locação acima da média geral', soma_valor_locacao 'Valor total da categoria' from valor_locacao_categoria_2006 where soma_valor_locacao < (select round(avg(soma_valor_locacao),0) as media_geral from valor_locacao_categoria_2006);
