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





use mydb2


truncate table employ
select * from employ





INSERT INTO employ (id, Name, Email, Adress, age, salary)
VALUES
(1, 'Ayaan', 'ayaan@gmail.com', 'Srinagar', 22, 25000),
(2, 'Rahul', 'rahul@gmail.com', 'Delhi', 25, 30000),
(3, 'Amit', 'amit@gmail.com', 'Mumbai', 24, 28000),
(4, 'Priya', 'priya@gmail.com', 'Jammu', 23, 32000),
(5, 'Sara', 'sara@gmail.com', 'Srinagar', 26, 35000),
(6, 'Arjun', 'arjun@gmail.com', 'Chandigarh', 28, 40000),
(7, 'Neha', 'neha@gmail.com', 'Delhi', 21, 22000),
(8, 'Rohan', 'rohan@gmail.com', 'Pune', 27, 38000),
(9, 'Zoya', 'zoya@gmail.com', 'Srinagar', 24, 31000),
(10, 'Adil', 'adil@gmail.com', 'Anantnag', 29, 45000),
(11, 'Karan', 'karan@gmail.com', 'Mumbai', 30, 50000),
(12, 'Isha', 'isha@gmail.com', 'Jammu', 22, 26000),
(13, 'Vikas', 'vikas@gmail.com', 'Delhi', 31, 55000),
(14, 'Anaya', 'anaya@gmail.com', 'Pune', 25, 36000),
(15, 'Kabir', 'kabir@gmail.com', 'Srinagar', 28, 42000),
(16, 'Meera', 'meera@gmail.com', 'Jammu', 23, 29000),
(17, 'Farhan', 'farhan@gmail.com', 'Baramulla', 27, 39000),
(18, 'Simran', 'simran@gmail.com', 'Chandigarh', 26, 34000),
(19, 'Danish', 'danish@gmail.com', 'Anantnag', 32, 60000),
(20, 'Ayesha', 'ayesha@gmail.com', 'Srinagar', 24, 33000)




select * from employ


--Aaggergate--
select max(salary) as highest_sal from employ


select min(salary) from 

select avg(age) from employ


select  count(*) from employ

select sum(salary) from employ


select * from employ



select * from employ
where salary>20000 and Adress = 'Srinagar'



select * from employ
where salary>20000 or Adress = 'Srinagr'



select * from employ
where salary between 20000 and 40000


select * from employ
where salary >20000 and salary<=40000


select * from employ
where name like '%a'



select * from employ
where name like 'ay%'



select sum(salary) from employ
where adress = 'Srinagar'


select count(*) as Total_employ from employ
where adress = 'Srinagar'


select * from employ
where adress = 'Srinagar'



select top 1 * from employ
order by salary desc



select * from employ


use mydb2

select * from employ


select adress, count(*) from employ
group by Adress



select  count(*) from employ
where adress = 'Srinagar'


select adress, count(*) from employ
group by Adress



select adress, count(*) as no_employ from employ
group by adress
order by no_employ desc


select adress, max(salary) from employ
group by adress


select adress , COUNT(*) from employ
group by adress
having COUNT(*)>3



select  AVG(salary) from employ
where Adress = 'Delhi'


--Adresses earning average more than 35k
select adress, AVG(salary) from employ
group by adress
having AVG(salary)>35000





select adress, sum(salary) from employ
group by adress
having sum(salary)>100000



select AVG(age) from employ
where Adress = 'delhi'


select adress, avg(age) from employ
group by adress
having AVG(age)>25


use mydb2




drop table department



create table department
(
deptid int primary key,
deptname varchar(30),
deptlocation varchar(30)
)


create table employ
(
empid int primary key,
name varchar(40),
salary int,
age int,
deptid int,
foreign key(deptid) references department(deptid)

)

insert into department(deptid,deptname,deptlocation)
values(100,'HR','BLR'),(101,'SALES','SXR'),(102,'CS','DEL')



select * from department


create table employ





INSERT INTO employ (empid, name, salary, age, deptid)
VALUES
(1, 'Amit', 35000, 25, 100),
(2, 'Priya', 42000, 28, 101),
(3, 'Rahul', 50000, 30, 102),
(4, 'Sneha', 38000, 26, 100),
(5, 'Vikas', 45000, 32, 101),
(6, 'Neha', 55000, 29, 102),
(7, 'Arjun', 30000, 24, 100),
(8, 'Pooja', 48000, 31, 101),
(9, 'Karan', 60000, 35, 102),
(10, 'Anjali', 40000, 27, 100),
(11, 'Rohit', 52000, 33, 101),
(12, 'Simran', 65000, 36, 102),
(13, 'Deepak', 32000, 23, 100),
(14, 'Kavita', 47000, 29, 101),
(15, 'Manish', 58000, 34, 102),
(16, 'Riya', 36000, 25, 100),
(17, 'Sahil', 44000, 28, 101),
(18, 'Divya', 70000, 38, 102),
(19, 'Varun', 39000, 26, 100),
(20, 'Meena', 51000, 32, 101),
(21, 'Akash', 62000, 35, 102),
(22, 'Nisha', 34000, 24, 100),
(23, 'Tarun', 46000, 30, 101),
(24, 'Isha', 75000, 40, 102),
(25, 'Mohit', 41000, 27, 100),
(26, 'Kiran', 53000, 33, 101),
(27, 'Sonia', 68000, 37, 102),
(28, 'Ajay', 37000, 25, 100),
(29, 'Komal', 49000, 31, 101),
(30, 'Ramesh', 80000, 42, 102)






select * from employ
select * from department





select max(salary) from employ
where salary<(select max(salary) from employ)


--employes earning less than averages

select * from employ
where salary<(select AVG(salary) from employ)





--department of rahul

select deptname from department
where deptid = 
(
select deptid from employ
where name = 'Rahul'

)


--highest salary in each department
select * from employ e
where salary=(

select max(salary) from employ
where deptid = e.deptid
)

select * from department

--employes which have dept location SXR

select * from employ
where deptid in
(
select deptid from department
where deptlocation = 'SXR'

)

select max(salary) as Thirdsal from employ
where salary <(select max(salary) from employ
where salary<(select max(salary) from employ )
)





-- 30 question subqueris

