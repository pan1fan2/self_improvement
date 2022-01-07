-- Create table If Not Exists Logs (id int,num varchar(10));
-- insert into Logs (id,num) values ('1', '1');
-- insert into Logs (id,num) values ('2', '1');
-- insert into Logs (id,num) values ('3', '1');
-- insert into Logs (id,num) values ('4', '2');
-- insert into Logs (id,num) values ('5', '1');
-- insert into Logs (id,num) values ('6', '2');
-- insert into Logs (id,num) values ('7', '2');
# 180 consecutive numbers
-- Write an SQL query to find all numbers that appear at least three times consecutively.Logs
--  into Logs (id,num) values ('8', '2');
Select num "ConsecutiveNums"
from (Select num, lead(num,1) over() as 2times,lead(num,2) over() as 3times from Logs) tmp
where num = 2times and 2times = 3times;

-- solution
SELECT a.Num as ConsecutiveNums
FROM Logs a
JOIN Logs b
ON a.id = b.id+1 AND a.num = b.num
JOIN Logs c
ON a.id = c.id+2 AND a.num = c.num;