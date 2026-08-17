-- 18/08/2026
-- Easy
-- LeetCode 181: Employees Earning More Than Their Managers using a Self Join.

SELECT 
    e1.name AS Employee
FROM 
    Employee e1
JOIN 
    Employee e2 ON e1.managerId = e2.id
WHERE 
    e1.salary > e2.salary;