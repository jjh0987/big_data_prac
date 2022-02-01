CREATE TABLE Reservation(ID INT, Name VARCHAR(30), ReserveDate DATE, RoomNum INT);

CREATE TABLE Customer (ID INT, Name VARCHAR(30), Age INT, Address VARCHAR(20));

 

INSERT INTO Reservation(ID, Name, ReserveDate, RoomNum) VALUES(1, '홍길동', '2016-01-05', 2014);

INSERT INTO Reservation(ID, Name, ReserveDate, RoomNum) VALUES(2, '임꺽정', '2016-02-12', 918);

INSERT INTO Reservation(ID, Name, ReserveDate, RoomNum) VALUES(3, '장길산', '2016-01-16', 1208);

INSERT INTO Reservation(ID, Name, ReserveDate, RoomNum) VALUES(4, '홍길동', '2016-03-17', 504);

 

INSERT INTO Customer (ID, Name, Age, Address) VALUES (1, '홍길동', 17, '서울');

INSERT INTO Customer (ID, Name, Age, Address) VALUES (2, '임꺽정', 11, '인천');

INSERT INTO Customer (ID, Name, Age, Address) VALUES (3, '장길산', 13, '서울');

INSERT INTO Customer (ID, Name, Age, Address) VALUES (4, '전우치', 17, '수원');

show tables;
create table test(id int);
drop table test;

desc Customer;
show table status;
desc Reservation;
alter table Reservation add Phone int not null;
desc Reservation;
alter table Reservation drop RoomNum;
desc Reservation;


use test;
delete from test.reservation where name = '홍길동';

show tables;
select * from customer;
delete from Reservation where id=4;
select * from Reservation;









