-- Create table If Not Exists Employee (Id int,Name Varchar(10),Department Varchar(1),ManagerId int);
-- insert into Employee (Id,Name,Department,ManagerId) values ('101', 'John', 'A',NULL);
-- insert into Employee (Id,Name,Department,ManagerId) values ('102', 'Dan', 'A', '101');
-- insert into Employee (Id,Name,Department,ManagerId) values ('103', 'James', 'A', '101');
-- insert into Employee (Id,Name,Department,ManagerId) values ('104', 'Amy', 'A', '101');
-- insert into Employee (Id,Name,Department,ManagerId) values ('105', 'Anne', 'A', '101');
-- insert into Employee (Id,Name,Department,ManagerId) values ('106', 'Ron', 'B', '101');

/*Q570 Given the Employee table, write a SQL query that finds out managers with at least 5 direct report.*/

select Name 
from Employee
where Id in
(
select ManagerId
from Employee
group by ManagerId
having count(Id) >= 5
);
