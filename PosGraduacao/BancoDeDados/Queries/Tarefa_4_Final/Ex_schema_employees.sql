#Exercícios do Schema employees
#Por Daline da Cruz

use employees;

#Exercício 1
#Funcionário desligados
select dept_no as departamento, count(emp_no) as 'quantidade de empregados', year (from_date), year (to_date), (year (to_date) - year (from_date)) as 'Quantidade de anos' from dept_manager where year (to_date) <> '9999' group by (emp_no);
#Funcionário ativos
select dept_no as departamento, count(emp_no) as 'quantidade de empregados', year (from_date), year (to_date) from dept_manager where year (to_date) = '9999' group by (emp_no);

#Exercício 2
#Quantidade de cargos ocupados por cada funcionário
select emp_no, count(title) from titles group by emp_no;

#Exercício 3
#Cria view com a média de cargos por funcionario
create or replace view media_cargos
as 
select emp_no, count(title) as n_cargo
from titles 
group by emp_no;

#Funcionarios que altrapassaram a média geral de cargos
select emp_no, n_cargo from media_cargos where n_cargo > (select avg(n_cargo) as media_geral from media_cargos);

#Funcionarios que ficaram abaixo da média geral de cargos
select emp_no, n_cargo from media_cargos where n_cargo < (select avg(n_cargo) as media_geral from media_cargos);

#Exercício 4
#Criação de view com a média de salários por empregado
create or replace view media_salarios
as
select emp_no, round(avg(salary),2) as media_salario
from salaries 
group by emp_no;

#Funcionarios que atingiram salário acima da média geral
select emp_no as 'Funcionario', media_salario from media_salarios where media_salario > (select round(avg(media_salario),2) as media_geral from media_salarios) order by media_salario desc;
#Funcionarios que ficaram abaixo da média geral de salários
select emp_no as 'Funcionario', media_salario from media_salarios where media_salario < (select round(avg(media_salario),2) as media_geral from media_salarios) order by media_salario desc;
