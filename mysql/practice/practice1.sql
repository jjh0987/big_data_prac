use sqldb;
show tables;
desc usertbl;
select userName,height from userTbl where height in 
((select max(height) from userTbl),(select min(height) from userTbl));
select count(mobile1) from userTbl;

desc buyTBL;
select userID,sum(amount*price) '총 구매액' from buyTbl group by userID;
# where 절에는 집계함수 쓸 수 없다. 서브쿼리로 값 제한 
# having 절은 group by data 에 대해 집계함수를 쓸 수 있다.
select userID,sum(amount*price) '총 구매액' from buyTbl group by userID
having sum(amount*price) > 1000;
select userID,sum(amount*price) '총 구매액' from buyTbl group by userID
having sum(amount*price) > 1000 order by sum(amount*price) asc;
select userID,sum(amount*price) '총 구매액' from buyTbl group by userID
having sum(amount*price) > 1000 order by 2 asc;

select * from buyTbl;
select num,groupName,sum(amount*price) from buyTbl group by groupName,num with rollup;
# 소합계,총합계
select groupName,sum(amount*price) '총 구매액' from buyTbl group by groupName with rollup;

create table testTbl1 (
id 			int,
userName 	char(3),
age 		int
);
insert into testTbl1 values (1,'홍길동',25);
insert into testTbl1(id,userName) values (2,'설현');
insert into testTbl1(age,userName,id) values (25,'하니',3);
insert into testTbl1 values (4,'aaa',20),(5,'bbb',21);
select * from testTbl1;


create table testTbl2 (
id 			int auto_increment primary key,
userName 	char(3),
age 		int
);
# id가 누락되어도 오름차순 넘버링이 된다.
insert into testTbl2 values (null,'aaa',20),(null,'bbb',21),(null,'ccc',22);
select * from testTbl2;
insert into testTbl2 (userName,age) values ('abc',24);
alter table testTbl2 auto_increment = 100;
insert into testTbl2 values (null,'ddd',23);
select * from testTbl2;

set @@auto_increment_increment = 3; # 증분 설정.

create table testTbl3 (
id 			int,
FName 		varchar(50),
LName 		varchar(50)
);
insert into testTbl3 select emp_no,first_name,last_name from employees.employees;

create table testTbl4 (select emp_no,first_name,last_name from employees.employees);

update testTbl3 set Lname = '없음' where Fname = 'Kyoichi';
select * from testTbl3 where Fname = 'Kyoichi';

use sqldb;
update buyTBL set price = price*1.5;
delete from testTbl3 where Fname = 'Aamer';


















