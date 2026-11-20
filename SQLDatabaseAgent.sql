drop schema if exists itx;
create schema itx;
use itx;
Create table STUDENT(Name varchar(25), Class varchar(25),
Section varchar(25), Marks int);
Insert Into STUDENT values('Krish','Data Science','A',90);
Insert Into STUDENT values('John','Data Science','B',100);
Insert Into STUDENT values('Mukesh','Data Science','A',86);
Insert Into STUDENT values('Jacob','DEVOPS','A',50);
Insert Into STUDENT values('Dipesh','DEVOPS','A',35);

select * from STUDENT;

select Name from STUDENT
where Class = 'Data Science';

select Name from student where
marks>=85;