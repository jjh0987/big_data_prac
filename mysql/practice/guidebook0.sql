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