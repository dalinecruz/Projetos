#Exercícios do Schema world
#Por Daline da Cruz

use world;

#Exercício 1
select continent, sum(population) as 'population' from country group by continent order by sum(population) desc limit 3;

#Exercício 2
select round(avg(lifeexpectancy),1) as 'Média global de espectativa de vida' from country;

create or replace view abaixo_media
as
select `name`, lifeexpectancy 
from country 
where lifeexpectancy < (select round(avg(lifeexpectancy),1) from country) 
order by lifeexpectancy desc;

select `name` as 'Países abaixo da média global de expectativa de vida', lifeexpectancy as 'Expectativa de vida no país' from abaixo_media;

create or replace view acima_media
as
select `name`, lifeexpectancy 
from country 
where lifeexpectancy > (select round(avg(lifeexpectancy),1) from country) 
order by lifeexpectancy desc;

select `name` as 'Países acima da média global de expectativa de vida', lifeexpectancy as 'Expectativa de vida no país' from acima_media;

#Exercício 3
create or replace view media_populacao_continentes
as
select continent, round(avg(population),1) as media
from country 
group by continent 
order by round(avg(population),1) desc; 

select `name` as 'Países com população acima da média continental', population as População from country 
where population > (select media from media_populacao_continentes where continent = 'asia')
and continent = 'asia'
order by population desc;

select `name` as 'Países com população abaixo da média continental', population as População from country 
where population < (select media from media_populacao_continentes where continent = 'europe')
and continent = 'europe'
order by population desc;
