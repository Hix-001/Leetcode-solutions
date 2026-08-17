-- 18/08/2026
-- Easy
-- LeetCode 183: Customers Who Never Order using Left Anti-Join.

SELECT 
    c.name AS Customers
FROM 
    Customers c
LEFT JOIN 
    Orders o ON c.id = o.customerId
WHERE 
    o.id IS NULL;