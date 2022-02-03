use scott;
show tables;
select * from dept;
select * from emp;
select * from emp,dept where emp.deptno = dept.deptno;
select * from emp A,dept B where A.deptno = B.deptno; # alias 이용시 alias 명칭으로 작성.
select a.deptno,a.dname,b.ename from dept a,emp b where a.loc = 'NEW YORK' and a.deptno = b.deptno order by 1;
select a.empno,a.ename,a.deptno,b.deptno as deptno_d,b.dname from dept b, emp a where a.sal < 1500 and a.deptno = b.deptno;
select a.empno,a.ename,a.deptno,b.deptno as deptno_d,b.dname from dept b, emp a where a.sal < 1500 and a.deptno > b.deptno;
# 비등가 조인
select a.empno,a.ename,a.deptno,b.deptno as deptno_d,b.dname from dept b, emp a 
where a.sal < 1500 
and a.deptno > b.deptno 
and b.deptno >= 20;

show tables;
select * from salgrade;
select a.empno,a.ename,a.sal,b.losal,b.hisal,b.grade 
from emp a, salgrade b 
where a.sal between b.losal and b.hisal;
