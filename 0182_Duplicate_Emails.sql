--31/07/2026--
--Easy--
-- LeetCode 182: Duplicate Emails using GROUP BY and HAVING clause. --
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;