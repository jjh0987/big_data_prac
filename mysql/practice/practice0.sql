use employees;
select * from departments;
-- select * from employees.titles;
/*select * from departments;*/ -- 범위주석
# show table status;
show tables;
create database test;
show databases;
use test;

create table memberTBL(
id char(8) not null,
memberName char(5) not null,
memberAdd char(20) default 1,
date date,
number int
);

show tables;
desc memberTBL;
drop table memberTBL;

create database sqldb;
use sqldb;
create table userTBL(
	userName char(3) not null primary key,
    birthYear int not null,
    addr char(2) not null,
    mobile char(12)    
);

create table buyTBL(
	userName char(3) not null,
    prodName char(3) not null,
    price int not null,
    amount int not null
);
alter table buyTBL add constraint foreign key(userName) references userTBL(userName);

#--------------------------------------

select * from usertbl;
select * from usertbl where userName='김경호';
select * from usertbl where birthYear >= 1970 and height >= 182;
select * from usertbl wHere birthYear >= 1970 or height >= 182;
select * from usertbl where height between 180 and 183;
select * from usertbl where addr='경남' or addr='전남' or addr='경북';
select * from usertbl where addr in ('경남','전남','경북');
select * from usertbl where userName like '김%';
select * from usertbl where userName like '_종신';
select * from usertbl where height > (select height from usertbl where userName = '김경호');
select * from usertbl where height >= (select min(height) from usertbl where addr='경남');
select * from usertbl where height >= any(select height from usertbl where addr='경남');
select * from usertbl where height >= all(select height from usertbl where addr='경남');
select * from usertbl where height in (select height from usertbl where addr='경남');
select * from usertbl where height = any(select height from usertbl where addr='경남');
select * from usertbl order by mDate;
select * from usertbl order by mDate desc;
select * from usertbl order by mDate desc,userName asc;
select distinct addr from usertbl; 

use employees;
select emp_no, hire_date from employees order by hire_date asc limit 0,5;