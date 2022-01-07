/* 184. Department Highest Salary 

Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, your SQL query should return the following rows (order of rows does not matter).

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
Explanation:
Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.

*/

select  d.Name Department, e.Name Employee, e.Salary
from Employee_184 e
join Department_184 d on e.departmentId = d.Id
where (e.DepartmentId,e.Salary) in 
(
select DepartmentId , max(Salary)
from Employee_184
group by DepartmentId) 
order by Department,Employee desc;

/*185.Department Top Three Salaries */

WITH department_ranking AS (
SELECT Name AS Employee, Salary ,DepartmentId
  ,DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) AS rnk
FROM Employee_184
)

SELECT d.Name AS Department, r.Employee, r.Salary
FROM department_ranking AS r
JOIN Department_184 AS d
ON r.DepartmentId = d.Id
WHERE r.rnk <= 3
ORDER BY d.Name ASC, r.Salary DESC;
