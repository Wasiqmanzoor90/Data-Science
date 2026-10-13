create database mydb2

use mydb2


--This is single line comment

/*
this is 
multiline
coment
*/



--Data type is a cconcept which tell us what type of data a particular variable store
/*
--int :- stores numerical value
char (30) :- stores textual data
varchar(30) :- stores textual data
Datetime 
float
*/



/*
DDL --Data defination Language

Create 
Alter
Truncate
drop

*/

use mydb1
drop database mydb2

create database mydb2





use mydb2





create table employ
(
id int,
name varchar(30),
Adress varchar(30)
)


alter table employ
add  roll_no int

select * from employ


alter table employ
drop column adress


truncate table employ

/*
Data Manipulation  Language(DDL)
1. insert -- 
2. Select -- retreives data from table
3. update -- modify existing data
4 . delete 
*/


insert employ(id,name,roll_no)
values(1,'wasiq',12),
(2,'umer',13)



select * from employ



/*
Clause 
In SQL Server, a clause is a built-in keyword used to structure,
filter, group, or organize data within a query
1. select
2. from
3.where
4.Having
5.group by
6. order by
7.Distinct
*/


update employ
set name ='Athar'
where id = 2


delete employ
where id =1


select * from employ






