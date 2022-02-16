# data write
use employees;
select * from departments;
# table 에 export filetable1rtments;
select * from employees;

create table emp (select * from employees limit 10);
select * from emp;

select distinct dept_no from dept_emp;
select concat(deptno,' ',loc) from dept;
select length(concat(deptno,' ',loc)) from dept;
select truncate(22.22,2);
select ename as Name,round(sal/12,1) as round_sal,truncate(sal/12,1) as trunc_sal from emp;
select sysdate();
select ename,hiredate from emp;
select ename,hiredate,extract(year from hiredate),extract(month from hiredate),extract(day from hiredate) from emp;
select ename,hiredate,date(hiredate),year(hiredate),month(hiredate),day(hiredate) from emp;

# select convert
show databases;
use mulcamDB;
drop database mulcamDB;
show tables;
select * from userTable;


use scott;
select * from emp;
select * from salgrade;
select * from dept;

select a.empno,a.deptno,b.loc 
from emp a inner join dept b 
where b.deptno = a.deptno;

select a.empno,a.deptno,b.loc 
from emp a, dept b 
where b.deptno = a.deptno;

select a.ename,a.sal,b.grade
from emp a,salgrade b
where a.sal between b.losal and b.hisal;


select empno,deptno,loc 
from emp a natural join dept b;

select a.empno,a.deptno,b.loc 
from emp a join dept b 
where b.deptno = a.deptno;

select a.empno,deptno,b.loc 
from emp a join dept b using (deptno)
where deptno > 10
order by deptno;

create table temp_dept select * from dept;
select * from temp_dept;

select a.empno,a.deptno,b.dname,c.loc as new
from emp a join dept b on b.deptno = a.deptno
join temp_dept c on c.deptno = b.deptno;

select a.empno,a.deptno,b.dname,c.loc as new
from emp a join dept b join temp_dept c 
on c.deptno = b.deptno and b.deptno = a.deptno;

select a.empno,a.deptno,b.dname,c.loc as new
from emp a,dept b,temp_dept c
where c.deptno = b.deptno and b.deptno = a.deptno;

select * from dept;
select emp.ename,dept.dname from emp a,dept b;

select *,'all' as job from dept;



