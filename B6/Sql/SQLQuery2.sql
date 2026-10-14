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
8. Top
*/


update employ
set name ='Athar'
where id = 2


delete employ
where id =1


select * from employ


use mydb2


select * from employ


alter table employ
add age int


delete employ
where id = 2




insert into employ(id,name,salary,age)
values(1,'eshaan',50000,21),
(2,'Wasiq',250000,32),
(3,'Khan',5000,26),
(4,'Athar',150000,22),
(5,'Madeeha',25000,29)



select * from employ


select * from employ
order by salary


select * from employ
order by salary desc


select top 1 * from employ



select top 2 * from employ
order by salary desc









/*
constraint are rules that are applied to a table
1. Primary key --- uniquely idenfies each row
2. not null -- null are not allowes
3. Default --- pre defined
4. check ---apply condtion
5. unique -- duplicate value are not allowed
6. foreign key -- establish relationship netween two tables

*/


drop table employ




create table employ
(
id int Primary key,
Name varchar(50) not null,
Email varchar(50) unique not null,
Adress varchar(100) default 'Srinagr',
age int check(age>=18),
salary int


)


select * from employ



insert into employ(id,Name,Email,age, salary)
values(1,'Wasiq','w@gmail', 29,10000)



insert into employ(id,Name,Email,Adress,age, salary)
values(2,'Ubaid','u@gmail', 'BLR',17,10000)


insert into employ(id,Name,Email,Adress, age,salary)
values(2,'Ubair','t@gmail', 'BLR',20,10000)


insert into employ(id,Name,Adress,age, salary)
values(3,'Ubaid', 'BLR',34,10000)



insert into employ(id,Email,Adress,age, salary)
values(4,'m@gmail','BLR',34,10000)

SELECT * FROM EMPLOY