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



use mydb




--Aggeregate 



select max(salary) from student
select min(salary) from student
select avg(salary) from student
select COUNT(*) from student



--The SQL Server GROUP BY clause is used to arrange identical data into groups.

drop table student


create table student
(
id int,
name varchar(30),
salary int,
adress varchar(30)

)



INSERT INTO student (id, name, salary, adress)
VALUES
(1, 'Aamir', 25000, 'Srinagar'),
(2, 'Rahul', 30000, 'Delhi'),
(3, 'Wasiq', 45000, 'Kashmir'),
(4, 'Ayesha', 28000, 'Jammu'),
(5, 'Zubair', 35000, 'Anantnag'),
(6, 'Rohan', 40000, 'Mumbai'),
(7, 'Sana', 32000, 'Srinagar'),
(8, 'Arjun', 50000, 'Delhi'),
(9, 'Irfan', 22000, 'Baramulla'),
(10, 'Priya', 38000, 'Pune'),
(11, 'Adil', 27000, 'Sopore'),
(12, 'Neha', 42000, 'Chennai'),
(13, 'Sameer', 33000, 'Jammu'),
(14, 'Karan', 55000, 'Jammu'),
(15, 'Zoya', 29000, 'Srinagar'),
(16, 'Bilal', 48000, 'Anantnag'),
(17, 'Vikram', 36000, 'Hyderabad'),
(18, 'Hina', 31000, 'Pulwama'),
(19, 'Danish', 60000, 'Delhi'),
(20, 'Mehak', 34000, 'Srinagar')


select * from student


select adress,count(*) from student
group by adress



select adress,avg(salary) from student
group by adress



select adress, sum(salary) from student
group by adress



select * from student
where adress = 'Srinagar' and salary = 30000


select * from student
where adress = 'Srinagar' or salary = 30000



select adress, COUNT(*) as no_employ from student
group by adress
order by no_employ desc


select adress, COUNT(*) from student
group by adress
having count(*)>2






use mydb


select * from student

select adress, max(salary) from student
group by adress


select AVG(salary) from student
where adress = 'Delhi'




select adress, AVG(salary) from student
group by adress
having AVG(salary)>40000


select adress, sum(salary) from student
group by adress
having sum(salary)>100000






/*
constraint are the rules that are applied to particular table

1 . Primary key --uniquely identifies each row
2. Not null -- it doesn't allowed empty value
3. Unique --- it doesnt allow duplicate value
4. check -- it cheks the the condition
5. foreign key --it establish relationship beyween two tables
6. Default-- pre defined value

*/






create table employ
(

id int primary key,
Name varchar(30) not null,
email varchar(50) unique,
adress varchar(30) default 'Srinagar',
salary int,
age int check(age>=18)
)




insert into employ(id,Name,email,adress,salary,age)
values(1,'wasiq','w@gmail.com','BLR',100000,25)


--not null
insert into employ(id,email,adress,salary,age)
values(2,'T@gmail.com','BLR',300000,25)


--unique
insert into employ(id,Name,email,adress,salary,age)
values(3,'w@gmail.com','BLR',50000,25)


--salary null
insert into employ(id,name,email,salary,age)
values(4,'Aahil','a@gmail.com',45000,25)


--check
insert into employ(id,name,email,salary,age)
values(5,'ubaid','u@gmail.com',45000,17)

select * from employ







