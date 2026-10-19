-- 16/08/2026
-- Easy
-- LeetCode 175: Combine Two Tables using a standard LEFT JOIN.

SELECT 
    firstName, 
    lastName, 
    city, 
    state
FROM 
    Person
LEFT JOIN 
    Address ON Person.personId = Address.personId;