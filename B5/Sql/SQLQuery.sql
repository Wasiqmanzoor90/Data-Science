
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

insert into student(roll_no,name,class,section)
values(2,'umer','9th','B'),
(3,'Abdul','11th','c'),
(4,'umi','9th','B'),
(5,'rizwan','9th','c')

--Here we update a particular item in a table

update student
set name ='wasiq'
where roll_no = 1

--here we delete particular row in table
delete student where name = 'wasiq'


