-- Create table If Not Exists courses (student varchar(1),class varchar(10));
-- insert into courses (student,class) values ('A', 'Math');
-- insert into courses (student,class) values ('B', 'English');
-- insert into courses (student,class) values ('C', 'Math');
-- insert into courses (student,class) values ('D', 'Biology');
-- insert into courses (student,class) values ('E', 'Math');
-- insert into courses (student,class) values ('F', 'Computer');
-- insert into courses (student,class) values ('G', 'Math');
-- insert into courses (student,class) values ('H', 'Math');
-- insert into courses (student,class) values ('I', 'Math');
-- Please list out all classes which have more than or equal to 5 students.

select class, count(*) as tot_num
from courses
GROUP BY class
having tot_num > 5

