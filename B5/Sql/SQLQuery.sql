
--This is single line comment

--Multi line comment
/*
dsgcksckvjsd
dnksxbncdslhnc
sb ksdbjbsd
bc dsjkblksbj
sbsn
ascnsx
asn*/

--Data Type tells us ehich type of value a variable holds
/*
int --- stores numerical data
char -- stores textual data  fixed length
varchar -- stores textual data variable length
boolean  -- stores true false
--Date   -- stores date
*/


/*
DDL Data defiantion language 
DML Data manipulation language
TCL  Transaction control language
*/


Create database mydb1

drop database mydb1
use mydb1


--Create 
create table student
(
Roll_no int,
Name Varchar(20),
class varchar(10)
)





use mydb1

/*DDL COMANDS
Create   -- creates table
Alter    -- it chages structure of table 
Turncate   --- It deletes data inside a table 
drop  -- it deletes whole table as well as data
*/

alter table student
add section varchar(30)


truncate table student  --deletes data inside table but not table 
drop table student  -- it delets data as well as table
select * from student



/* DML Data manipulation language
Select --- it fetches data from database
insert --it adds data in particular table
update -- it updates existing data in table
delete  -- it delets particular row from table 
*/



select * from student

insert into student(roll_no,name,class)
values(2,'umer','9th'),
(3,'Abdul','11th','c'),
(4,'umi','9th','B'),
(5,'rizwan','9th','c')

--Here we update a particular item in a table

update student
set name ='wasiq'
where roll_no = 1

--here we delete particular row in table
delete student where name = 'wasiq'

select * from student
use mydb1


/*Constraint are rule that are applied to table

Primary-Key--- Uniquely identifies each row in table
Not null --- it doesnt allow nill value in a particular column
Unique  --- the value shouldnt be repeted or we can say it should be unique
Default -- pre defined
check-- to apply condition
Foreign key -- establish relationship be tween two table
*/

create table employ
(
empid int primary key,
name varchar(30) not null,
adress varchar(30) default 'Srinagar'
)


select * from employ

insert into employ(empid,name,adress)
values(2,'umer','bgl')

insert into employ(empid,name,adress)
values(4,'chen','kel')



use mydb1

drop table employ


create table employ
(
empid int Primary key,
email varchar(30) unique,
name varchar(30) not null,
adress varchar(20) default 'srinagar', 
age int check(age>=18),
salary int

)

select * from employ
insert into employ(empid,email,name,adress,age,salary)
values(100,'wasiq@gmai','wasiq','sgr',43,100000),
(101,'maria@gmai','maria','sgr',23,50000),
(102,'tahir@gmai','tahir','poonch',20,20000),
(103,'Adil@gmai','Adil','Kupwara',25,150000),
(104,'muskaan@gmai','Muskaan','sgr',43,10000)


--clause commond in sql means to filter out data, order data etc its use some comonds that are as under
--where
--from
--order by
--having


select * from employ
where email = 'maria@gmai'

select * from employ
where adress = 'sgr'


--And means both of the condition should be true
--or means one of the condition should be true
select * from employ
where adress ='sgr' and salary >30000


select * from employ
where name like '%q'

select * from employ
where name like 'm%'

--Between means range
select * from employ
where salary between 50000 and 100000

select * from employ

--order by simply means to sort data by default it's asscending
select * from employ
order by salary

select * from employ
order by salary desc


select * from employ
order by age



select * from employ
order by age desc


use mydb1

select * from employ
--Aggerate
select max(salary) as max_salary from employ
select min(salary) as min_salary from employ
select avg(salary) as avg_sal from employ
select sum(salary) as total from employ
select count(*) as total_emp from employ 

select * from employ
order by age,name desc


select count(*) from employ
where adress = 'sgr'

select avg(salary) from employ
where adress = 'sgr'

select count(*) as ok from employ
where salary <50000 and adress ='sgr'



select sum(salary) from employ
where adress = 'sgr'

select *  from employ
where adress ='poonch'


select * from employ
where name ='wasiq'

use mydb1
select * from employ

alter table employ
add Department varchar(30)

update employ
set Department = 'Hr'
WHERE empid = 104


--Group by is a clause that organize  rows with same value into group

select adress , count(*) from employ
group by adress


select adress , count(*) as no_employ from employ
group by adress
order by no_employ desc


select department , count(*) as no_employ from employ
group by department
order by no_employ desc

select department, count(*) as no_employ from employ
group by department
having count(*) >1

--it gives highest salary of eah department
select department, max(salary) from employ
group by department

select adress, max(salary) from employ
group by adress


--sub query means query within query

select max(salary) from employ

--second largest salary
select max(salary) from employ 
where salary <(select max(salary) from employ)


use mydb1

create table department
(
Deptid int primary key,
DeptName varchar(30),
DeptLocation varchar(20)

)

create table employ(
empid int primary key,
empname varchar(30),
salary int,
age int check(age>=18),
Deptid int,
foreign key(Deptid) references department(Deptid)

)

insert into department(Deptid,DeptName,DeptLocation)
values(100,'CS','America'),(101,'Marketing','inida'),(102,'HR','Srg')

select * from department






INSERT INTO employ (empid, empname, salary, age, Deptid) VALUES
(1, 'John Doe', 75000, 28, 101),
(2, 'Jane Smith', 82000, 34, 102),
(3, 'Michael Brown', 61000, 22, 100),
(4, 'Emily Davis', 95000, 41, 101),
(5, 'David Wilson', 54000, 25, 100),
(6, 'Sarah Martinez', 88000, 31, 102),
(7, 'James Anderson', 72000, 29, 100),
(8, 'Amanda Thomas', 67000, 27, 101),
(9, 'Robert Jackson', 105000, 45, 100),
(10, 'Lisa White', 59000, 23, 102),
(11, 'William Harris', 83000, 36, 100),
(12, 'Megan Martin', 91000, 38, 100),
(13, 'Kevin Thompson', 64000, 26, 100),
(14, 'Rachel Garcia', 76000, 30, 102),
(15, 'Brian Martinez', 52000, 21, 100),
(16, 'Christine Robinson', 110000, 48, 101),
(17, 'Timothy Clark', 69000, 32, 100),
(18, 'Laura Rodriguez', 80000, 33, 102),
(19, 'Jason Lewis', 58000, 24, 100),
(20, 'Stephanie Lee', 97000, 42, 101),
(21, 'wasiq', 97000, 42, 101),
(22, 'khan', 97000, 42, 101);





select * from employ

--join is a clause that is used to combine rows from two or more table

--inner join retrieves data from two diffrent table based on same column
select e.empname, e.salary, d.deptname from employ e
inner join department d
on e.Deptid = d.Deptid