/* 03/08/2026
Easy
LeetCode 196: Delete Duplicate Emails using a SQL self-join.
*/

DELETE p1
FROM Person p1
JOIN Person p2 
ON p1.email = p2.email AND p1.id > p2.id;

