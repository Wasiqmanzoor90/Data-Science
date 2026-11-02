--This is single line comment

/*
this
is 
multi line-coment
*/

--we creatred a databse here
create database mydb


--here we are deleting our databse
drop database mydb1



use mydb


/*

Data Defination Language DDL

DDL (Data Definition Language) is a subset of SQL commands used to 
define, modify, and manage the structure (schema) of a database.

Here are comands ddl
1. Create
2. Alter 
3. Drop
4. Truncate
5. Rename



Data Manipulation Language DML
Data Manipulation Language (DML) is a subset of SQL commands used to manage and 
manipulate data within existing database structures (tables).

Here are DML comandas

CRUD --

1. Select -- reteives all the data from the database
2. insert -- inserts data in table
3 update --- updates existing data in table
4. delete  -- its delets an indivdual row in table



Transaction Control Laguage(TCL)
1. Commit
2. RollBack



Data Query Language (DQL)
1. Select
*/



/*
Data Type tells us which type of data a variable holds

1. int --holds numerical data
2. varchar --- it holds textual data
3. char -- it holds textual data
4. float --holds decimal value
5. DateTime



*/




Create table student
(

id int,
name varchar(40),
roll_no varchar(20)
)


select * from student



insert into student(id,name,roll_no)
values(2,'Tanfeez',101),
(3,'Ahil',102),
(4,'Arslan',103),
(5,'Ubaid',104)


update student
set name ='Sahil'
where id = 3


update student
set name ='Hasik'
where roll_no=100

delete student
where id =1

select * from student




use mydb




/*
SQL clauses are the built-in structural components of an SQL query
that allow you to filter, group, sort, and restrict data.


Six core sql causes

1. from
2. where
3. having
4. like
5. group by
6. order by 
7. top
*/


alter table student
add salary int



select * from student


update student
set salary = 17000
where id =5




select * from student


select * from student
order by salary



select * from student
order by salary desc



select * from student
where name like 't%'


select * from student
where name like '%d'





select top 2 * from  student
order by salary desc



select * from student
where salary between 10000 and 15000