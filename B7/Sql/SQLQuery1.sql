--this i commet

/*
Multi
line 
commet
*/

/*
Data Type is a process which tells us which type of data a 
particular variable holds

1.int---stores numerical value
2. char --stores textual data
3. varchar --stores textual data
4. boolean -- true/false
5. float -- point values
6. DateTime  ---stores datetime







Data Definition Language (DDL) is a subset of
SQL commands used to define, modify, and remove the structure of database object

1. CREATE
2. ALTER
3. DROP
4. TRUNCATE


DML (Data Manipulation Language) is the subset of SQL commands used to add, read, update,
and delete the actual data stored inside database tables.


1. insert-- inserting data in table
2. update
3. Delete -- it delets an indivial row
4. Select -- it retreives from databse

*/





Create database ilsdb


drop database ilsdb

use ilsdb











create table Student
(
Roll_no int,
name varchar(30),
class varchar(20)
)



select * from STUDENT


alter table  student
add adress varchar(50)


alter table student
drop column adress







use ilsdb


select * from Student



insert into Student(Roll_no,name,class)
values(1,'wasiq','ist'),(2,'Himu','ist')


update Student
set class = '3rd'
where Roll_no=1


delete from Student
where Roll_no = 1


truncate table student
drop table Student
select * from Student







create table employe
(
id int,
name varchar(30),
salary int,
deptname varchar(30)

)


select * from employe


insert into employe(id,name,salary,deptname)
values
(4,'Rubhaan',40,'Sales'),
(1,'wasiq',100,'CS'),
(2,'hemu',20,'HR'),
(3,'Zayiem',10,'CS'),

(4,'Rubhaan',40,'Sales')


select * from employe
where salary =100

select * from employe
where salary >=40


select * from employe
where id = 1


select name from employe

select * from employe


update employe
set name ='hanan'
where id = 4



